import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal interactions with modified frequencies
        for i in range(self.dim):
            f += 1.2 * np.sin(15 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 2) % self.dim])
            
        # Modified penalty terms with different exponents
        f += 0.15 * np.sum(np.abs(x)**2.1) + 0.08 * np.sum(x**4) + 0.3 * np.sum(np.sin(1.1 * x)**2)
        
        # Cross-dimensional coupling with altered phase shifts and mixed terms
        for i in range(self.dim):
            f += 0.3 * np.cos(12 * x[i]) * np.sin(8 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.15 * x[i]**2 * x[(i + 1) % self.dim]
            
        # Additional shifted local minima with varying intensities and phase changes
        for i in range(self.dim):
            f += 0.4 * np.sin(9 * x[i] + 2.1) * np.cos(6 * x[(i + 1) % self.dim] - 0.8)
            
        # Non-adjacent dimension interactions with different frequencies
        for i in range(self.dim):
            f += 0.3 * np.sin(8 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions with different coefficients
        for i in range(self.dim):
            f += 0.2 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.15 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Higher-order chaotic terms with new frequency combinations
        for i in range(self.dim):
            f += 0.08 * np.sin(18 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # New coupled sinusoidal terms with additional phase shifts
        for i in range(self.dim):
            f += 0.18 * np.sin(13 * x[i] + 0.7) * np.cos(9 * x[(i + 2) % self.dim] - 1.5) * np.sin(4 * x[(i + 4) % self.dim] + 1.1)
            
        # Increased penalty for large values with modified exponents
        f += 0.3 * np.sum(np.abs(x)**4.2)
        
        return f