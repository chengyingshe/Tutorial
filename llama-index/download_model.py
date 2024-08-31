# 模型下载
from modelscope import snapshot_download

model_id = 'Ceceliachenen/paraphrase-multilingual-MiniLM-L12-v2'
local_dir = '/home/scy/models/sentence-transformers/'
model_dir = snapshot_download(model_id, local_dir=local_dir)