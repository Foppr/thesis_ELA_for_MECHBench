import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal chaotic component with varying frequencies
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) / self.dim
            result += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Polynomial potential component with alternating signs
        for i in range(self.dim):
            poly = (-1)**i * (x[i]**4 - 2*x[i]**2 + 1)
            result += 0.5 * poly
        
        # Cross-dimensional coupling creating complex interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.3 * coupling
        
        # Logistic map inspired chaotic behavior
        for i in range(self.dim):
            logistic = 4 * x[i] * (1 - x[i])
            result += 0.2 * np.sin(logistic)
        
        # Multi-scale harmonic component
        for i in range(self.dim):
            scale = 1 + 0.5 * np.sin(3 * x[i])
            result += 0.4 * scale * np.cos(5 * x[i])
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result