import argparse

#J'en suis a inserer bert à la fin 
# solution ne pas merger text et question ensemble mais le faire comme c'est dans colab

def main():
    parser = argparse.ArgumentParser(
        description='Discover driving sessions into log files.')
    parser.add_argument('-t', '--text_question', help='full input text', required=True)
    parser.add_argument('-o', '--output', help='Output folder', required=True)

    args = parser.parse_args()

    process(args.full_text,args.output)

def process(full_text_question, question_file, output):

	with open(full_text_question, 'r') as file:
		for paragraph in listParagraph :
			textProcessed = ""
			cpt = 0
			for question in listQuestion:
				textProcessed += paragraph + " [SEP] " + question + "\n"
				cpt +=1
				if cpt == 5 :
					break
			listTextProcessed.append(textProcessed)
		 

	with open(output + '/result_Text_Question.txt', 'w') as resultFile:
		for item in listTextProcessed : 
			resultFile.write(item)

if __name__ == '__main__':
    main()