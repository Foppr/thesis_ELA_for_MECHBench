import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function
        result = 0.1 * np.sum(x**2)
        
        # Add exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * x[i]**2) * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Add asymmetric gradient components
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.8 * np.sin(x[i]**1.5) * np.exp(-0.1 * x[i])
            else:
                result += 0.6 * np.cos(x[i]**1.3) * np.exp(-0.2 * np.abs(x[i]))
                
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.5 * np.sin(x[i] * x[j]) * np.exp(-0.3 * dist) * (1 + 0.2 * np.sin(x[i] + x[j]))
                
        # Add polynomial interaction with fractional exponents
        for i in range(self.dim):
            result += 0.3 * (x[i]**2.5) * np.cos(4 * x[i]) + 0.2 * (x[i]**1.7) * np.sin(3 * x[i])
            
        # Add a non-smooth component with step-like behavior
        for i in range(self.dim):
            result += 0.4 * np.abs(x[i])**1.3 + 0.15 * np.floor(np.abs(x[i])) * np.cos(x[i])
            
        # Add a high-frequency oscillatory component
        for i in range(self.dim):
            result += 0.6 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result