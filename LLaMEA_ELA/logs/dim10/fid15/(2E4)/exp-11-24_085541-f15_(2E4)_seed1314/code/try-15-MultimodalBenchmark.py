import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Add periodic components with varying wavelengths and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 3)  # Varying frequencies
            amp = 1.0 + 0.5 * (i % 2)  # Alternating amplitudes
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
            
        # Asymmetric saddle points with polynomial terms
        for i in range(self.dim):
            result += 0.3 * (x[i]**3 - 0.5 * x[i]**2) * np.exp(-0.1 * x[i]**2)
            
        # Non-linear cross-dimension interactions using exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.exp(-0.5 * (x[i] - x[j])**2)
                result += 0.2 * coupling * np.sin(x[i] * x[j])
                
        # Add a global scaling factor based on dimensionality
        result *= (1 + 0.1 * self.dim)
        
        return result