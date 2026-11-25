import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number adjustment
        result = 0.02 * np.sum(x**2)
        
        # Nested exponential decay with trigonometric modulation at multiple scales
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.5 * x[i]**2) * np.sin(6 * x[i])**3
        
        # Multi-scale wave interference pattern with increased coupling and fractal-like behavior
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(8 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric gradient field with modified polynomial terms and fractal scaling
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**3.5 * np.exp(-0.15 * x[i])  # Increased coefficient and exponent
            else:
                result += 0.2 * x[i]**6 * np.exp(-0.4 * np.abs(x[i]))  # Reduced coefficient and exponent
        
        # High-frequency oscillatory component with spatially varying amplitude and self-similarity
        for i in range(self.dim):
            result += 3.0 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1 + 0.5 * np.sin(0.8 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with stronger exponential decay and fractal scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.exp(-0.7 * np.abs(x[i] - x[j])**1.3) * np.sin(3 * x[i]) * np.cos(4 * x[j])
        
        # Fractional power and logarithmic interaction terms with altered exponents and nested scaling
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1) * np.exp(-0.05 * np.abs(x[i]))
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result