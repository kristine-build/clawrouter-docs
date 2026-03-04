#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

OUTLINE_TEXT = """- API 参考
  - AI 模型接口
    - 音频（Audio）
      - 原生Gemini格式
      - 原生OpenAI格式
        - 文本转语音
        - 音频转录
        - 音频翻译
    - 聊天（Chat）
      - 原生Claude格式
      - 原生Gemini格式
        - Gemini媒体识别
        - Gemini文本聊天
      - 原生OpenAI格式
        - ChatCompletions格式
        - Responses格式
    - 补全（Completions）
      - 原生OpenAI格式
    - 嵌入（Embeddings）
      - 原生OpenAI格式
      - 原生Gemini格式
    - 图像（Images）
      - 原生Gemini格式
        - Gemini原生格式
        - OpenAI聊天格式
      - 原生OpenAI格式
        - 编辑图像
        - 生成图像
      - 通义千问OpenAI格式
        - 生成图像
        - 编辑图像
    - 模型（Models）
      - 列出模型
        - 原生OpenAI格式
        - 原生Gemini格式
    - 审查（Moderations）
      - 原生OpenAI格式
    - 实时语音（Realtime）
      - 原生OpenAI格式
    - 重排序（Rerank）
      - 文档重排序
    - 未实现（Unimplemented）
      - 文件（Files）
        - 上传文件 (未实现)
        - 删除文件 (未实现)
        - 获取文件内容 (未实现)
        - 列出文件 (未实现)
        - 获取文件信息 (未实现)
    - 微调（Fine-tuning）
      - 取消微调任务 (未实现)
      - 创建微调任务 (未实现)
      - 获取微调任务事件 (未实现)
      - 列出微调任务 (未实现)
      - 获取微调任务详情 (未实现)
    - 视频（Videos）
      - 创建视频生成任务
      - 获取视频生成任务状态
      - 即梦格式
        - 即梦视频生成
      - 可灵格式
        - Kling 图生视频
        - Kling 文生视频
        - 获取 Kling 图生视频任务状态
        - 获取 Kling 文生视频任务状态
      - Sora格式
        - 创建视频
        - 获取视频任务状态
        - 获取视频内容
  - 管理接口
    - 鉴权体系说明（Auth）
    - 渠道管理
      - 批量删除渠道
      - 批量设置渠道标签
      - 复制渠道
      - 删除已禁用渠道
      - 获取上游模型列表
      - 获取模型列表
      - 修复渠道能力
      - 获取所有渠道
      - 删除渠道
      - 获取指定渠道
      - 获取渠道密钥
      - 获取已启用模型列表
      - 获取渠道模型列表
      - 管理多密钥
      - 添加渠道
      - 更新渠道
      - 搜索渠道
      - 禁用标签渠道
      - 启用标签渠道
      - 获取标签模型
      - 编辑标签渠道
      - 测试所有渠道
      - 测试指定渠道
      - 更新所有渠道余额
      - 更新指定渠道余额
    - default
      - 使用兑换码
    - 分组
      - 获取所有分组
      - 获取预填分组
      - 删除预填分组
      - 创建预填分组
      - 更新预填分组
    - 日志
      - 删除历史日志
      - 获取所有日志
      - 搜索日志
      - 获取个人日志
      - 搜索个人日志
      - 获取个人日志统计
      - 获取日志统计
      - 通过令牌获取日志
    - 模型管理
      - 获取所有模型元数据
      - 删除模型
      - 获取指定模型
      - 获取缺失模型
      - 创建模型元数据
      - 更新模型元数据
      - 搜索模型
      - 同步上游模型
      - 预览上游模型同步
    - OAuth
      - Discord OAuth登录
      - 绑定邮箱
      - GitHub OAuth登录
      - LinuxDO OAuth登录
      - OIDC登录
      - 生成OAuth State
      - 绑定Telegram
      - Telegram登录
      - 绑定微信
      - 微信OAuth登录
    - 充值
      - Creem Webhook
      - Stripe Webhook
      - 获取支付金额
      - 发起Creem支付
      - 易支付回调
      - 发起易支付
      - 获取Stripe支付金额
      - 发起Stripe支付
      - 获取充值信息
      - 获取用户充值记录
    - 兑换码
      - 获取所有兑换码
      - 删除兑换码
      - 获取指定兑换码
      - 删除无效兑换码
      - 创建兑换码
      - 更新兑换码
      - 搜索兑换码
    - 安全验证
      - 通用安全验证
      - 获取验证状态
    - 数据统计
      - 获取所有额度数据
      - 获取个人额度数据
    - 系统
      - 获取关于信息
      - 获取首页内容
      - 获取模型列表
      - 获取公告
      - 获取定价信息
      - 获取隐私政策
      - 获取倍率配置
      - 获取初始化状态
      - 初始化系统
      - 获取系统状态
      - 测试系统状态
      - 获取Uptime Kuma状态
      - 获取用户协议
    - 系统设置
      - 获取系统选项
      - 迁移控制台设置
      - 更新系统选项
      - 重置模型倍率
      - 获取可同步渠道
      - 获取上游倍率
    - 任务
      - 获取所有Midjourney任务
      - 获取个人Midjourney任务
      - 获取所有任务
      - 获取个人任务
    - 令牌管理
      - 批量删除令牌
      - 获取所有令牌
      - 删除令牌
      - 获取指定令牌
      - 创建令牌
      - 更新令牌
      - 搜索令牌
      - 获取令牌使用情况
    - 两步验证
      - 重新生成备用码
      - 禁用2FA
      - 启用2FA
      - 设置2FA
      - 获取2FA统计
      - 获取2FA状态
    - 用户登陆注册
      - 发送密码重置邮件
      - 获取用户分组列表
      - 两步验证登录
      - 用户登录
      - 用户登出
      - 开始Passkey登录
      - 完成Passkey登录
      - 用户注册
      - 重置密码
      - 发送邮箱验证码
    - 用户管理
      - 转换邀请额度
      - 获取邀请码
      - 获取所有用户
      - 管理员禁用用户2FA
      - 删除用户
      - 获取指定用户
      - 管理员重置用户Passkey
      - 管理用户状态
      - 获取用户可用模型
      - 删除Passkey
      - 获取Passkey状态
      - 开始注册Passkey
      - 完成注册Passkey
      - 开始验证Passkey
      - 完成验证Passkey
      - 创建用户
      - 更新用户
      - 搜索用户
      - 注销当前用户
      - 获取当前用户信息
      - 获取当前用户分组
      - 更新当前用户信息
      - 更新用户设置
      - 生成访问令牌
      - 管理员完成充值
      - 获取所有充值记录
    - 供应商
      - 获取所有供应商
      - 删除供应商
      - 获取指定供应商
      - 创建供应商
      - 更新供应商
      - 搜索供应商
"""

