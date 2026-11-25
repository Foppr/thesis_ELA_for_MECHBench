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
            f += 0.9 * np.sin(14 * x[i]) * np.cos(10 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim])
            
        # Increased irregular penalty terms with varied exponents
        f += 0.12 * np.sum(np.abs(x)**1.9) + 0.06 * np.sum(x**5) + 0.45 * np.sum(np.sin(1.0 * x)**2)
        
        # Cross-dimensional coupling with enhanced chaotic phase shifts and cubic terms
        for i in range(self.dim):
            f += 0.3 * np.cos(11 * x[i]) * np.sin(7 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.15 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Multiple shifted local minima with increased intensities and varied phases
        for i in range(self.dim):
            f += 0.4 * np.sin(9 * x[i] + 2.0) * np.cos(6 * x[(i + 1) % self.dim] - 0.8)
            
        # Irregular interaction terms between non-adjacent dimensions with altered frequencies
        for i in range(self.dim):
            f += 0.3 * np.sin(8 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions with modified coefficients
        for i in range(self.dim):
            f += 0.2 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.15 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms with more complex frequency combinations
        for i in range(self.dim):
            f += 0.07 * np.sin(17 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # New coupled sinusoidal terms with significantly altered phase shifts
        for i in range(self.dim):
            f += 0.18 * np.sin(12 * x[i] + 0.6) * np.cos(8 * x[(i + 2) % self.dim] - 1.5) * np.sin(4 * x[(i + 4) % self.dim] + 1.0)
            
        # Strengthened penalty for large values with higher-order terms
        f += 0.3 * np.sum(np.abs(x)**3.9)
        
        return f