import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with increased condition number
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay with enhanced trigonometric modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(5 * x[i])**3
        
        # Multi-scale wave interference pattern with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(8 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with stronger polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**4 * np.exp(-0.25 * x[i])  # Increased exponent and coefficient
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.35 * np.abs(x[i]))  # Increased exponent and reduced coefficient
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.5 * np.sin(0.7 * x[i]))
        
        # Cross-dimensional coupling with even stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.0 * np.exp(-0.7 * np.abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(4 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1.5)
        
        # Add stronger noise to prevent trivial solutions
        result += 0.03 * np.random.random()
        
        return result