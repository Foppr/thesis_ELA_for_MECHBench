import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sine-wave interaction terms with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 3 * (i + 1) * (j + 1)
                amp = 0.3 / (1 + abs(i - j))
                result += amp * np.sin(freq * x[i]) * np.cos(freq * x[j])
        
        # Polynomial penalty terms with increasing degree
        for i in range(self.dim):
            result += 0.2 * (x[i]**4 + 0.5 * x[i]**3 + 0.1 * x[i]**2)
            
        # Chaotic global minimum modulation using a logistic map-like function
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= np.sin(2 * np.pi * (x[i] + 0.5) / 5.0)
        result += 0.1 * chaotic_factor
        
        # Multi-modal structure with shifted valleys
        for i in range(self.dim):
            shift = 2.0 * np.sin(0.5 * i)
            result += 0.1 * np.cos(4 * (x[i] - shift)) * np.exp(-0.1 * (x[i] - shift)**2)
            
        # Time-varying penalty component (static in this implementation)
        time_penalty = 0.05 * np.sum(np.abs(x))
        result += time_penalty
        
        return result