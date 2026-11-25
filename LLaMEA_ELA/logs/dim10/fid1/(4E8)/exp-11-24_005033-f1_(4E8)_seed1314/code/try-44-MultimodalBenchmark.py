import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential barrier terms to penalize boundary violations
        result = np.sum(np.exp(2.0 * (1.0 - np.abs(x) / 5.0)) - 1.0)
        
        # High-frequency trigonometric interference pattern
        result += 3.0 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale adaptive conditioning with polynomial weights
        weights = np.arange(1, self.dim + 1)
        result += np.sum((x**2 + 0.1 * x**4) / (1.0 + weights * np.abs(x)))
        
        # Cross-dimensional coupling with chaotic sine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(5.0 * (x[i] + x[j])) * np.cos(7.0 * (x[i] - x[j]))
                result += 0.05 * coupling * (x[i]**2 + x[j]**2)
        
        # Add a global scaling factor to increase problem difficulty
        result *= (1.0 + 0.1 * np.sum(np.sin(0.5 * x) ** 2))
        
        return result