# AI Text Assistant

一个基于 Streamlit 的 AI 文本处理小工具，支持：

- 文本总结
- 文本改写

## 功能介绍

用户可以在网页中输入文本，并选择对应功能：

- 总结：输出摘要、关键词和行动建议
- 改写：支持正式、简洁、口语化等风格

处理完成后，结果会自动保存到 `result.json`。

## 安装

先创建虚拟环境并激活，然后安装依赖：

```bash
pip install -r requirements.txt