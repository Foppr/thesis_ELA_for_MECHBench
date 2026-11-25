import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic frequencies and weights
        self.frequencies = np.arange(1, dim + 1)
        self.weights = np.exp(-np.arange(dim) * 0.3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with mixed monomials
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += self.weights[i] * (x[i]**4 + x[i]**3 - 2*x[i]**2 + x[i])
        
        # Spherical harmonic decomposition with angular coupling
        spherical_harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                angle = np.arctan2(x[j], x[i])
                spherical_harmonic += np.sin(self.frequencies[i] * angle) * np.cos(self.frequencies[j] * angle) * np.exp(-dist/5.0)
        
        # Adaptive gradient modulation with dynamic scaling
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += (x[i]**2 + 1.0) * np.sin(x[i]) * np.cos(0.5 * x[i])
        
        # Cross-dimensional polynomial interactions
        cross_poly = 0.0
        for i in range(self.dim - 1):
            cross_poly += (x[i] * x[i+1])**2 + (x[i] + x[i+1])**3
        
        # Multi-scale oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(2.0 * self.frequencies[i] * x[i]) * np.cos(3.0 * self.frequencies[i] * x[i])
        
        # Fractal-like recursive interaction
        fractal = 0.0
        if self.dim >= 3:
            for i in range(self.dim - 2):
                fractal += np.sin(x[i] + x[i+1] + x[i+2]) * np.cos(x[i] * x[i+1] * x[i+2])
        
        # Dimensionality-adaptive scaling factor
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combined function with weighted components
        return scale_factor * (0.7 * poly_chaos + 0.6 * spherical_harmonic + 
                              0.5 * grad_mod + 0.4 * cross_poly + 
                              0.3 * oscillatory + 0.2 * fractal)