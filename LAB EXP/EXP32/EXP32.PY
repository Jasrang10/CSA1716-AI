import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)   # e.g. years of experience
y = np.array([30,35,41,45,52,56,61,66,72,75])        # e.g. salary (k)

model = LinearRegression().fit(X, y)
pred = model.predict(X)

print("Slope:", model.coef_[0], "Intercept:", model.intercept_)
print("MSE:", mean_squared_error(y, pred), "R2:", r2_score(y, pred))
print("Prediction for x=11:", model.predict([[11]])[0])

plt.scatter(X, y); plt.plot(X, pred, color='red')
plt.xlabel("X"); plt.ylabel("y"); plt.show()
