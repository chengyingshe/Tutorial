#模型下载
from modelscope import snapshot_download
model_id = 'Shanghai_AI_Laboratory/internlm2-chat-7b'
local_dir = '/home/scy/models/Shanghai_AI_Laboratory/internlm2-chat-7b'
model_dir = snapshot_download(model_id, local_dir=local_dir)