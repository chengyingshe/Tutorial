#!/bin/bash

lmdeploy serve api_server \
    /home/scy/models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat-w4a16-4bit \
    --model-format awq \
    --quant-policy 4 \
    --cache-max-entry-count 0.4\
    --server-name 0.0.0.0 \
    --server-port 23333 \
    --tp 1