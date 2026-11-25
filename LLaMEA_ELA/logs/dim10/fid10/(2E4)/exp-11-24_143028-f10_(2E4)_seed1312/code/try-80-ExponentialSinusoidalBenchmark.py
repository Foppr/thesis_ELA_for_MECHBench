import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with conditioning
        result = 0.1 * np.sum(x**2)
        
        # Exponentially decaying sinusoidal waves with varying frequencies
        for i in range(self.dim):
            freq = 2 * (i + 1) * np.exp(-0.1 * np.abs(x[i]))
            result += np.exp(-0.5 * np.abs(x[i])) * np.sin(freq * x[i]) * np.cos(3 * x[i])
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.2 * (np.abs(x[i]) + np.abs(x[j])))
                result += coupling * np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.tan(0.5 * (x[i] + x[j]))
        
        # Multi-modal structure with adaptive valley depths
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Fractal-like self-similarity with recursive scaling
        for i in range(self.dim):
            result += 0.3 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(9 * x[i]**3) * (1 + 0.2 * np.abs(x[i]))
        
        # Boundary-sensitive penalty with exponential scaling
        boundary_penalty = 0
        for i in range(self.dim):
            boundary_penalty += 2.0 * np.exp(np.abs(x[i]) - 5.0) * (np.abs(x[i]) > 5.0)
        result += boundary_penalty
        
        # Cubic nonlinearity to increase condition number
        for i in range(self.dim):
            result += 0.15 * x[i]**3
        
        return result