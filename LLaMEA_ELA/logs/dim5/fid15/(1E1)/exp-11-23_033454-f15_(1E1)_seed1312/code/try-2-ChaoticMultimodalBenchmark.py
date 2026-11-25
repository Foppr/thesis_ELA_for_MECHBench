import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coefficients = np.random.uniform(-1, 1, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term
        radial_term = 0.01 * np.sum(x**2)
        
        # Sinusoidal oscillations creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(self.coefficients[i] * x[i] + self.phase_shifts[i]) * np.cos(0.5 * x[i])
        
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1 + np.abs(x[i]) + np.abs(x[j]))
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all terms with different weights
        return radial_term - 0.5 * sin_term + 0.3 * cross_term + 0.2 * chaotic_term