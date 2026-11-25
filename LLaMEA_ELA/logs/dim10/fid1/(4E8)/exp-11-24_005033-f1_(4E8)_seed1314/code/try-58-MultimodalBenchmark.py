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
        
        # Exponentially increasing sinusoidal components with chaotic modulation
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            result += 1.2 * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
            result += 0.8 * np.sin(2 * freq * np.pi * x[i])**3
            result += 0.6 * np.cos(3 * freq * np.pi * x[i])**2
            # Add chaotic modulation based on neighboring dimensions
            if i > 0:
                result += 0.3 * np.sin(freq * x[i-1] * x[i]) * np.cos(freq * x[i-1] + x[i])
        
        # Enhanced polynomial penalty terms with higher degrees and varying weights
        for i in range(self.dim):
            result += 0.04 * x[i]**4 + 0.03 * x[i]**5 + 0.02 * x[i]**6 + 0.01 * x[i]**8
        
        # Cross-dimensional coupling with chaotic interaction and dynamic scaling
        for i in range(self.dim - 3):
            result += 0.12 * np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i] + x[i+1] + x[i+2])
            result += 0.08 * (x[i]**3 + x[i+1]**3) * np.sin(0.5 * (x[i] - x[i+1])**3)
            # Add dynamic coupling strength based on position
            dynamic_factor = 1.0 + 0.2 * np.abs(x[i]) * np.abs(x[i+1])
            result += 0.05 * dynamic_factor * np.sin(0.3 * x[i] * x[i+2]) * np.cos(0.3 * x[i+1] * x[i+2])
        
        # Adaptive scaling based on dimensionality and position with enhanced complexity
        adaptive_factor = 1.0 + 0.4 * np.sum(np.abs(x)) + 0.12 * np.sum(x**2) + 0.05 * np.sum(np.abs(x)**3)
        result *= adaptive_factor
        
        # Add a global exponential penalty to increase landscape complexity
        result += 0.2 * np.exp(0.2 * np.sum(np.abs(x))) + 0.1 * np.exp(0.3 * np.sum(x**2))
        
        # Add a chaotic perturbation term for increased multimodality
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.05 * np.sin(7 * x[i]) * np.cos(5 * x[i])
        result += chaos_term * (1.0 + 0.1 * np.sum(x**2))
        
        return result