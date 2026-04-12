import streamlit as st
from utils.llm_api import call_llm
from utils.prompt import build_summary_prompt, build_rewrite_prompt
from utils.file_ops import save_json

st.set_page_config(page_title="AI Text Assistant", page_icon="🤖")

st.title("🤖 AI Text Assistant")
st.write("这是一个基于 Streamlit 的 AI 文本处理小工具，支持文本总结和文本改写。")
st.info("请选择功能后输入文本，再点击开始处理。")

text = st.text_area("请输入文本内容", height=220)

mode = st.selectbox(
    "请选择功能",
    ["总结", "改写"]
)

style = None
if mode == "改写":
    style = st.selectbox(
        "请选择改写风格",
        ["正式", "简洁", "口语化"]
    )

if st.button("开始处理"):
    if not text.strip():
        st.warning("请输入内容后再提交")
    else:
        try:
            if mode == "总结":
                prompt = build_summary_prompt(text)
            else:
                prompt = build_rewrite_prompt(text, style)

            result = call_llm(prompt)

            if not result.strip():
                st.error("模型返回为空，请稍后再试")
            elif result.startswith("请求失败") or result.startswith("错误"):
                st.error(result)
            else:
                st.success("处理完成")

                st.subheader("处理结果")
                st.write(result)

                result_data = {
                    "mode": mode,
                    "style": style if style else "",
                    "input": text,
                    "output": result
                }

                save_json("result.json", result_data)
                st.info("结果已保存到 result.json")

        except Exception as e:
            st.error(f"发生错误：{e}")