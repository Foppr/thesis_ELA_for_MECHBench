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
            result += 0.9 * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
            result += 0.5 * np.sin(2 * freq * np.pi * x[i])**3
            result += 0.4 * np.cos(3 * freq * np.pi * x[i])**2
        
        # Polynomial penalty terms with varying degrees (slightly modified)
        for i in range(self.dim):
            result += 0.03 * x[i]**4 + 0.02 * x[i]**5 + 0.01 * x[i]**7  # Increased weights
        
        # Cross-dimensional cubic coupling with chaotic interaction (modified)
        for i in range(self.dim - 2):
            result += 0.08 * np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i] + x[i+1] + x[i+2])  # Increased weight
            result += 0.05 * (x[i]**3 + x[i+1]**3) * np.sin(0.4 * (x[i] - x[i+1])**3)  # Slightly modified
        
        # Adaptive scaling based on dimensionality and position (slightly altered)
        adaptive_factor = 1.0 + 0.3 * np.sum(np.abs(x)) + 0.08 * np.sum(x**2)  # Increased factors
        result *= adaptive_factor
        
        # Add a global exponential penalty to increase landscape complexity (modified)
        result += 0.15 * np.exp(0.15 * np.sum(np.abs(x)))  # Increased coefficient
        
        return result