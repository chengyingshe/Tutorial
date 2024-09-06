NPROC_PER_NODE=2 xtuner train ./internvl_v2_internlm2_2b_qlora_finetune_copy.py  \
        --work-dir /home/scy/models/internvl_ft_run_8_filter  \
        --deepspeed deepspeed_zero1
