# API 参考

## 概述

New API 提供完整的 RESTful API 接口，分为 **AI 模型接口** 和 **管理接口** 两大类。您可以通过这些接口实现 AI 能力调用和系统管理功能。

{% hint style="info" %}
您可以访问 [Apifox 操练场](https://apifox.newapi.ai/) 在线测试和调试 API 接口，或浏览下方的 API 文档。
{% endhint %}

## AI 模型接口

<table data-view="cards">
  <thead>
    <tr>
      <th>分类</th>
      <th>说明</th>
      <th>文档</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型列表</td>
      <td>获取可用的模型列表。</td>
      <td><a href="ai-model/models/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>聊天</td>
      <td>对话补全接口。</td>
      <td><a href="ai-model/chat/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>补全</td>
      <td>传统文本补全接口。</td>
      <td><a href="ai-model/completions/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>嵌入</td>
      <td>文本嵌入向量生成接口。</td>
      <td><a href="ai-model/embeddings/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>重排序</td>
      <td>文档重排序接口。</td>
      <td><a href="ai-model/rerank/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>审查</td>
      <td>内容安全审核接口。</td>
      <td><a href="ai-model/moderations/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>音频</td>
      <td>语音识别和语音合成接口。</td>
      <td><a href="ai-model/audio/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>实时语音</td>
      <td>实时音频流接口。</td>
      <td><a href="ai-model/realtime/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>图像</td>
      <td>AI图像生成接口。</td>
      <td><a href="ai-model/images/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>视频</td>
      <td>AI视频生成接口。</td>
      <td><a href="ai-model/videos/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>未实现</td>
      <td>占位接口，暂未实现。</td>
      <td><a href="ai-model/unimplemented/README.md">查看文档</a></td>
    </tr>
  </tbody>
</table>

## 管理接口

<table data-view="cards">
  <thead>
    <tr>
      <th>分类</th>
      <th>说明</th>
      <th>文档</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>系统</td>
      <td>系统信息和状态接口。</td>
      <td><a href="management/system/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>系统设置</td>
      <td>系统配置管理接口。</td>
      <td><a href="management/system-settings/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>用户认证</td>
      <td>用户登录、注册、密码管理等接口。</td>
      <td><a href="management/user-auth/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>用户管理</td>
      <td>用户信息管理接口。</td>
      <td><a href="management/user-management/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>双因素认证</td>
      <td>2FA 双因素认证接口。</td>
      <td><a href="management/two-factor-auth/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>OAuth</td>
      <td>第三方 OAuth 登录接口。</td>
      <td><a href="management/oauth/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>渠道管理</td>
      <td>API 渠道配置管理接口。</td>
      <td><a href="management/channel-management/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>模型管理</td>
      <td>模型配置管理接口。</td>
      <td><a href="management/model-management/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>令牌管理</td>
      <td>API 令牌管理接口。</td>
      <td><a href="management/token-management/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>兑换码</td>
      <td>兑换码管理接口。</td>
      <td><a href="management/redemption-codes/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>支付</td>
      <td>支付和充值接口。</td>
      <td><a href="management/payments/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>日志</td>
      <td>使用日志查询接口。</td>
      <td><a href="management/logs/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>统计</td>
      <td>数据统计接口。</td>
      <td><a href="management/statistics/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>任务</td>
      <td>异步任务管理接口。</td>
      <td><a href="management/tasks/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>分组</td>
      <td>用户分组管理接口。</td>
      <td><a href="management/groups/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>供应商</td>
      <td>供应商管理接口。</td>
      <td><a href="management/vendors/README.md">查看文档</a></td>
    </tr>
    <tr>
      <td>安全验证</td>
      <td>安全验证相关接口。</td>
      <td><a href="management/README.md">查看文档</a></td>
    </tr>
  </tbody>
</table>
