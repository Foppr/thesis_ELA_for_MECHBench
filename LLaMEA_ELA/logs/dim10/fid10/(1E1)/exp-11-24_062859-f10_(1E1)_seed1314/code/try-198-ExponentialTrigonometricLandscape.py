import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number adjustment
        result = 0.02 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation - increased frequency
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(6 * x[i])**2
        
        # Multi-scale wave interference pattern with increased coupling and higher frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist) * np.sin(8 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms - more complex
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**3 * np.exp(-0.15 * x[i])  # Increased coefficient and exponent
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.4 * np.abs(x[i]))  # Higher exponent and modified coefficient
        
        # High-frequency oscillatory component with spatially varying amplitude - more complex
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.6 * np.sin(0.8 * x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay and higher frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.0 * np.exp(-0.7 * np.abs(x[i] - x[j])) * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents - more complex
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1)
        
        # Additional noise component with higher variance
        result += 0.03 * np.random.random()
        
        return result