METHOD_LINES = {"GET", "POST", "PUT", "DELETE"}

class Node:
    def __init__(self, title: str):
        self.title = title
        self.children: list[Node] = []


def parse_outline(text: str) -> Node:
    root = Node("ROOT")
    stack: list[tuple[int, Node]] = [(-1, root)]
    for raw in text.splitlines():
        if not raw.strip():
            continue
        if raw.strip() in METHOD_LINES:
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        level = indent // 2
        title = raw.strip()
        if title.startswith("- "):
            title = title[2:].strip()

        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1]
        node = Node(title)
        parent.children.append(node)
        stack.append((level, node))
    return root

EXPLICIT = {
    "API 参考": "api-reference",
    "AI 模型接口": "ai-model",
    "管理接口": "management",
    "音频（Audio）": "audio",
    "聊天（Chat）": "chat",
    "补全（Completions）": "completions",
    "嵌入（Embeddings）": "embeddings",
    "图像（Images）": "images",
    "模型（Models）": "models",
    "审查（Moderations）": "moderations",
    "实时语音（Realtime）": "realtime",
    "重排序（Rerank）": "rerank",
    "未实现（Unimplemented）": "unimplemented",
    "微调（Fine-tuning）": "fine-tuning",
    "视频（Videos）": "videos",
    "原生OpenAI格式": "openai-native",
    "原生Gemini格式": "gemini-native",
    "原生Claude格式": "claude-native",
    "文本转语音": "tts",
    "音频转录": "audio-transcription",
    "音频翻译": "audio-translation",
    "Gemini媒体识别": "gemini-media",
    "Gemini文本聊天": "gemini-chat",
    "ChatCompletions格式": "chat-completions",
    "Responses格式": "responses",
    "Gemini原生格式": "gemini-native",
    "OpenAI聊天格式": "openai-chat-format",
    "通义千问OpenAI格式": "qwen-openai-format",
    "列出模型": "list-models",
    "文档重排序": "document-rerank",
    "文件（Files）": "files",
    "即梦格式": "jimeng",
    "可灵格式": "kling",
    "Sora格式": "sora",
    "鉴权体系说明（Auth）": "auth",
    "渠道管理": "channel-management",
    "分组": "groups",
    "日志": "logs",
    "模型管理": "model-management",
    "OAuth": "oauth",
    "充值": "payments",
    "兑换码": "redemption-codes",
    "安全验证": "security-verification",
    "数据统计": "statistics",
    "系统": "system",
    "系统设置": "system-settings",
    "任务": "tasks",
    "令牌管理": "token-management",
    "两步验证": "two-factor-auth",
    "用户登陆注册": "user-auth",
    "用户管理": "user-management",
    "供应商": "vendors",
}

