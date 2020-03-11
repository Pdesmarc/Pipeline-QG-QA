def colab(): 
	path_par = os.path.join('/content/drive/My Drive/Projet_Industriel/data/geo', 'LongText.txt')
	#path_par = os.path.join('/content/drive/My Drive/Projet_Industriel/data/geo', 'geologieTexte2.txt')
	#path_q = os.path.join('/content/drive/My Drive/Projet_Industriel/data/geo', 'geologie_questions2.txt')
	path_q = os.path.join('/content/drive/My Drive/Projet_Industriel/data/geo', 'Question_LongText.txt')

	with open(path_par, "r", encoding="utf-8") as fpar:
	  paragraphs = [x.strip().split('[SEP]')[0] for x in fpar.readlines()]
	  paragraphs = [x.lower() for x in paragraphs]

	with open(path_par, "r", encoding="utf-8") as fr:
	  responses = [x.strip().split('[SEP]')[1] for x in fr.readlines()]
	  responses = [x.lower() for x in responses]

	with open(path_q, "r", encoding="utf-8") as fq:
	  questions = [x for x in fq.readlines()]
	  questions = [x.lower() for x in questions]

	  answers = []
	for j in range(len(questions)):
	  ## Pour faire de l'inférence avec le checkpoint
	  text = paragraphs[j]
	  question = questions[j]
	  print("Number of tokens:", howManyTokens(text, question))
	  #WordPiece tokenizer ==> real number of encoded tokens (512 max) + CLS, SEP and ##xx words
	  input_ids = tokenizer.encode(question, text)
	  print(torch.tensor([input_ids]).shape)
	  #print(input_ids)

	  token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
	  # Tous les tokens dont l'ID est inférieur à 102 correspond aux tokens spécials du type [SEP] ou [CLS]

	  start_scores, end_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([token_type_ids]))
	  #cf https://huggingface.co/transformers/glossary.html#input-ids
	  #print(start_scores, end_scores)
	  all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
	  #print("ALL TOKENS:",all_tokens)
	  answer = ' '.join(all_tokens[torch.argmax(start_scores) : torch.argmax(end_scores)+1])
	  answer = answer.replace(' ##', '')
	  answers.append(answer)
	  ##We need to detokenize the answer before printing it

	  #assert answer == "nine"
	for i, a in enumerate(answers):
	  print("PARAGRAPH:",paragraphs[i])
	  print("\n")
	  print("QUESTION:",questions[i])
	  print("\n")
	  print("ANSWER PREDICTED:", a)
	  print("GOLD ANSWER:", responses[i])
	  print("\n")