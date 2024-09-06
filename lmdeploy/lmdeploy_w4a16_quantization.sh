#!/bin/bash

lmdeploy lite auto_awq \
   /home/scy/models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat \
  --calib-dataset 'ptb' \
  --calib-samples 128 \
  --calib-seqlen 2048 \
  --w-bits 4 \
  --w-group-size 128 \
  --batch-size 1 \
  --search-scale False \
  --work-dir /home/scy/models/Shanghai_AI_Laboratory/internlm2_5-1_8b-chat-w4a16-4bit