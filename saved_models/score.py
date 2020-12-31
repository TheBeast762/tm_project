import pickle
from utilities.data_loader import prepare_dataset
from dataset.data_loader import SemEvalDataLoader
from sklearn.metrics import accuracy_score, f1_score, recall_score

def evaluation_report(correct, predicted):
	return recall_score(correct, predicted, average="macro"), #avgRecall
	(f1_score(correct, predicted, labels=['positive'])+f1_score(correct, predicted, labels=['negative']))/2,#f1posneg
	accuracy_score(correct, predicted)#accuracy

if __name__ == '__main__':
	embeddings, word_indices = get_embeddings(corpus="datastories.twitter", dim=300)
	gold_data = SemEvalDataLoader().get_gold(task=TASK)
	gX = [obs[1] for obs in gold_data]
	gy = [obs[0] for obs in gold_data]
	gold = prepare_dataset(gX, gy, loader.pipeline, loader.y_one_hot)
	print(gold)

	loaded_model = pickle.load(open('baseline.pickle', 'rb'))
	predicted = loaded_model.predict(gX)
	print(evaluation_report(gY, predicted))