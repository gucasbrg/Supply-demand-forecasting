
from basemodel import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from preprocess.preparedata import HoldoutSplitMethod

class KNNModel(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.usedFeatures = [9,1]
        self.holdout_split = HoldoutSplitMethod.IMITTATE_TEST2_MIN
        self.save_final_model = True
        self.do_cross_val = False
        return
    def get_train_validation_foldid(self):
        return -1
    def setClf(self):
        clf = KNeighborsClassifier(n_neighbors = 50)
        min_max_scaler = preprocessing.MinMaxScaler()
        self.clf = Pipeline([('scaler', min_max_scaler), ('estimator', clf)])
        return
    def getTunedParamterOptions(self):
#         tuned_parameters = [{'n_neighbors': np.arange(2, 150, 1)}]
        tuned_parameters = [{'estimator__n_neighbors': [5,10]}]
        return tuned_parameters




if __name__ == "__main__":   
    obj= KNNModel()
    obj.run()