import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add periodic sine-wave interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.7 * np.sin(11 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim])
            
        # Add asymmetric penalty terms with non-uniform exponents
        f += 0.15 * np.sum(np.abs(x)**2.3) + 0.08 * np.sum(x**4) + 0.3 * np.sum(np.sin(0.8 * x)**3)
        
        # Add cross-dimensional coupling with asymmetric phase shifts and quartic terms
        for i in range(self.dim):
            f += 0.2 * np.cos(9 * x[i]) * np.sin(5 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.1 * x[i]**4 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities and non-uniform phases
        for i in range(self.dim):
            f += 0.3 * np.sin(9 * x[i] + 1.5) * np.cos(6 * x[(i + 1) % self.dim] - 0.8)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.2 * np.sin(6 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # Enhanced quartic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.15 * x[i]**4 * x[(i + 2) % self.dim]**2 + 0.1 * x[i]**2 * x[(i + 3) % self.dim]**4
            
        # Additional higher-order chaotic terms
        for i in range(self.dim):
            f += 0.08 * np.sin(14 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Increased penalty for large values with asymmetric scaling
        f += 0.2 * np.sum(np.abs(x)**3.5)
        
        return f