import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with increased condition number
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay with trigonometric modulation and higher frequency
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.4 * x[i]**2) * np.sin(6 * x[i])**3
        
        # Multi-scale wave interference pattern with increased coupling and phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(8 * (x[i] + x[j]) + i) * np.cos(4 * (x[i] - x[j]) + j)
        
        # Asymmetric gradient field with modified polynomial terms and fractional exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**3.5 * np.exp(-0.25 * x[i])  # Increased exponent and coefficient
            else:
                result += 0.2 * x[i]**4.2 * np.exp(-0.35 * np.abs(x[i]))  # Modified exponent and coefficient
        
        # High-frequency oscillatory component with spatially varying amplitude and phase
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.5 * np.sin(0.8 * x[i] + i))
        
        # Cross-dimensional coupling with stronger exponential decay and additional trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.0 * np.exp(-0.6 * np.abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(4 * x[j]) + \
                         0.5 * np.sin(2 * x[i] + x[j]) * np.cos(5 * x[i] - x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents and additional noise
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1) + \
                         0.3 * np.sin(0.5 * x[i]**2)
        
        # Add enhanced noise to prevent trivial solutions
        result += 0.03 * np.random.random()
        
        return result