import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal modulation factors
        self.modulation_factors = np.sin(np.arange(dim) * np.pi / dim) * 0.5 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with sinusoidal modulation
        for i in range(self.dim):
            result += np.exp(-0.5 * (x[i] - self.modulation_factors[i])**2) * (1 + 0.3 * np.sin(5 * x[i]))
            
        # Sinusoidal coupling with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2 + 3 * self.modulation_factors[i]
                amp = 0.2 + 0.1 * self.modulation_factors[j]
                result += amp * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
                
        # Polynomial interaction terms with chaotic coefficients
        coeffs = np.random.rand(self.dim) * 2 + 1
        for i in range(self.dim):
            result += coeffs[i] * x[i]**3 + 0.5 * coeffs[i] * x[i]**2
            
        # Multi-scale sinusoidal modulation with exponential decay
        for i in range(self.dim):
            result += 0.1 * np.sin(10 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add a global shaping term with exponential scaling
        result += 0.05 * np.sum(np.exp(0.1 * np.abs(x)) - 1)
        
        # Add a chaotic noise component
        noise = 0.02 * np.sum(np.sin(x * 7) * np.cos(x * 3))
        result += noise
        
        return result