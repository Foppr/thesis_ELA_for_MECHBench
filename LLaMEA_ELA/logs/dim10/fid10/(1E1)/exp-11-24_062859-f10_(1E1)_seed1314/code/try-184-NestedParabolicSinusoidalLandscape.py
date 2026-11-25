import numpy as np

class NestedParabolicSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number adjustment
        result = 0.1 * np.sum(x**2)
        
        # Nested parabolic wells with varying depths
        for i in range(self.dim):
            result += 3.0 * (x[i]**2 + 0.5 * x[i]**4 + 0.1 * x[i]**6)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.0 * np.sin(3 * x[i]) * np.cos(5 * x[i]) * (1 + 0.3 * np.sin(0.7 * x[i]))
        
        # Cross-dimensional interference with nested structure
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 1.2 * np.sin(2 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric polynomial terms with varying exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.8 * x[i]**3.5 + 0.2 * x[i]**5.5
            else:
                result += 0.3 * x[i]**4.2 + 0.1 * x[i]**6.8
        
        # Multi-scale oscillatory component with decreasing amplitude
        for i in range(self.dim):
            result += 1.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * np.abs(x[i]))
        
        # Fractional power and logarithmic interaction terms
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.5 * np.abs(x[i])**1.8 * np.log(np.abs(x[i]) + 2)
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result