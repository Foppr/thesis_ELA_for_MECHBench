import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sine-wave interaction terms with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 4 * (i + 1) * (j + 1)
                amp = 0.4 / (1 + abs(i - j)**0.5)
                result += amp * np.sin(freq * x[i]) * np.cos(freq * x[j])
        
        # Modified polynomial penalty terms with different exponents
        for i in range(self.dim):
            result += 0.15 * (x[i]**5 + 0.6 * x[i]**4 + 0.2 * x[i]**3 + 0.05 * x[i]**2)
            
        # Chaotic global minimum modulation using a modified logistic map
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= np.cos(2 * np.pi * (x[i] + 0.3) / 5.0)
        result += 0.12 * chaotic_factor
        
        # Enhanced multi-modal structure with sinusoidally shifted valleys
        for i in range(self.dim):
            shift = 1.5 * np.sin(0.7 * i)
            result += 0.18 * np.cos(3 * (x[i] - shift)) * np.exp(-0.08 * (x[i] - shift)**2)
            
        # Time-varying penalty component with dynamic scaling
        time_penalty = 0.08 * np.sum(np.abs(x)**1.5)
        result += time_penalty
        
        return result