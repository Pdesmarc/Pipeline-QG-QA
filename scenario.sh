#!/bin/bash

DATA_DIR=example
MODEL_RECOVER_PATH=MODEL/qg_model.bin
EVAL_SPLIT=test
export PYTORCH_PRETRAINED_BERT_CACHE=tmp/bert-cased-pretrained-cache

python ${DATA_DIR}/extraction_answer.py -t ${DATA_DIR}/texte_brut.txt -o ${DATA_DIR}

# run decoding
python src/biunilm/decode_seq2seq.py --bert_model bert-large-cased --new_segment_ids --mode s2s \
  --input_file ${DATA_DIR}/result_Text_Answer.txt --split ${EVAL_SPLIT} \
  --output_file ${DATA_DIR}/questions_generated.txt \
  --model_recover_path ${MODEL_RECOVER_PATH} \
  --max_seq_length 512 --max_tgt_length 48 \
  --batch_size 1 --beam_size 1 --length_penalty 0

python ${DATA_DIR}/bert_anwser.py -t ${DATA_DIR}/result_Text_Answer.txt -q ${DATA_DIR}/questions_generated.txt -o ./

# --tokenized_input = Whether the text is tokenized with WordPiece
# run evaluation using our tokenized data as reference
#python src/qg/eval_on_unilm_tokenized_ref.py --out_file src/qg/output/qg.test.output.txt
# run evaluation using tokenized data of Du et al. (2017) as reference
#python src/qg/eval.py --out_file src/qg/output/qg.test.output.txt
