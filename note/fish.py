import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

length = bream_length + smelt_length
weight = bream_weight + smelt_length

len(bream_length)
len(smelt_length)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier

fish_data = [
	[25.4, 242.0],
	[26.3, 290.0],
	...
	 ]

fish_target = [ ]

#데이터를 ML에 먹인다
kn.fit(fish_data, fish_data)

#예측
r = kn.predict([[30.1, 600.123]])
