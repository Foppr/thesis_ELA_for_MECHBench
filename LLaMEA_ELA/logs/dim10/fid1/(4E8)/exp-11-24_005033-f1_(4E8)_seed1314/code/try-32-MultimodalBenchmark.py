import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Base quadratic term with adaptive conditioning
        for i in range(self.dim):
            result += 0.05 * x[i]**2
        
        # Exponentially increasing sinusoidal components
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            result += 0.8 * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
            result += 0.4 * np.sin(2 * freq * np.pi * x[i])**3
            result += 0.3 * np.cos(3 * freq * np.pi * x[i])**2
        
        # Polynomial penalty terms with varying degrees
        for i in range(self.dim):
            result += 0.02 * x[i]**4 + 0.01 * x[i]**5 + 0.005 * x[i]**7
        
        # Cross-dimensional cubic coupling with chaotic interaction
        for i in range(self.dim - 2):
            result += 0.05 * np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i] + x[i+1] + x[i+2])
            result += 0.03 * (x[i]**3 + x[i+1]**3) * np.sin(0.3 * (x[i] - x[i+1])**3)
        
        # Adaptive scaling based on dimensionality and position
        adaptive_factor = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(x**2)
        result *= adaptive_factor
        
        # Add a global exponential penalty to increase landscape complexity
        result += 0.1 * np.exp(0.1 * np.sum(np.abs(x)))
        
        # Add chaotic sine-cosine interactions for increased multimodality
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    result += 0.02 * np.sin(5 * x[i] * x[j]) * np.cos(5 * x[i] + x[j])
        
        # Add a logarithmic barrier term to create more challenging terrain
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += 0.01 / (1e-10 + np.abs(x[i]))
        result += log_barrier
        
        return result