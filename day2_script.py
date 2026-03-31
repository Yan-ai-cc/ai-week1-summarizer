import json

# 读取 txt 文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 打印全文
print("全文内容：")
print(content)

# 统计字符数
print("\n字符数：", len(content))

# 按行拆分
lines = content.splitlines()

# 打印前两行
print("\n前两行：")
for line in lines[:2]:
    print(line)

# 组织结果
result = {
    "char_count": len(content),
    "line_count": len(lines),
    "preview": lines[:2]
}

# 写入 json 文件
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("\n统计结果已写入 result.json")