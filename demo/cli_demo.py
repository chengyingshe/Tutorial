import torch
from modelscope import AutoTokenizer, AutoModelForCausalLM

model_dir = 'Shanghai_AI_Laboratory/internlm2-chat-1_8b'
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, torch_dtype=torch.float16, trust_remote_code=True).cuda()
model = model.eval()

print("开始对话，输入'exit'退出")

history = []
length = 0
while 1:
    inp = input('[INPUT] ')
    if inp == 'exit':
        print('结束对话。')
        break
    print('[OUTPUT] ', end='')
    for resp, history in model.stream_chat(tokenizer, inp, history=history):
        print(resp[length:], end='', flush=True)
        length = len(resp)
    print()