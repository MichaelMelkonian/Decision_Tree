#-------------------------------------------------------------------------
# AUTHOR: Michael Melkonian
# FILENAME: Assignment 1 Problem 7d
# SPECIFICATION: Converting 1d data into 2d to output decision tree
# FOR: CS 4200- Assignment #1
# TIME SPENT: 1.5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

# #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# #--> addd your Python code here
X = []
Y = []
# Create dictionary for mapping feature/class categories to numeric values
age = {"Young":1,"Prepresbyopic":2, "Presbyopic":3} #Equating age value to 1,2, or 3
speculate_prescrip = {"Myope":1, "Hypermetrope":2} #Equating SP value to 1 or 2
astigmatism = {"No":1, "Yes":2} #Equating Astig value to 1 or 2
tear_production_rate = {"Reduced":1, "Normal":2} #Equating TPR value to 1 or 2
recommended_lenses = {"No":1, "Yes":2} #Equating CLASSES to 1 or 2

for i in range(len(db)): #traversing through DB or csv file
    feature_row = [age.get(db[i][0]), speculate_prescrip.get(db[i][1]), astigmatism.get(db[i][2]), tear_production_rate.get(db[i][3])] #assigning value to 2d values to columns (age) (astigmatism)
    X.append(feature_row)
    
    class_row = recommended_lenses.get(db[i][4]) #assiging 2d values to classes (Recommended Lenses)
    Y.append(class_row)
    

# #fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

# #plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()