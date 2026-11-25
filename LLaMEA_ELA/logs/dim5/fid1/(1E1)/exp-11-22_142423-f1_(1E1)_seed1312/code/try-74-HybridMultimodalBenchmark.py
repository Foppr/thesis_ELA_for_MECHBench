import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical base term
        f = np.sum(x**2)
        
        # Sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            
        # Exponential penalty terms with asymmetric exponents
        f += 0.3 * np.sum(np.exp(0.5 * np.abs(x)) - 1) + 0.2 * np.sum(np.exp(-0.3 * x**2) - 1)
        
        # Cross-dimensional interactions with exponential decay
        for i in range(self.dim):
            f += 0.4 * np.exp(-0.1 * (x[i] - x[(i + 2) % self.dim])**2) * np.sin(5 * x[i])
            
        # Asymmetric local minima with different intensities
        for i in range(self.dim):
            f += 0.25 * (np.abs(x[i]) ** 1.5) * np.cos(4 * x[(i + 1) % self.dim])
            
        # Higher-order polynomial interactions
        for i in range(self.dim):
            f += 0.15 * x[i]**4 * x[(i + 1) % self.dim]**2
            
        # Chaotic oscillations with varying amplitudes
        for i in range(self.dim):
            f += 0.3 * np.sin(7 * x[i]) * np.cos(9 * x[(i + 3) % self.dim]) * np.sin(5 * x[(i + 4) % self.dim])
            
        # Asymmetric penalty for large values
        f += 0.2 * np.sum(np.abs(x)**3.2)
        
        return f