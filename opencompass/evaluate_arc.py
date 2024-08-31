import requests
import json

# 配置API服务器信息
api_url = "http://0.0.0.0:23333/v1"  # 本地API服务器地址
api_key = "internlm2"  # API密钥

# 自定义Prompt
prompt_template = """
Role: 高级问答系统工程师和认知科学家
Background: 用户需要设计一个能够准确回答AI2 Reasoning Challenge（ARC）测试中问题的高级问答系统。ARC测试包含需要复杂推理和常识应用的问题，这些问题超出了传统问答系统的能力范围。
Profile: 你是一个在自然语言处理和机器学习领域具有深厚背景的专家，专注于构建能够理解和推理复杂问题的认知系统。
Skills: 你需要掌握深度学习、知识表示、推理算法和自然语言理解等关键技能，以便构建能够处理ARC级别挑战的系统。
Goals: 开发一个能够准确理解并回答ARC测试中复杂问题的高级问答系统。
Constrains: 系统应能够处理需要推理、常识应用和深层次文本理解的问题，同时保证高准确性和可靠性。
OutputFormat: 输出应包括问题的答案和支持该答案的推理过程。
Workflow:
  1. 理解问题并确定所需的信息和推理类型。
  2. 检索和分析相关的背景知识和事实。
  3. 应用推理算法来整合信息并得出答案。
  4. 验证答案的准确性并通过反例测试来增强系统的鲁棒性。
Examples:
  - 例子1：问题 "Which property of a mineral can be determined just by looking at it?" 答案 "luster" 推理 "通过观察矿物可以确定其光泽，因为光泽是矿物表面反射光的属性，与物理接触无关。"
  - 例子2：问题 "A student riding a bicycle observes that it moves faster on a smooth road than on a rough road. This happens because the smooth road has (A) less gravity (B) more gravity (C) less friction [correct] (D) more friction" 答案 "less friction" 推理 "平滑路面摩擦力小，因此自行车可以更快地移动，因为摩擦力是阻碍运动的力。"
Initialization: 在第一次对话中，请直接输出以下：您好，作为一个专注于复杂问题解答的高级问答系统工程师，我可以帮助您解答需要深度推理和常识应用的问题。请提出您的问题，我将尽我所能提供最准确的答案。

Question: {question}
"""

# 读取ARC数据集
def load_arc_dataset(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# 评测函数
def evaluate(model_url, api_key, dataset):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    results = []

    for item in dataset:
        question = item["question"]
        formatted_prompt = prompt_template.format(question=question)

        payload = {
            "prompt": formatted_prompt,
            "max_tokens": 200  # 设置生成文本的最大长度
        }

        response = requests.post(model_url, headers=headers, json=payload)
        if response.status_code == 200:
            answer = response.json().get("text", "")
            results.append({
                "question": question,
                "answer": answer.strip()
            })
        else:
            print(f"Error {response.status_code}: {response.text}")

    return results

# 主程序
if __name__ == "__main__":
    # 设置ARC数据集路径
    arc_dataset_path = "/home/scy/llm/opencompass/data/ARC/ARC-c/ARC_c_test_contamination_annotations.json"  # 替换为你的ARC数据集路径
    arc_data = load_arc_dataset(arc_dataset_path)
    print(arc_data)
    # 开始评测
    evaluation_results = evaluate(api_url, api_key, arc_data)

    # 输出结果
    for result in evaluation_results:
        print(f"Question: {result['question']}")
        print(f"Answer: {result['answer']}")
        print("-" * 50)
