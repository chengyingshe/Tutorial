model_dir="/home/scy/models/internlm/internlm2-chat-1_8b"
lmdeploy serve api_server $model_dir --server-port 23333 --api-keys internlm2
