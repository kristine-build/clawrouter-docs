# API 参考

## AI 模型介面

AI 模型介面提供各种 AI 能力的調用，兼容 OpenAI API 格式。

<table data-view="cards">
  <thead>
    <tr>
      <th>标题</th>
      <th>说明</th>
      <th>連結</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>模型清單</td>
      <td>取得可用的模型清單。</td>
      <td><a href="ai-model/models/list-models/README.md">查看文件</a></td>
    </tr>
    <tr>
      <td>聊天</td>
      <td>對話補全介面。</td>
      <td><a href="ai-model/chat/openai-native/chat-completions.md">查看文件</a></td>
    </tr>
    <tr>
      <td>補全</td>
      <td>传统文本補全介面。</td>
      <td><a href="ai-model/completions/openai-native.md">查看文件</a></td>
    </tr>
    <tr>
      <td>嵌入</td>
      <td>文本嵌入向量生成介面。</td>
      <td><a href="ai-model/embeddings/openai-native.md">查看文件</a></td>
    </tr>
    <tr>
      <td>重排序</td>
      <td>文件重排序介面。</td>
      <td><a href="ai-model/rerank/document-rerank.md">查看文件</a></td>
    </tr>
    <tr>
      <td>審查</td>
      <td>內容安全審核介面。</td>
      <td><a href="ai-model/moderations/openai-native.md">查看文件</a></td>
    </tr>
    <tr>
      <td>音訊</td>
      <td>語音辨識和語音合成介面。</td>
      <td><a href="ai-model/audio/openai-native/tts.md">查看文件</a></td>
    </tr>
    <tr>
      <td>即時語音</td>
      <td>即時音訊流介面。</td>
      <td><a href="ai-model/realtime/openai-native.md">查看文件</a></td>
    </tr>
    <tr>
      <td>图像</td>
      <td>AI图像生成介面。</td>
      <td><a href="ai-model/images/openai-native/image-2.md">查看文件</a></td>
    </tr>
    <tr>
      <td>影片</td>
      <td>AI影片生成介面。</td>
      <td><a href="ai-model/videos/sora/create-video.md">查看文件</a></td>
    </tr>
    <tr>
      <td>未實作</td>
      <td>占位介面，暂未實作。</td>
      <td><a href="ai-model/unimplemented/files/item-2.md">查看文件</a></td>
    </tr>
  </tbody>
</table>

## 管理介面

管理介面用于系統設定、使用者管理、业务管理等后台操作。

<table data-view="cards">
  <thead>
    <tr>
      <th>标题</th>
      <th>说明</th>
      <th>連結</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>系統</td>
      <td>系統資訊和狀態介面。</td>
      <td><a href="management/system/status.md">查看文件</a></td>
    </tr>
    <tr>
      <td>系統設定</td>
      <td>系統設定管理介面。</td>
      <td><a href="management/system-settings/get.md">查看文件</a></td>
    </tr>
    <tr>
      <td>使用者驗證</td>
      <td>使用者登入、註冊、密碼管理等介面。</td>
      <td><a href="management/user-auth/user-login.md">查看文件</a></td>
    </tr>
    <tr>
      <td>使用者管理</td>
      <td>使用者資訊管理介面。</td>
      <td><a href="management/user-management/get-user-3.md">查看文件</a></td>
    </tr>
    <tr>
      <td>双因素驗證</td>
      <td>2FA 双因素驗證介面。</td>
      <td><a href="management/two-factor-auth/get-2fa-status.md">查看文件</a></td>
    </tr>
    <tr>
      <td>OAuth</td>
      <td>第三方 OAuth 登入介面。</td>
      <td><a href="management/oauth/github-oauth-login.md">查看文件</a></td>
    </tr>
    <tr>
      <td>渠道管理</td>
      <td>API 渠道設定管理介面。</td>
      <td><a href="management/channel-management/get-channel.md">查看文件</a></td>
    </tr>
    <tr>
      <td>模型管理</td>
      <td>模型設定管理介面。</td>
      <td><a href="management/model-management/get-model.md">查看文件</a></td>
    </tr>
    <tr>
      <td>令牌管理</td>
      <td>API 令牌管理介面。</td>
      <td><a href="management/token-management/get-token.md">查看文件</a></td>
    </tr>
    <tr>
      <td>兑换码</td>
      <td>兑换码管理介面。</td>
      <td><a href="management/redemption-codes/get-redemption-code.md">查看文件</a></td>
    </tr>
    <tr>
      <td>支付</td>
      <td>支付和充值介面。</td>
      <td><a href="management/payments/get-user-payment.md">查看文件</a></td>
    </tr>
    <tr>
      <td>日誌</td>
      <td>使用日誌查询介面。</td>
      <td><a href="management/logs/get-log.md">查看文件</a></td>
    </tr>
    <tr>
      <td>统计</td>
      <td>資料统计介面。</td>
      <td><a href="management/statistics/get.md">查看文件</a></td>
    </tr>
    <tr>
      <td>任務</td>
      <td>异步任務管理介面。</td>
      <td><a href="management/tasks/get-task.md">查看文件</a></td>
    </tr>
    <tr>
      <td>分组</td>
      <td>使用者分组管理介面。</td>
      <td><a href="management/groups/get.md">查看文件</a></td>
    </tr>
    <tr>
      <td>供应商</td>
      <td>供应商管理介面。</td>
      <td><a href="management/vendors/get-vendor.md">查看文件</a></td>
    </tr>
    <tr>
      <td>安全驗證</td>
      <td>安全驗證相关介面。</td>
      <td><a href="management/security-verification/get-verify-status.md">查看文件</a></td>
    </tr>
  </tbody>
</table>
