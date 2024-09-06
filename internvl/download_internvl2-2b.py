#验证SDK token
from modelscope.hub.api import HubApi
api = HubApi()
api.login('8295c677-b6c1-4d53-8b5b-b4eac302704e')

#模型下载
from modelscope import snapshot_download
model_id = 'OpenGVLab/InternVL2-2B'
local_dir = '/home/scy/models/OpenGVLab/InternVL2-2B'
model_dir = snapshot_download(model_id, local_dir=local_dir)