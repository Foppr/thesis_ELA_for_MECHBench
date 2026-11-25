import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with increased condition number
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation and altered frequencies
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(5 * x[i])**3
        
        # Multi-scale wave interference pattern with increased coupling and new interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms and new exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**4 * np.exp(-0.25 * x[i])  # Increased exponent
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.35 * np.abs(x[i]))  # Higher order polynomial
        
        # High-frequency oscillatory component with spatially varying amplitude and new modulation
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.5 * np.sin(0.7 * x[i])**2)
        
        # Cross-dimensional coupling with stronger exponential decay and additional harmonic
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.exp(-0.6 * np.abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(4 * x[j]) + \
                          0.3 * np.exp(-0.4 * np.abs(x[i] + x[j])) * np.cos(5 * x[i]) * np.sin(2 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents and new components
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1) + \
                          0.15 * np.abs(x[i])**1.3 * np.sin(3 * x[i])
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result