REPL = [
    ("（", " "), ("）", " "), ("(", " "), (")", " "),
    ("格式", " format"), ("原生", " native"), ("获取", " get "), ("创建", " create "),
    ("删除", " delete "), ("更新", " update "), ("搜索", " search "), ("列表", " list "),
    ("模型", " model "), ("渠道", " channel "), ("用户", " user "), ("日志", " log "),
    ("任务", " task "), ("充值", " payment "), ("令牌", " token "), ("状态", " status "),
    ("验证", " verify "), ("登录", " login "), ("注册", " register "), ("设置", " setting "),
    ("图像", " image "), ("视频", " video "), ("供应商", " vendor "), ("兑换码", " redemption-code "),
]

def slugify(title: str) -> str:
    if title in EXPLICIT:
        return EXPLICIT[title]
    s = title
    for a, b in REPL:
        s = s.replace(a, b)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "item"


def ensure_file(path: Path, title: str):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n", encoding="utf-8")


def write_outline(root: Node, out_path: Path):
    lines: list[str] = []
    def walk(node: Node, depth: int):
        for child in node.children:
            lines.append(f"{'  '*depth}- {child.title}")
            walk(child, depth + 1)
    walk(root, 0)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary_and_stubs(root: Node, docs_root: Path):
    used: dict[str, set[str]] = defaultdict(set)

    def uniq(parent_key: str, base: str) -> str:
        if base not in used[parent_key]:
            used[parent_key].add(base)
            return base
        i = 2
        while f"{base}-{i}" in used[parent_key]:
            i += 1
        cand = f"{base}-{i}"
        used[parent_key].add(cand)
        return cand

    lines = ["# Summary", ""]

    def walk(node: Node, rel_dir: Path, depth: int):
        key = rel_dir.as_posix()
        for child in node.children:
            child_slug = uniq(key, slugify(child.title))
            if child.children:
                child_dir = rel_dir / child_slug
                link = (child_dir / "README.md").as_posix()
                lines.append(f"{'  '*depth}- [{child.title}]({link})")
                ensure_file(docs_root / link, child.title)
                walk(child, child_dir, depth + 1)
            else:
                link = (rel_dir / f"{child_slug}.md").as_posix()
                lines.append(f"{'  '*depth}- [{child.title}]({link})")
                ensure_file(docs_root / link, child.title)

    top = root.children[0]
    lines.append(f"- [{top.title}](README.md)")
    ensure_file(docs_root / "README.md", top.title)
    walk(top, Path("."), 1)

    (docs_root / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_links_exist(summary_path: Path, docs_root: Path) -> list[str]:
    text = summary_path.read_text(encoding="utf-8")
    links = re.findall(r"\(([^)]+\.md)\)", text)
    missing: list[str] = []
    for link in links:
        p = docs_root / link
        if not p.exists():
            missing.append(link)
    return missing


def main():
    repo = Path(__file__).resolve().parents[1]
    docs = repo / "docs"
    docs.mkdir(parents=True, exist_ok=True)

    root = parse_outline(OUTLINE_TEXT)

    write_outline(root, repo / "sidebar_outline.md")
    write_summary_and_stubs(root, docs)

    missing = verify_links_exist(docs / "SUMMARY.md", docs)
    for link in missing:
        ensure_file(docs / link, link.rsplit("/", 1)[-1].replace(".md", ""))

    print(f"docs_root={docs}")
    print(f"outline={repo / 'sidebar_outline.md'}")
    print(f"summary={docs / 'SUMMARY.md'}")
    print(f"missing_links_fixed={len(missing)}")


if __name__ == "__main__":
    main()
