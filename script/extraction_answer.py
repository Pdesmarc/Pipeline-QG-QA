# pour verifier 512 token, importer bert tokenizer, et go cchecker dans le drive Bert_Inference_QA


import argparse
import spacy
from spacy import displacy

def main():
    parser = argparse.ArgumentParser(
        description='Discover driving sessions into log files.')
    parser.add_argument('-t', "--full_text", help='full input text', required=True)
    parser.add_argument('-o', '--output', help='Output folder', required=True)

    args = parser.parse_args()

    process(args.full_text,args.output)


def process(full_text, output):
	listParagraph = []
	listTextProcessed = []

	with open(full_text, 'r') as file:
		for l in file : 
			listParagraph.append(l.rstrip())

	nlp = spacy.load("en_core_web_sm")

	for paragraph in listParagraph : 
		doc = nlp(paragraph)
		#displacy.serve(doc, style="ent")

		textProcessed = ""
		cpt = 0
		for words in doc.ents:
			textProcessed += paragraph + " [SEP] " + words.text + "\n"
			cpt +=1
			if cpt == 5 :
				break
		listTextProcessed.append(textProcessed)
		 

	with open(output + '/result_Text_Answer.txt', 'w') as resultFile:
		for item in listTextProcessed : 
			resultFile.write(item)

if __name__ == '__main__':
    main()