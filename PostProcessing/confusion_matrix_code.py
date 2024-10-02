# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import pickle
import copy

goal_set = pickle.load(open('Data/goal_set.p', 'rb'))
disease2groupid = {}
for i in goal_set['train']:
  disease = i['disease_tag']
  group_id = i['group_id']
  disease2groupid[disease] = copy.deepcopy(group_id)

group_id = {'1': 0, '4': 1, '5': 2, '6': 3, '7': 4, '12': 5, '13': 6, '14': 7, '19': 8}

filepath = '{insert the location where the disease_record.p file is located}'
disease_record = pickle.load(open('disease_record.p', 'rb'))

# This variable holds the group-wise performance for each test run.
performance_group_wise = {}

# Iterate over the records in the file. Each batch of 1000 records correspond to a specific test run.
# So, we iterate across batch of 1000s, get the performance value for each batch and store accordingly.

for i in range(0, 5000, 1000):

  # Variables to store the count the number of failed diagnoses and total cases belonging to each group
  wrong_count = np.zeros((9, 9))
  total_count = np.zeros(9)

  for element in disease_record[i:i+1000]:
    true_disease = element[0]
    predicted_disease = element[1]

    id_true_disease = group_id[str(disease2groupid[true_disease])]
    id_predicted_disease = group_id[str(disease2groupid[predicted_disease])]

    if true_disease != predicted_disease:
      wrong_count[id_true_disease][id_predicted_disease] += 1

    total_count[id_true_disease] += 1
  performance_group_wise[str(int(i/1000))] = {'total_count' : copy.deepcopy(total_count), 'wrong_count': copy.deepcopy(wrong_count)}

# This will calculate the proportion of failed cases to the total cases (group-wise) for each test batch
for i in range(0, 5):
  key = str(i)
  for j in range(0, 9):
    performance_group_wise[key]['wrong_count'][j] /= performance_group_wise[key]['total_count'][j]

# Variable that holds the average group-wise performance
average_performance_group_wise = np.zeros((9, 9))
for i in range(0, 5):
  key = str(i)
  average_performance_group_wise += performance_group_wise[key]['wrong_count']

average_performance_group_wise /= 5

#print(average_performance_group_wise)

# Code for plotting the confusion matrix

plt.figure(figsize=(10, 10))
labels = list(group_id.keys())
hm = sn.heatmap(data= average_performance_group_wise, xticklabels=labels, yticklabels=labels, annot=True)

# displaying the plotted heatmap
#plt.title('The error analysis for the disease classifier in different groups on our HRL model')
#plt.xlabel('predicted group')
#plt.ylabel('true group')
plt.show()
plt.savefig('CM.png')
