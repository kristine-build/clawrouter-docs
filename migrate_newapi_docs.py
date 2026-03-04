import os
import re
import time
import json
import hashlib
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


START_URL = "https://docs.newapi.pro/zh/docs/api"
ALLOWED_PREFIX = "https://docs.newapi.pro/zh/docs/api"
OUT_DIR = "docs"
SLEEP_SECONDS = 0.8  # be nice to the site


def norm_url(u: str) -> str:
    # Remove fragments and normalize trailing slash-ish.
    u = u.split("#")[0]
    return u.rstrip("/")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff\- ]+", "", text)  # keep CJK
    text = text.replace(" ", "-")
    text = re.sub(r"-{2,}", "-", text)
    return text[:120] or "page"


def safe_filename(url: str, title: str) -> str:
    # Use path + short hash so it's stable & unique.
    path = urlparse(url).path.strip("/").replace("/", "__")
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    base = slugify(title) if title else "page"
    return f"{path}__{base}__{h}.md"


def is_index_only(soup: BeautifulSoup) -> bool:
    text = soup.get_text("\n", strip=True)
    return "Here are the articles in this section" in text


def is_leaf_page(soup: BeautifulSoup) -> bool:
    # Heuristics: leaf pages tend to include endpoints/methods.
    text = soup.get_text("\n", strip=True)
    if "/v1/" in text:
        return True
    for m in ("GET", "POST", "PUT", "DELETE", "PATCH"):
        if re.search(rf"\b{m}\b", text):
            return True
    return False


def extract_article_html(soup):
    # GitBook-style sites usually have <article>.
    article = soup.find("article")
    if article:
        return str(article)
    # fallback: main content
    main = soup.find("main")
    if main:
        return str(main)
    return None


def get_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("mailto:") or href.startswith("javascript:"):
            continue
        full = urljoin(base_url, href)
        full = norm_url(full)
        if full.startswith(ALLOWED_PREFIX):
            links.append(full)
    return sorted(set(links))


def fetch(url: str) -> BeautifulSoup:
    r = requests.get(url, timeout=30, headers={"User-Agent": "clawrouter-doc-migrator/1.0"})
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    visited = set()
    queue = [norm_url(START_URL)]
    saved = []
    skipped = []
    errors = []

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        try:
            soup = fetch(url)
        except Exception as e:
            errors.append({"url": url, "error": str(e)})
            continue

        title = (soup.title.get_text(strip=True) if soup.title else "").replace("·", "-").strip()
        links = get_links(soup, url)

        # Always keep crawling deeper.
        for lk in links:
            if lk not in visited:
                queue.append(lk)

        # Skip index-only pages (like the ones you saw in GitBook)
        if is_index_only(soup) and not is_leaf_page(soup):
            skipped.append({"url": url, "title": title, "reason": "index-only"})
            time.sleep(SLEEP_SECONDS)
            continue

        if not is_leaf_page(soup):
            skipped.append({"url": url, "title": title, "reason": "not-leaf"})
            time.sleep(SLEEP_SECONDS)
            continue

        article_html = extract_article_html(soup)
        if not article_html:
            skipped.append({"url": url, "title": title, "reason": "no-article"})
            time.sleep(SLEEP_SECONDS)
            continue

        # Convert HTML -> Markdown
        content_md = md(article_html, heading_style="ATX", bullets="-")
        content_md = content_md.strip()

        # Add a banner so it’s clear this is migrated
        banner = (
            "> Migrated from NewAPI docs. Content will be adapted for ClawRouter.\n\n"
        )
        final_md = banner + f"# {title or 'ClawRouter Docs'}\n\n" + content_md + "\n"

        filename = safe_filename(url, title)
        out_path = os.path.join(OUT_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_md)

        saved.append({"url": url, "title": title, "file": out_path})
        print(f"Saved ({len(saved)}): {url}")

        time.sleep(SLEEP_SECONDS)

    # Write index
    index_path = os.path.join(OUT_DIR, "_index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# ClawRouter Docs (Migrated)\n\n")
        f.write("> Auto-generated from NewAPI docs. Links below point to local Markdown files.\n\n")
        for item in saved:
            rel = os.path.basename(item["file"])
            t = item["title"] or rel
            f.write(f"- [{t}]({rel})\n")

    # Write report
    report = {
        "start_url": START_URL,
        "visited_count": len(visited),
        "saved_count": len(saved),
        "skipped_count": len(skipped),
        "error_count": len(errors),
        "saved": saved,
        "skipped": skipped,
        "errors": errors,
    }
    report_path = os.path.join(OUT_DIR, "_migration_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\n=== DONE ===")
    print(f"Visited: {len(visited)}")
    print(f"Saved:   {len(saved)}")
    print(f"Skipped: {len(skipped)}")
    print(f"Errors:  {len(errors)}")
    print(f"Index:   {index_path}")
    print(f"Report:  {report_path}")


if __name__ == "__main__":
    main()
