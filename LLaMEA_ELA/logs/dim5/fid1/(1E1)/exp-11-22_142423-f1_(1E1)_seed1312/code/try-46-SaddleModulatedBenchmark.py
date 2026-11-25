import numpy as np

class SaddleModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add periodic modulations with varying wavelengths and amplitudes
        for i in range(self.dim):
            f += 0.3 * np.sin(2 * np.pi * x[i] / 1.5) * np.cos(3 * np.pi * x[(i + 1) % self.dim] / 2.0)
            
        # Introduce saddle-point structure via hyperbolic tangent interactions
        for i in range(self.dim):
            f += 0.2 * np.tanh(x[i]) * np.sinh(x[(i + 2) % self.dim])
            
        # Asymmetric basin contributions using exponential and polynomial terms
        for i in range(self.dim):
            f += 0.15 * (np.exp(0.5 * x[i]) - 1) * (x[(i + 1) % self.dim]**2 + 0.1)
            
        # Cross-dimensional coupling with asymmetric weights
        for i in range(self.dim):
            f += 0.1 * x[i] * np.cos(4 * x[(i + 3) % self.dim]) * (x[(i + 1) % self.dim]**2 + 0.5)
            
        # Add multi-scale harmonic oscillations
        for i in range(self.dim):
            f += 0.25 * np.sin(5 * x[i] + 0.5) * np.cos(7 * x[(i + 2) % self.dim] - 1.0) * np.sin(3 * x[(i + 4) % self.dim])
            
        # Introduce irregular penalty terms with non-uniform exponents
        f += 0.1 * np.sum(np.abs(x)**1.5) + 0.08 * np.sum(x**4)
        
        # Add cubic cross-dimensional interactions with phase shifts
        for i in range(self.dim):
            f += 0.12 * x[i]**3 * np.cos(2 * x[(i + 1) % self.dim]) + 0.09 * x[i]**2 * np.sin(3 * x[(i + 2) % self.dim])
            
        # Final chaotic enhancement using sine products
        for i in range(self.dim):
            f += 0.05 * np.sin(11 * x[i]) * np.cos(9 * x[(i + 1) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim])
            
        return f