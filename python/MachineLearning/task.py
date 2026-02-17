import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionGD:
    def __init__(self, learning_rate=0.001, n_iters=100):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.theta_0 = 0.0  
        self.theta_1 = 0.0 
        self.sse_history = []

    def fit(self, X, y):
        n = len(y)
        
        for i in range(self.n_iters):
            # 1. التوقع الحالي (Linear Equation: y = mx + b)
            y_predicted = self.theta_0 + self.theta_1 * X
            
       
            error = y_predicted - y
            sse = np.sum(error ** 2)
            self.sse_history.append(sse)
            
            d_theta0 = (2/n) * np.sum(error)
            d_theta1 = (2/n) * np.sum(error * X)
            
    
            self.theta_0 -= self.lr * d_theta0
            self.theta_1 -= self.lr * d_theta1

    def predict(self, X):
        return self.theta_0 + self.theta_1 * X

    def plot_training(self, X, y):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
   
        ax1.plot(range(self.n_iters), self.sse_history, color='red')
        ax1.set_title('SSE over Iterations')
        ax1.set_xlabel('Iterations')
        ax1.set_ylabel('SSE')
        
        # رسم خط الانحدار مع البيانات
        ax2.scatter(X, y, color='blue', label='Data Points')
        ax2.plot(X, self.predict(X), color='black', label='Regression Line')
        ax2.set_title('Regression Line Fit')
        ax2.legend()
        
        plt.show()



X = np.array([50, 60, 70, 80, 90])
y = np.array([150, 180, 210, 240, 270])


model = LinearRegressionGD(learning_rate=0.0001, n_iters=100) 
model.fit(X, y)


print(f"Learned theta_0 (Intercept): {model.theta_0:.4f}")
print(f"Learned theta_1 (Slope): {model.theta_1:.4f}")

house_size = 70
predicted_price = model.predict(house_size)
print(f"Predicted price for {house_size}m²: {predicted_price:.2f} thousand")


model.plot_training(X, y)