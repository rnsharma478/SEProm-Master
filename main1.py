from src import readSequenceFile, getParameterDetails, pcaRegressionAlgorithm, motifsAlgorithm, processResults, writeFile,pca,pca_training,reg_training,dataframe_woraround, cross_correlation
from sklearn.decomposition import PCA
from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from src import reg_training_without_pca, random_forest

seq_data = dataframe_woraround.readingCSV()

pca_trained = pca_training.pca_train(seq_data)
# print(len(pca_trained))

reg_training.log_reg(seq_data)

random_forest.random_forest(seq_data)
import sys
sys.exit()

