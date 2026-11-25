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
            f += 1.2 * np.sin(15 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim])
            
        # Add irregular penalty terms with non-uniform exponents
        f += 0.15 * np.sum(np.abs(x)**2.1) + 0.08 * np.sum(x**6) + 0.5 * np.sum(np.sin(1.1 * x)**2)
        
        # Add cross-dimensional coupling with chaotic phase shifts and cubic terms
        for i in range(self.dim):
            f += 0.35 * np.cos(12 * x[i]) * np.sin(8 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.18 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities
        for i in range(self.dim):
            f += 0.5 * np.sin(10 * x[i] + 2.1) * np.cos(7 * x[(i + 1) % self.dim] - 0.8)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.35 * np.sin(9 * x[i]) * np.sin(6 * x[(i + 2) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.25 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.18 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms with modified frequencies
        for i in range(self.dim):
            f += 0.09 * np.sin(18 * x[i]) * np.cos(10 * x[(i + 1) % self.dim]) * np.sin(7 * x[(i + 3) % self.dim]) * np.cos(9 * x[(i + 4) % self.dim])
            
        # New coupled sinusoidal terms with altered phase shifts
        for i in range(self.dim):
            f += 0.2 * np.sin(13 * x[i] + 0.7) * np.cos(9 * x[(i + 2) % self.dim] - 1.5) * np.sin(4 * x[(i + 4) % self.dim] + 1.1)
            
        # Increased penalty for large values
        f += 0.35 * np.sum(np.abs(x)**4.2)
        
        # Add dense local minima landscape with trigonometric chaos
        for i in range(self.dim):
            f += 0.28 * np.sin(14 * x[i]) * np.cos(12 * x[(i + 1) % self.dim]) * np.sin(10 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Add polynomial chaos with fractional exponents
        for i in range(self.dim):
            f += 0.12 * (x[i]**2.5 * x[(i + 2) % self.dim]**1.8 + x[i]**1.7 * x[(i + 3) % self.dim]**2.3)
            
        # Add hyperchaotic interaction terms
        for i in range(self.dim):
            f += 0.16 * np.sin(20 * x[i]) * np.cos(15 * x[(i + 1) % self.dim]) * np.sin(12 * x[(i + 2) % self.dim]) * np.cos(9 * x[(i + 3) % self.dim]) * np.sin(6 * x[(i + 4) % self.dim])
            
        return f