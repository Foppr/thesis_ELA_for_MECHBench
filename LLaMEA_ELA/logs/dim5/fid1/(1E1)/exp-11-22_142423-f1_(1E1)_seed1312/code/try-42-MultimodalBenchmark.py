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
            f += 1.2 * np.sin(17 * x[i]) * np.cos(11 * x[(i + 1) % self.dim]) * np.sin(5 * x[(i + 2) % self.dim])
            
        # Add irregular penalty terms with non-uniform exponents
        f += 0.15 * np.sum(np.abs(x)**2.1) + 0.08 * np.sum(x**6) + 0.5 * np.sum(np.sin(1.1 * x)**2)
        
        # Add cross-dimensional coupling with chaotic phase shifts and cubic terms
        for i in range(self.dim):
            f += 0.3 * np.cos(14 * x[i]) * np.sin(8 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.15 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities
        for i in range(self.dim):
            f += 0.4 * np.sin(10 * x[i] + 2.1) * np.cos(7 * x[(i + 1) % self.dim] - 0.8)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.3 * np.sin(9 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(7 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.22 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.15 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms
        for i in range(self.dim):
            f += 0.08 * np.sin(19 * x[i]) * np.cos(10 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Increased penalty for large values
        f += 0.3 * np.sum(np.abs(x)**4.1)
        
        # Add a new set of high-frequency oscillations to increase complexity
        for i in range(self.dim):
            f += 0.25 * np.sin(25 * x[i]) * np.cos(15 * x[(i + 1) % self.dim]) * np.sin(12 * x[(i + 2) % self.dim])
            
        # Add a new set of quartic interaction terms
        for i in range(self.dim):
            f += 0.1 * x[i]**4 * x[(i + 3) % self.dim] + 0.08 * x[i]**2 * x[(i + 4) % self.dim]**2
            
        return f