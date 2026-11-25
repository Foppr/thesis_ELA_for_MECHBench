import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number adjustment
        result = 0.05 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * x[i]**2) * np.sin(3 * x[i])**2
        
        # Multi-scale wave interference pattern with increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 1.0 * np.exp(-dist) * np.sin(5 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.7 * x[i]**3 * np.exp(-0.15 * x[i])  # Increased coefficient and exponent
            else:
                result += 0.3 * x[i]**5 * np.exp(-0.25 * np.abs(x[i]))  # Reduced coefficient and exponent
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 1.8 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * (1 + 0.3 * np.sin(0.5 * x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.exp(-0.4 * np.abs(x[i] - x[j])) * np.sin(2 * x[i]) * np.cos(3 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.3 * np.abs(x[i])**1.5 * np.log(np.abs(x[i]) + 1)
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result