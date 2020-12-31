import pickle
import os
#from utilities.data_loader import get_embeddings, Task4Loader, prepare_dataset
#from dataset.data_loader import SemEvalDataLoader
#from sklearn.metrics import accuracy_score, f1_score, recall_score

#def evaluation_report(correct, predicted):
#	return recall_score(correct, predicted, average="macro"), #avgRecall
#	(f1_score(correct, predicted, labels=['positive'])+f1_score(correct, predicted, labels=['negative']))/2,#f1posneg
#	accuracy_score(correct, predicted)#accuracy

if __name__ == '__main__':
	models = os.listdir("./saved_models")
	models.remove("score.py") 
	results_dict = {}
	for model in models:
		print("_____MODEL_"+model+"_____")
		results_dict[os.path.splitext(model)[0]] = pickle.load(open('saved_models/'+model, 'rb'))
		print(results_dict[os.path.splitext(model)[0]].keys())
		print(results_dict[os.path.splitext(model)[0]]['3-test.f1_pn'])
		print(results_dict[os.path.splitext(model)[0]]['3-test.M_recall'])
		print(results_dict[os.path.splitext(model)[0]]['3-test.M_precision'])
		input()
