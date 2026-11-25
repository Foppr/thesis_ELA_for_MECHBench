import numpy as np

class SaddlePolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.1 * np.sum(x**2)
        
        # Polynomial chaos expansion with mixed terms
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2.0 * x[i]**2
        
        # Radial symmetry component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 3.0 * np.exp(-0.1 * r**2) * np.cos(2 * r)
        
        # Saddle-point structure with cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Multi-scale harmonic components with varying amplitudes
        for i in range(self.dim):
            result += 1.2 * np.sin(3 * x[i]) * np.cos(5 * x[i]) * (1 + 0.3 * np.sin(0.7 * x[i]))
        
        # Asymmetric polynomial with exponential decay
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.8 * x[i]**3.5 * np.exp(-0.2 * x[i])
            else:
                result += 0.2 * x[i]**4.5 * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.4 * np.sin(3 * dist) * np.cos(2 * (x[i] + x[j]))
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result