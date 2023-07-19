import datetime  # For getting the timestamp ex. Timestamp: 2023-01-16 2:56:47 PM
from pandas import DataFrame  # getting predicted target to drop and fit other features
from sklearn.ensemble import RandomForestClassifier  # choice of learning model
from sklearn.tree import DecisionTreeClassifier  # 2nd choice comparison learning model
import numpy as np
import joblib  # Does save() properly ... to the specified filepath using joblib? 2nd using joblib??
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
# 2 extra classification models in colab


file_path = "only_training.joblib"
class Machine:  # machine.py for section named "view"
    def __init__(self, df: DataFrame):
        target = df["Rarity"]  # what we are aiming or feature targeted
        features = df.drop(columns=["Rarity"])  # we drop the target to prevent model from cheating
        self.model = RandomForestClassifier()  # DecisionTreeClassifier
        self.name = {self.model}  # the name : RandomForestClassifier()
        self.model.fit(features, target)  # fit the features in the data frame
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #
        # we want the date time .now in string format from the year down to second

    def __call__(self, pred_basis: DataFrame) -> tuple:  # converting dataframe features to tuple
        prediction = self.model.predict(pred_basis)  # this means: RandomForestClassifier.predict
        probabilities = self.model.predict_proba(pred_basis)
        confidence = np.max(probabilities, axis=1)
        return prediction, confidence  # returning numerical rank number and confidence percentage

    def info(self):  # the function returns info about model in the form of 2 strings
        space = "<br>"  # using html to make a line break
        return f"Base Model: Random Forest Classifier {space} Timestamp: {self.timestamp}"
    # in the application we show the model chosen with a string and the proper time .now


    def save(self):
        joblib.dump(self, "only_training.joblib")

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)
