from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/v1/messages", methods=["POST"])
def fake_claude():
    data = request.json

    user_messages = [m["content"] for m in data.get("messages", []) if m["role"] == "user"]
    last_user_message = user_messages[-1] if user_messages else "（无用户输入）"

    # 模拟 Claude 的回复格式
    fake_response = {
        "id": "fake-msg-123",
        "type": "message",
        "role": "assistant",
        "model": data.get("model", "fake-claude"),
        "content": [
            {
                "type": "text",
                "text": f"这是本地假 Claude 的回复：你刚才说的是 —— {last_user_message}"
            }
        ]
    }

    return jsonify(fake_response)

if __name__ == "__main__":
    print("🚀 本地假 Claude API 已启动：http://127.0.0.1:5000/v1/messages")
    app.run(host="127.0.0.1", port=5000)
