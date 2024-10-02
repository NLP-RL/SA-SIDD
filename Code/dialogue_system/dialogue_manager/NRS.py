import pickle

fslot_set = pickle.load(open("D/fslot_set.p", 'rb'))
slot_set = pickle.load(open("D/slot_set.p", 'rb'))
slot_set.pop('disease')

Non_RS = set(slot_set)-set(fslot_set)
print('NRS:',Non_RS)
