import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from implement.decisiontreemodel import DecisionTreeModel
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import ShuffleSplit
from evaluation.sklearnmape import mean_absolute_percentage_error_scoring
from time import time

class TuneModel:
    def __init__(self):

        return
    def runGridSearch(self, model):
        print "run grid search on model {}".format(model.__class__.__name__)
        data = model.loadTransformedData()
        features,labels = data[model.usedFeatures], data[model.usedLabel]
        # do grid search
        estimator = GridSearchCV(model.clf, model.getTunedParamterOptions(), cv=ShuffleSplit(labels.shape[0], n_iter=1000,test_size=.25, random_state=0),
                       scoring=mean_absolute_percentage_error_scoring)
        estimator.fit(features, labels)
        model.clf = estimator.best_estimator_
        
        model.dispFeatureImportance()
        print estimator.best_params_
        print -estimator.best_score_ 
        
        
        return
    def run(self):
        model = DecisionTreeModel()
        model.usedFeatures = [1,2,3]
        t0 = time()
        self.runGridSearch(model)
        print "runGridSearch:", round(time()-t0, 3), "s"
        return




if __name__ == "__main__":   
    obj= TuneModel()
    obj.run()