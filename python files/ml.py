import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
new_data = pd.read_csv(r'C:\Users\user\Desktop\Python-2\machine learning\house_prediction\canada_predicted_csv.csv')
new_model = linear_model.LinearRegression()
new_model.fit(new_data[['year']],new_data[['pci']])


predicted_pci = new_model.predict(new_data[['year']])
new_data['predicted_pci'] = predicted_pci
new_data
new_data.to_csv('canada_predicted_csv.csv')
new_data = pd.read_csv('canada_predicted_csv.csv')
plt.scatter(new_data.year,new_data.pci,color='red',label='Actual',marker="+",s=10)
plt.plot(new_data.year,new_data.predicted_pci,color='blue',label='Predicted')
plt.xlabel('year')
plt.ylabel('Per Capita Income')
plt.legend()
plt.show()
