import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Multi-scale fractal-like oscillations with varying amplitudes and frequencies
        for i in range(self.dim):
            scale = 2 ** (i % 4)  # Scale factors
            amp = 1.0 + 0.2 * (i % 3)  # Amplitude modulation
            freq = 1.0 + 0.5 * (i % 5)  # Frequency modulation
            
            # Combine multiple sine waves with different scales for fractal behavior
            oscillation = 0.0
            for k in range(1, 4):
                oscillation += amp * np.sin(freq * scale * x[i] / k) * np.cos(freq * scale * x[i] / (k + 1))
            
            result += oscillation
            
        # Asymmetric saddle points with exponential decay
        for i in range(self.dim):
            asym_term = 0.2 * x[i]**3 * np.exp(-0.1 * np.abs(x[i]))
            result += asym_term
            
        # Cross-dimension non-linear coupling with self-similar structure
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.sin(2 * x[i] * x[j]) * np.exp(-0.5 * (x[i]**2 + x[j]**2))
                result += 0.15 * coupling * (1 + 0.1 * (i + j))
                
        # Add dimensionality-dependent scaling to increase complexity
        result *= (1.0 + 0.05 * self.dim + 0.01 * np.sum(x**4))
        
        return result