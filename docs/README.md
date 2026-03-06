# API 参考

## 概述

New API 提供完整的 RESTful API 接口，分为 **AI 模型接口** 和 **管理接口** 两大类。您可以通过这些接口实现 AI 能力调用和系统管理功能。

## AI 模型接口

- [音频（Audio）](ai-model/audio/README.md)：语音识别和语音合成接口。
- [聊天（Chat）](ai-model/chat/README.md)：对话补全接口。
- [补全（Completions）](ai-model/completions/README.md)：传统文本补全接口。
- [嵌入（Embeddings）](ai-model/embeddings/README.md)：文本嵌入向量生成接口。
- [图像（Images）](ai-model/images/README.md)：AI 图像生成接口。
- [模型（Models）](ai-model/models/README.md)：模型查询与管理接口。
- [审查（Moderations）](ai-model/moderations/README.md)：内容安全审核接口。
- [实时语音（Realtime）](ai-model/realtime/README.md)：实时音频流接口。
- [重排序（Rerank）](ai-model/rerank/README.md)：文档重排序接口。
- [未实现（Unimplemented）](ai-model/unimplemented/README.md)：占位接口，暂未实现。
- [微调（Fine-tuning）](ai-model/fine-tuning/README.md)：模型微调相关接口。
- [视频（Videos）](ai-model/videos/README.md)：AI 视频生成接口。

## 管理接口

- [鉴权体系说明（Auth）](management/auth.md)：鉴权体系说明。
- [渠道管理](management/channel-management/README.md)：API 渠道配置管理接口。
- [default](management/default/README.md)：默认功能接口。
- [分组](management/groups/README.md)：用户分组管理接口。
- [日志](management/logs/README.md)：使用日志查询接口。
- [模型管理](management/model-management/README.md)：模型配置管理接口。
- [OAuth](management/oauth/README.md)：第三方 OAuth 登录接口。
- [充值](management/payments/README.md)：支付与充值接口。
- [兑换码](management/redemption-codes/README.md)：兑换码管理接口。
- [安全验证](management/security-verification/README.md)：安全验证相关接口。
- [数据统计](management/statistics/README.md)：数据统计接口。
- [系统](management/system/README.md)：系统信息和状态接口。
- [系统设置](management/system-settings/README.md)：系统配置管理接口。
- [任务](management/tasks/README.md)：异步任务管理接口。
- [令牌管理](management/token-management/README.md)：API 令牌管理接口。
- [两步验证](management/two-factor-auth/README.md)：2FA 双因素认证接口。
- [用户登陆注册](management/user-auth/README.md)：用户登录、注册、密码管理接口。
- [用户管理](management/user-management/README.md)：用户信息管理接口。
- [供应商](management/vendors/README.md)：供应商管理接口。

**Next：** [原生Gemini格式](ai-model/audio/gemini-native.md)
