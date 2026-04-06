from client import AnthropicClient

client = AnthropicClient()

response = client.chat([
    {"role": "user", "content": "你好，我想测试一下本地假 Claude！"}
])

print(response)
