import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add chaotic sinusoidal interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.7 * np.sin(14 * x[i]) * np.cos(8 * x[(i + 1) % self.dim]) * np.sin(3 * x[(i + 2) % self.dim])
            
        # Add irregular penalty terms with non-uniform exponents
        f += 0.12 * np.sum(np.abs(x)**1.9) + 0.04 * np.sum(x**5) + 0.35 * np.sum(np.sin(0.8 * x)**2)
        
        # Add cross-dimensional coupling with chaotic phase shifts and cubic terms
        for i in range(self.dim):
            f += 0.23 * np.cos(9 * x[i]) * np.sin(5 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.11 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities
        for i in range(self.dim):
            f += 0.32 * np.sin(7 * x[i] + 1.8) * np.cos(4 * x[(i + 1) % self.dim] - 0.5)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.23 * np.sin(6 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.19 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.11 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms
        for i in range(self.dim):
            f += 0.05 * np.sin(14 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Increased penalty for large values
        f += 0.23 * np.sum(np.abs(x)**3.6)
        
        return f