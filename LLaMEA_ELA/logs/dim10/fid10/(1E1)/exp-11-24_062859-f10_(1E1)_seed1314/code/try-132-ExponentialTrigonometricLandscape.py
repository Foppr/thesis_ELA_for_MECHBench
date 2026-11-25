import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with severe conditioning
        result = 0.1 * np.sum(x**2)
        
        # Exponential decay with high-frequency trigonometric modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.5 * x[i]**2) * np.sin(8 * x[i])**3
        
        # Multi-scale wave interference pattern with strong coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(10 * (x[i] + x[j])) * np.cos(5 * (x[i] - x[j]))
        
        # Asymmetric gradient field with higher-order polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.5 * x[i]**4 * np.exp(-0.3 * x[i])  # Increased exponent and coefficient
            else:
                result += 0.2 * x[i]**7 * np.exp(-0.4 * np.abs(x[i]))  # Higher degree and modified decay
        
        # High-frequency oscillatory component with fractal-like amplitude modulation
        for i in range(self.dim):
            result += 3.0 * np.sin(25 * x[i]) * np.cos(12 * x[i]) * (1 + 0.6 * np.sin(0.8 * x[i]) * np.cos(0.4 * x[i]))
        
        # Cross-dimensional coupling with ultra-strong exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.2 * np.exp(-0.7 * np.abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(4 * x[j])
        
        # Fractional power and logarithmic interaction terms with extreme exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.8 * np.abs(x[i])**2.1 * np.log(np.abs(x[i]) + 1.5)
        
        # Add fractal-like noise to prevent trivial solutions
        result += 0.03 * np.random.random() * (1 + np.sin(100 * np.sum(x)))
        
        return result