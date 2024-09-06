#!/bin/bash
xtuner_dir="/home/scy/llm/xtuner"  # config file path
pth_path="/home/scy/models/internvl_ft_run_8_filter/iter_3000.pth"  # trained_model_pth
model_path="/home/scy/models/OpenGVLab/InternVL2-2B-Merged"  # save_path
python $xtuner_dir/xtuner/configs/internvl/v1_5/convert_to_official.py \
        ./internvl_v2_internlm2_2b_qlora_finetune_copy.py \
        $pth_path \
        $model_path