from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

learn_data = [[0], [1], [2], [3], [4], [5], [6]]
learn_label = [[0], [2], [4], [6], [8], [10], [12]]

lr = LinearRegression()

lr.fit(learn_data, learn_label)

test_data = [[7], [8], [9], [10]]
test_label = lr.predict(test_data)

print(test_data, "の予測結果:", test_label)
print(" 正解率 = ", accuracy_score([14, 16, 18, 20], test_label))
