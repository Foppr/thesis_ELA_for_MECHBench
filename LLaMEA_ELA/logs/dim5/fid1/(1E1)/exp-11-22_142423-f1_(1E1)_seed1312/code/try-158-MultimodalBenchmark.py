import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal interactions with higher frequencies and amplitudes
        for i in range(self.dim):
            f += 1.2 * np.sin(20 * x[i]) * np.cos(15 * x[(i + 1) % self.dim]) * np.sin(8 * x[(i + 2) % self.dim])
            
        # Add irregular penalty terms with non-uniform exponents and higher order terms
        f += 0.15 * np.sum(np.abs(x)**2.3) + 0.08 * np.sum(x**6) + 0.5 * np.sum(np.sin(1.2 * x)**3)
        
        # Add cross-dimensional coupling with chaotic phase shifts, cubic terms and higher order interactions
        for i in range(self.dim):
            f += 0.35 * np.cos(15 * x[i]) * np.sin(10 * x[(i + 3) % self.dim]) * np.cos(5 * x[(i + 4) % self.dim]) + 0.18 * x[i]**3 * x[(i + 1) % self.dim] + 0.12 * x[i]**4 * x[(i + 2) % self.dim]
            
        # Add multiple shifted local minima with varying intensities and higher frequency components
        for i in range(self.dim):
            f += 0.5 * np.sin(12 * x[i] + 2.1) * np.cos(8 * x[(i + 1) % self.dim] - 0.9) + 0.3 * np.sin(15 * x[i] + 1.4) * np.cos(6 * x[(i + 2) % self.dim] - 1.1)
            
        # Add irregular interaction terms between non-adjacent dimensions with higher frequencies
        for i in range(self.dim):
            f += 0.35 * np.sin(10 * x[i]) * np.sin(7 * x[(i + 2) % self.dim]) * np.cos(9 * x[(i + 4) % self.dim]) + 0.25 * np.cos(11 * x[i]) * np.sin(5 * x[(i + 3) % self.dim]) * np.cos(8 * x[(i + 5) % self.dim])
            
        # Enhanced cubic cross-dimensional interactions with higher order terms
        for i in range(self.dim):
            f += 0.25 * x[i]**3 * x[(i + 2) % self.dim]**3 + 0.18 * x[i]**2 * x[(i + 3) % self.dim]**4 + 0.15 * x[i]**4 * x[(i + 1) % self.dim]**2
            
        # Additional chaotic higher-order terms with modified frequencies and complex phase shifts
        for i in range(self.dim):
            f += 0.12 * np.sin(25 * x[i]) * np.cos(12 * x[(i + 1) % self.dim]) * np.sin(9 * x[(i + 3) % self.dim]) * np.cos(14 * x[(i + 4) % self.dim]) + 0.08 * np.sin(18 * x[i]) * np.cos(16 * x[(i + 2) % self.dim]) * np.sin(13 * x[(i + 5) % self.dim])
            
        # New coupled sinusoidal terms with altered phase shifts and complex interactions
        for i in range(self.dim):
            f += 0.2 * np.sin(18 * x[i] + 0.7) * np.cos(13 * x[(i + 2) % self.dim] - 1.5) * np.sin(6 * x[(i + 4) % self.dim] + 1.1) + 0.15 * np.cos(19 * x[i] + 0.3) * np.sin(14 * x[(i + 3) % self.dim] - 0.8)
            
        # Increased penalty for large values with higher order exponents
        f += 0.35 * np.sum(np.abs(x)**4.2)
        
        # Add a complex hyperbolic term to increase problem difficulty
        for i in range(self.dim):
            f += 0.1 * np.sinh(2 * x[i]) * np.cosh(1.5 * x[(i + 1) % self.dim])
            
        return f