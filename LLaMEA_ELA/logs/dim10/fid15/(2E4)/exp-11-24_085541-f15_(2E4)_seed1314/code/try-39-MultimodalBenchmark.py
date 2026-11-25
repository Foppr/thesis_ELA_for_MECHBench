import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Enhanced chaotic oscillations with modified frequency and amplitude
        for i in range(self.dim):
            scale = 3 ** (i % 5)  # Different scale factors
            amp = 1.5 + 0.3 * np.sin(i)  # Dynamic amplitude modulation
            freq = 2.0 + 0.4 * np.cos(i)  # Dynamic frequency modulation
            
            # Combine multiple sine waves with different scales for chaotic behavior
            oscillation = 0.0
            for k in range(1, 5):
                oscillation += amp * np.sin(freq * scale * x[i] / (k + 0.5)) * np.cos(freq * scale * x[i] / (k + 1.5))
            
            result += oscillation
            
        # Asymmetric saddle points with modified exponential decay
        for i in range(self.dim):
            asym_term = 0.3 * x[i]**3 * np.exp(-0.15 * np.abs(x[i]))
            result += asym_term
            
        # Cross-dimension non-linear coupling with enhanced self-similarity
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(3 * x[i] * x[j]) * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                result += 0.2 * coupling * (1 + 0.15 * (i + j) + 0.05 * i * j)
                
        # Add dimensionality-dependent scaling with enhanced complexity
        result *= (1.0 + 0.07 * self.dim + 0.02 * np.sum(x**4) + 0.005 * np.sum(np.abs(x)**3))
        
        return result