import warnings
warnings.simplefilter('ignore')
import os 
import pandas, unidecode, json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier 

class Main: 
    def __init__(self): 
        #init
            dataset_path, separator = [os.path.join("model", "dataset.txt"), "   "]
            # load and Train model
            self.dataset = pandas.read_csv(dataset_path, names=['sentence', 'label'], sep=separator)
            self.vectorizer = None
            self.score = None
            self.model = None 
            self.train()
    




    def train(self) :
        
        #separate dataset and expected output 
            sentences = self.dataset['sentence'].values
            y = self.dataset['label'].values

            #Split datasets
            sentences_train, sentences_test, y_train, y_test =train_test_split(sentences, y, test_size=0.25, random_state=1000)

            #vectorization of training and testing data
            self.vectorizer = CountVectorizer ()
            self.vectorizer.fit(sentences_train)
            X_train = self.vectorizer.transform(sentences_train)
            X_test = self.vectorizer.transform(sentences_test)

            # Init model and fit it 
            self.model = XGBClassifier(max_depth=2, n_estimator=30)
            self.model.fit(X_train, y_train) 

            
            #Show xgboost parameters
            print(self.model)

            # make predictions for test data 
             
            y_pred = self.model.predict(X_test)
            predictions = [round(value) for value in y_pred]


            # evaluate predictions 
            self.score = accuracy_score(y_test, predictions)
            print("Accuracy:  %.2f%%" % (self.score * 100.0))

            #predictions
    def predict(self, json_text) :
            result = self.vectorizer.transform([unidecode.unidecode(json_text)])
            result = self.model.predict(result)

            if str(result[0]) == "0":
                   sentiment = "Negative"
            
            elif str(result[0]) == "1":
                   sentiment = "Positive"


            return sentiment
            

if __name__ == "__main__":
    main = Main()
    print(main.predict("Depuis ce matin votre application ne marche pas, je n'arrive pas à déverrouiller ma voiture."))
    print(main.predict("j'ai adore la prestation"))
