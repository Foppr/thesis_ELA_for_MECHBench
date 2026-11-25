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
            result += 2.0 * np.exp(-0.3 * x[i]**2) * np.sin(4 * x[i])**2
        
        # Multi-scale wave interference pattern with increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced interaction range
                dist = np.abs(x[i] - x[j])
                result += 1.5 * np.exp(-dist) * np.sin(6 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.9 * x[i]**3 * np.exp(-0.2 * x[i])  # Increased coefficient and exponent
            else:
                result += 0.15 * x[i]**5 * np.exp(-0.3 * np.abs(x[i]))  # Reduced coefficient and exponent
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 2.2 * np.sin(17 * x[i]) * np.cos(8 * x[i]) * (1 + 0.4 * np.sin(0.6 * x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay and memory effect
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.exp(-0.5 * np.abs(x[i] - x[j])) * np.sin(2.5 * x[i]) * np.cos(3.5 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.45 * np.abs(x[i])**1.7 * np.log(np.abs(x[i]) + 1)
        
        # Add fractional chaos component
        for i in range(self.dim):
            result += 0.3 * np.sin(23 * x[i]) * np.cos(11 * x[i]) * np.sin(0.5 * x[i]**2) * (1 + 0.3 * np.random.random())
        
        # Memory-dependent exponential coupling with time-delayed interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.exp(-0.7 * np.abs(x[i] - x[j]) * (1 + 0.2 * np.sin(0.3 * x[i]))) * np.cos(4 * x[i]) * np.sin(5 * x[j])
        
        # Enhanced asymmetry with cubic and quintic fractional terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.7 * x[i]**3.5 * np.exp(-0.15 * x[i]) 
            else:
                result += 0.2 * x[i]**4.2 * np.exp(-0.25 * np.abs(x[i]))
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result