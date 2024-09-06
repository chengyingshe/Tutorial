from lmdeploy import pipeline

pipe = pipeline('/home/scy/models/Shanghai_AI_Laboratory/internlm2_5-7b-chat')
response = pipe(['Hi, pls intro yourself', 'Shanghai is'])
print(response)