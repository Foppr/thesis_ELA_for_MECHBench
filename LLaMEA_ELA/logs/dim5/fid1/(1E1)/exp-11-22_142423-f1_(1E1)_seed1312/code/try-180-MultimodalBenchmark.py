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
            f += 0.8 * np.sin(13 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Add irregular penalty terms with non-uniform exponents
        f += 0.1 * np.sum(np.abs(x)**1.8) + 0.05 * np.sum(x**5) + 0.4 * np.sum(np.sin(0.9 * x)**2)
        
        # Add cross-dimensional coupling with chaotic phase shifts and cubic terms
        for i in range(self.dim):
            f += 0.25 * np.cos(10 * x[i]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(3 * x[(i + 4) % self.dim]) + 0.12 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities
        for i in range(self.dim):
            f += 0.35 * np.sin(8 * x[i] + 1.7) * np.cos(5 * x[(i + 1) % self.dim] - 0.6)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.25 * np.sin(7 * x[i]) * np.sin(4 * x[(i + 2) % self.dim]) * np.cos(6 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.18 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.12 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms with modified frequencies
        for i in range(self.dim):
            f += 0.06 * np.sin(16 * x[i]) * np.cos(8 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 3) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # New coupled sinusoidal terms with altered phase shifts
        for i in range(self.dim):
            f += 0.15 * np.sin(11 * x[i] + 0.5) * np.cos(7 * x[(i + 2) % self.dim] - 1.2) * np.sin(3 * x[(i + 4) % self.dim] + 0.8)
            
        # Increased penalty for large values
        f += 0.25 * np.sum(np.abs(x)**3.7)
        
        # Add new set of coupled sinusoidal functions with altered frequencies and phase shifts
        for i in range(self.dim):
            f += 0.18 * np.cos(14 * x[i] + 0.3) * np.sin(5 * x[(i + 2) % self.dim] - 0.9) * np.cos(8 * x[(i + 3) % self.dim] + 0.4)
            
        return f