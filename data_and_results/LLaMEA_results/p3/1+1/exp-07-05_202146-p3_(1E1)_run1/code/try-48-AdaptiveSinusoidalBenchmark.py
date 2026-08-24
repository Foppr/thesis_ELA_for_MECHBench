import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multi-scale sinusoidal components with adaptive frequencies
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.3) + 0.5 * np.cos(i * 0.7)
            amp = 1.0 + 0.5 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional interaction with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                strength = 0.5 * (1.0 + np.sin(i * 0.2 + j * 0.3))
                result += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Adaptive ruggedness with position-dependent amplitude
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(x[i] * 0.5)
            result += amp * np.sin(3.0 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Non-separable high-order terms with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * x[i]**3 * x[j]**2
                
        # Asymmetric periodic components
        for i in range(self.dim):
            result += 0.1 * np.sin(2 * np.pi * x[i] * (1.0 + 0.1 * x[i])) * np.cos(2 * np.pi * x[i] * (1.0 - 0.1 * x[i]))
            
        # Global scaling factor that depends on the sum of coordinates
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x) * 0.1)
        result *= global_scale
        
        # Logarithmic barrier near boundaries
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.1 * np.log(1.0 + np.abs(x[i] - 5.0)) + 0.1 * np.log(1.0 + np.abs(x[i] + 5.0))
        result += penalty
        
        return result