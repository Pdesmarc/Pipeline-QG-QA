# Pipeline-QG-QA
Repository of a pipeline between Question generation and Question answering using : [spaCy](https://spacy.io), [UniLMv1](https://github.com/microsoft/unilm/tree/master/unilm-v1), [Bert](https://github.com/huggingface/transformers) 

## Environment

### Linux

The recommended way to run the code is using Linux (ubuntu 18.04) 

In a shell :
```bash
. .bashrc
apt-get update
apt-get install -y vim wget ssh

pip install --user tensorboardX six numpy tqdm path.py pandas scikit-learn lmdb pyarrow py-lz4framed methodtools py-rouge pyrouge nltk
python -c "import nltk; nltk.download('punkt')"
```
Install the repo as a package:
```bash
mkdir ~/code; cd ~/code
git clone https://github.com/Pdesmarc/Pipeline-QG-QA.git
cd ~/code/Pipeline-QG-QA/src
pip install --user --editable .
```

## Set up
### Unilm QG Model
Please download a fine-tuned checkpoint of UniLM QG from [here](https://drive.google.com/open?id=1JN2wnkSRotwUnJ_Z-AbWwoPdP53Gcfsn) (The GDrive is Microsoft property).

Then (if you download the file in ~/Download)
```bash
mkdir ~/code/Pipeline-QG-QA//MODEL/
mv ~/Download/qg_model.bin ~/code/Pipeline-QG-QA//MODEL/
```

### spaCY
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Bert finetuned QA
```bash
pip install transformers
```

## How to run it 
```bash
cd ~/code/Pipeline-QG-QA
./first_scenario.sh argument1
# argument1 = /PATH/TO/YOUR/FILE/NAME_OF_THE_FILE.txt (example : ./scenario.sh ~/code/PipelineQG-QA/example/texte_brut.txt )
```
The output will be a file named : resultat_final_scenario1.txt 
