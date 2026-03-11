# API 参考

## 概述

New API 提供完整的 RESTful API 接口，分为 **AI 模型接口** 和 **管理接口** 两大类。您可以通过这些接口实现 AI 能力调用和系统管理功能。

{% hint style="info" %}
**在线调试**

您可以访问 [Apifox 操练场](https://apifox.newapi.ai/) 在线测试和调试 API 接口，或浏览下方的 API 文档。
{% endhint %}

## AI 模型接口

AI 模型接口提供各种 AI 能力的调用，兼容 OpenAI API 格式。

<table data-view="cards">
  <thead>
    <tr>
      <th>标题</th>
      <th>说明</th>
      <th>链接</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型列表</td>
      <td>获取可用的模型列表。</td>
      <td><a href="ai-model/models/list-models/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>聊天</td>
      <td>对话补全接口。</td>
      <td><a href="ai-model/chat/openai-native/chat-completions.md">查看文档</a></td>
    </tr>
    <tr>
      <td>补全</td>
      <td>传统文本补全接口。</td>
      <td><a href="ai-model/completions/openai-native.md">查看文档</a></td>
    </tr>
    <tr>
      <td>嵌入</td>
      <td>文本嵌入向量生成接口。</td>
      <td><a href="ai-model/embeddings/openai-native.md">查看文档</a></td>
    </tr>
    <tr>
      <td>重排序</td>
      <td>文档重排序接口。</td>
      <td><a href="ai-model/rerank/document-rerank.md">查看文档</a></td>
    </tr>
    <tr>
      <td>审查</td>
      <td>内容安全审核接口。</td>
      <td><a href="ai-model/moderations/openai-native.md">查看文档</a></td>
    </tr>
    <tr>
      <td>音频</td>
      <td>语音识别和语音合成接口。</td>
      <td><a href="ai-model/audio/openai-native/tts.md">查看文档</a></td>
    </tr>
    <tr>
      <td>实时语音</td>
      <td>实时音频流接口。</td>
      <td><a href="ai-model/realtime/openai-native.md">查看文档</a></td>
    </tr>
    <tr>
      <td>图像</td>
      <td>AI图像生成接口。</td>
      <td><a href="ai-model/images/openai-native/image-2.md">查看文档</a></td>
    </tr>
    <tr>
      <td>视频</td>
      <td>AI视频生成接口。</td>
      <td><a href="ai-model/videos/sora/create-video.md">查看文档</a></td>
    </tr>
    <tr>
      <td>未实现</td>
      <td>占位接口，暂未实现。</td>
      <td><a href="ai-model/unimplemented/files/item-2.md">查看文档</a></td>
    </tr>
  </tbody>
</table>

## 管理接口

管理接口用于系统配置、用户管理、业务管理等后台操作。

<table data-view="cards">
  <thead>
    <tr>
      <th>标题</th>
      <th>说明</th>
      <th>链接</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>系统</td>
      <td>系统信息和状态接口。</td>
      <td><a href="management/system/status.md">查看文档</a></td>
    </tr>
    <tr>
      <td>系统设置</td>
      <td>系统配置管理接口。</td>
      <td><a href="management/system-settings/get.md">查看文档</a></td>
    </tr>
    <tr>
      <td>用户认证</td>
      <td>用户登录、注册、密码管理等接口。</td>
      <td><a href="management/user-auth/user-login.md">查看文档</a></td>
    </tr>
    <tr>
      <td>用户管理</td>
      <td>用户信息管理接口。</td>
      <td><a href="management/user-management/get-user-3.md">查看文档</a></td>
    </tr>
    <tr>
      <td>双因素认证</td>
      <td>2FA 双因素认证接口。</td>
      <td><a href="management/two-factor-auth/get-2fa-status.md">查看文档</a></td>
    </tr>
    <tr>
      <td>OAuth</td>
      <td>第三方 OAuth 登录接口。</td>
      <td><a href="management/oauth/github-oauth-login.md">查看文档</a></td>
    </tr>
    <tr>
      <td>渠道管理</td>
      <td>API 渠道配置管理接口。</td>
      <td><a href="management/channel-management/get-channel.md">查看文档</a></td>
    </tr>
    <tr>
      <td>模型管理</td>
      <td>模型配置管理接口。</td>
      <td><a href="management/model-management/get-model.md">查看文档</a></td>
    </tr>
    <tr>
      <td>令牌管理</td>
      <td>API 令牌管理接口。</td>
      <td><a href="management/token-management/get-token.md">查看文档</a></td>
    </tr>
    <tr>
      <td>兑换码</td>
      <td>兑换码管理接口。</td>
      <td><a href="management/redemption-codes/get-redemption-code.md">查看文档</a></td>
    </tr>
    <tr>
      <td>支付</td>
      <td>支付和充值接口。</td>
      <td><a href="management/payments/get-user-payment.md">查看文档</a></td>
    </tr>
    <tr>
      <td>日志</td>
      <td>使用日志查询接口。</td>
      <td><a href="management/logs/get-log.md">查看文档</a></td>
    </tr>
    <tr>
      <td>统计</td>
      <td>数据统计接口。</td>
      <td><a href="management/statistics/get.md">查看文档</a></td>
    </tr>
    <tr>
      <td>任务</td>
      <td>异步任务管理接口。</td>
      <td><a href="management/tasks/get-task.md">查看文档</a></td>
    </tr>
    <tr>
      <td>分组</td>
      <td>用户分组管理接口。</td>
      <td><a href="management/groups/get.md">查看文档</a></td>
    </tr>
    <tr>
      <td>供应商</td>
      <td>供应商管理接口。</td>
      <td><a href="management/vendors/get-vendor.md">查看文档</a></td>
    </tr>
    <tr>
      <td>安全验证</td>
      <td>安全验证相关接口。</td>
      <td><a href="management/security-verification/get-verify-status.md">查看文档</a></td>
    </tr>
  </tbody>
</table>
