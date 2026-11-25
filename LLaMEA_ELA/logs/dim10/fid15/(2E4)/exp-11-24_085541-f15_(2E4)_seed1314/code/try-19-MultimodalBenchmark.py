import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Enhanced periodic components with nested frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Varying frequencies with higher diversity
            amp = 1.5 + 0.5 * np.sin(i * 0.5)  # Sinusoidal amplitude modulation
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3)
            
        # Asymmetric saddle points with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.4 * (x[i]**4 - 0.6 * x[i]**3 + 0.1 * x[i]**2) * np.exp(-0.15 * x[i]**2)
            
        # Stronger non-linear cross-dimension interactions using coupled trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range but stronger interaction
                coupling = np.sin(0.5 * (x[i] - x[j])**2)
                result += 0.3 * coupling * np.cos(x[i] * x[j] / 2)
                
        # Add a global scaling factor based on dimensionality with logarithmic growth
        result *= (1 + 0.2 * np.log(1 + self.dim))
        
        return result