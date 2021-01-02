import pickle
import matplotlib.pyplot as plt
import numpy as np
import os
#from utilities.data_loader import get_embeddings, Task4Loader, prepare_dataset
#from dataset.data_loader import SemEvalDataLoader
#from sklearn.metrics import accuracy_score, f1_score, recall_score

#def evaluation_report(correct, predicted):
#	return recall_score(correct, predicted, average="macro"), #avgRecall
#	(f1_score(correct, predicted, labels=['positive'])+f1_score(correct, predicted, labels=['negative']))/2,#f1posneg
#	accuracy_score(correct, predicted)#accuracy

if __name__ == '__main__':
	models = ['val_size0.05.pickle', 'val_size0.06.pickle', 'val_size0.07.pickle', 'val_size0.08.pickle', 'val_size0.09.pickle', 'baseline.pickle', 'val_size0.11.pickle', 
		'val_size0.12.pickle', 'val_size0.13.pickle', 'val_size0.14.pickle', 'val_size0.15.pickle']
	for model in models:
		result = pickle.load(open('saved_models/'+model, 'rb'))
		print()
		print("_____MODEL_"+str(model)+"_____")
		print("   f1_pn: "+str(result['3-test.f1_pn'][-1]))
		print("   avg_recall: "+str(result['3-test.M_recall'][-1]))
