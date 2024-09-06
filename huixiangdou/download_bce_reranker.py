from modelscope.hub.api import HubApi
api = HubApi()
api.login('8295c677-b6c1-4d53-8b5b-b4eac302704e')

from modelscope import snapshot_download
model_id = 'maidalun/bce-reranker-base_v1'
local_dir = '/home/scy/models/maidalun/bce-reranker-base_v1'
model_dir = snapshot_download(model_id, local_dir=local_dir)