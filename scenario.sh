#!/bin/bash

DATA_DIR=script
MODEL_RECOVER_PATH=MODEL/qg_model.bin
EVAL_SPLIT=test
export PYTORCH_PRETRAINED_BERT_CACHE=tmp/bert-cased-pretrained-cache

python ${DATA_DIR}/extraction_answer.py -t $1 -o ${DATA_DIR}/tmp

# run decoding
python src/biunilm/decode_seq2seq.py --bert_model bert-large-cased --new_segment_ids --mode s2s \
  --input_file ${DATA_DIR}/tmp/result_Text_Answer.txt --split ${EVAL_SPLIT} \
  --output_file ${DATA_DIR}/tmp/questions_generated.txt \
  --model_recover_path ${MODEL_RECOVER_PATH} \
  --max_seq_length 512 --max_tgt_length 48 \
  --batch_size 1 --beam_size 1 --length_penalty 0

python ${DATA_DIR}/bert_anwser.py -t ${DATA_DIR}/tmp/result_Text_Answer.txt -q ${DATA_DIR}/tmp/questions_generated.txt -o ./


