model_dir="/home/scy/models/Shanghai_AI_Laboratory/internlm2_5-7b-chat"
lmdeploy serve api_server $model_dir --server-port 23333 --api-keys internlm
