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
            f += 0.35 * np.cos(14 * x[i]) * np.sin(8 * x[(i + 3) % self.dim]) * np.cos(4 * x[(i + 4) % self.dim]) + 0.18 * x[i]**3 * x[(i + 1) % self.dim]
            
        # Add multiple shifted local minima with varying intensities
        for i in range(self.dim):
            f += 0.5 * np.sin(10 * x[i] + 2.1) * np.cos(7 * x[(i + 1) % self.dim] - 0.8)
            
        # Add irregular interaction terms between non-adjacent dimensions
        for i in range(self.dim):
            f += 0.35 * np.sin(9 * x[i]) * np.sin(5 * x[(i + 2) % self.dim]) * np.cos(8 * x[(i + 4) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions
        for i in range(self.dim):
            f += 0.25 * x[i]**3 * x[(i + 2) % self.dim]**2 + 0.18 * x[i]**2 * x[(i + 3) % self.dim]**3
            
        # Additional chaotic higher-order terms
        for i in range(self.dim):
            f += 0.09 * np.sin(19 * x[i]) * np.cos(10 * x[(i + 1) % self.dim]) * np.sin(7 * x[(i + 3) % self.dim]) * np.cos(9 * x[(i + 4) % self.dim])
            
        # Increased penalty for large values
        f += 0.35 * np.sum(np.abs(x)**4.1)
        
        # Add a new layer of complex interaction terms
        for i in range(self.dim):
            f += 0.2 * np.sin(12 * x[i]) * np.cos(6 * x[(i + 2) % self.dim]) * np.sin(3 * x[(i + 3) % self.dim]) * np.cos(5 * x[(i + 5) % self.dim])
            
        # Add hyperbolic tangent interactions for additional nonlinearity
        for i in range(self.dim):
            f += 0.12 * np.tanh(2 * x[i]) * np.sin(9 * x[(i + 1) % self.dim]) * np.cos(4 * x[(i + 3) % self.dim])
            
        return f