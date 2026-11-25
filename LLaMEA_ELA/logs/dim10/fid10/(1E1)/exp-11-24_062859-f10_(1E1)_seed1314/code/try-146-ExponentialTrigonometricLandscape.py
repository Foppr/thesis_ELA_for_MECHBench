import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number adjustment
        result = 0.03 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(5 * x[i])**2
        
        # Multi-scale wave interference pattern with increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist) * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**3 * np.exp(-0.15 * x[i])  # Increased coefficient and exponent
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.25 * np.abs(x[i]))  # Higher exponent and modified coefficient
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 3.0 * np.sin(19 * x[i]) * np.cos(9 * x[i]) * (1 + 0.5 * np.sin(0.7 * x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.exp(-0.6 * np.abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(4 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.5 * np.abs(x[i])**1.9 * np.log(np.abs(x[i]) + 1)
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result