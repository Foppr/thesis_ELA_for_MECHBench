import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with severe conditioning
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(5 * x[i])**3
        
        # Multi-scale wave interference pattern with increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist) * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with stronger polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.5 * x[i]**4 * np.exp(-0.3 * x[i])  # Increased exponent and coefficient
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.4 * np.abs(x[i]))  # Higher degree and reduced coefficient
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.5 * np.sin(0.7 * x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.exp(-0.6 * np.abs(x[i] - x[j])) * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1)
        
        # Add stronger noise to prevent trivial solutions
        result += 0.03 * np.random.random()
        
        return result