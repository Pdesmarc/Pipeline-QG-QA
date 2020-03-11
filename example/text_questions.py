import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Discover driving sessions into log files.')
    parser.add_argument('-t', '--full_text', help='full input text', required=True)
    parser.add_argument('-q', '--question_file', help='question generated', required=True)
    parser.add_argument('-o', '--output', help='Output folder', required=True)

    args = parser.parse_args()

    process(args.full_text,args.question_file,args.output)


def process(full_text, question_file, output):
	listParagraph = []
	listQuestion = []
	listTextProcessed = []

	with open(full_text, 'r') as file:
		for l in file : 
			listParagraph.append(l.rstrip())

	with open(question_file, 'r') as question :
		for q in question :
			listQuestion.append(q.rstrip())

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