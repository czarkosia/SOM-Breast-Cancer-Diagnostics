import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r'Breast Cancer Coimbra_MLR\dataR2.csv')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# splitting data by classes and statistical analysis
n = np.count_nonzero(y==1)
X1 = X.iloc[:n]
X2 = X.iloc[n:]

mean1 = X1.mean()
mean2 = X2.mean()
std1 = X1.std()
std2 = X2.std()

print('Class 1:\nmean values:\n', mean1, '\nstandard deviation:\n', std1,
      '\nClass 2:\nmean values:\n', mean2, '\nstandard deviation:\n', std2)

# creating histograms
def histogram(feature, x1, x2):
      fig, axs = plt.subplots(1,2, sharex=True, sharey=True, figsize=(10,4))

      axs[0].hist(x1[feature], bins=40, edgecolor='black')
      axs[0].set_title(feature + ", class 1")
      axs[0].grid(True)

      axs[1].hist(x2[feature], bins=40, edgecolor='black')
      axs[1].set_title(feature + ", class 2")
      axs[1].grid(True)

      plt.tight_layout()
      plt.show()

for i in range(9):
      histogram(X1.columns[i], X1, X2)

# splitting data of both classes: 80% for training and 20% for tests
rows_1_learn = int(0.8*n)
rows_2_learn = int(0.8*(len(X)-n))

X1_learn = X1.iloc[:rows_1_learn]
X1_test = X1.iloc[rows_1_learn:]

X2_learn = X2.iloc[:rows_2_learn]
X2_test = X2.iloc[rows_2_learn:]