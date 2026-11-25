import numpy as np

class CompositeSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial component with multiple sinusoidal modulations
        r = np.sqrt(np.sum(x**2))
        radial_factor = 1.0 + 0.5 * np.sin(2.0 * r) * np.cos(3.0 * r)
        result += radial_factor * (r**2 - 4.0 * r + 4.0)
        
        # Composite sinusoidal terms with varying frequencies and phases
        for i in range(self.dim):
            xi = x[i]
            # Multiple harmonic components
            result += 0.5 * np.sin(5.0 * xi) + 0.3 * np.cos(7.0 * xi) + 0.2 * np.sin(11.0 * xi)
            
        # Cross-dimensional coupling with interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.1 * np.sin(2.0 * (xi + xj)) * np.cos(1.5 * (xi - xj))
                
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(0.5 * self.dim)
        result *= scale_factor
        
        # Nested multimodal structure with local minima
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**4 - 2.0 * xi**2 + 1.0) * np.exp(-xi**2/2.0)
            
        # Additional periodic modulation with dynamic frequency
        freq_mod = 1.0 + 0.2 * np.sin(0.3 * self.dim)
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.cos(freq_mod * xi) * np.sin(0.7 * xi)
            
        # Symmetric saddle point configuration
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.2 * (xi**2 - xj**2) * np.sin(xi + xj)
                
        # Gaussian-like local optima with varying heights
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.exp(-0.5 * (xi - 1.0)**2) + 0.1 * np.exp(-0.5 * (xi + 1.0)**2)
            
        return result