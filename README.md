# AI Text Summarizer

一个命令行版 AI 文本总结工具。

它会读取 `test.txt` 的内容，发送给大模型进行总结，并把结果保存到 `result.json`。

## 功能

- 读取文本文件
- 调用 AI 模型生成总结
- 保存结果为 JSON
- 基本错误处理：
  - 文件不存在
  - API_KEY / API_URL 缺失
  - 请求失败
  - 返回为空或格式异常

## 安装

先创建并激活虚拟环境，然后安装依赖：

```bash
pip install -r requirements.txt