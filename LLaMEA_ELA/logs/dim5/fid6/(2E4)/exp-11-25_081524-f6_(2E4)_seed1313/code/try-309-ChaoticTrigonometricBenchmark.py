import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial component with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        result += (r**2) * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Chaotic trigonometric terms with time-varying frequencies
        for i in range(self.dim):
            xi = x[i]
            freq1 = 1.0 + 0.5 * np.sin(0.3 * i + 0.1 * self.dim)
            freq2 = 1.0 + 0.3 * np.cos(0.4 * i + 0.2 * self.dim)
            result += 0.5 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.2 * np.sin(5.0 * xi))
            
        # Polynomial coupling with radial dependency
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**4 - 2*xi**2 + 1) * np.exp(-r/5.0)
            
        # Multi-scale harmonic interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * np.sin(10.0 * xi + 0.5 * r) * np.cos(7.0 * xi + 0.3 * r)
            
        # Cross-dimensional coupling with sine-cosine combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.1 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.1 * np.sin(3.0 * r))
                
        # Nested polynomial structure with varying exponents
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * (xi**6 - 3*xi**4 + 3*xi**2 - 1) * np.exp(-xi**2/2.0)
            
        # Enhanced radial symmetry with chaotic perturbations
        result += 0.25 * r * np.sin(4.0 * r + 0.5 * self.dim) * np.cos(3.0 * r + 0.3 * self.dim)
        
        # Additional trigonometric interference terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * np.sin(15.0 * xi) * np.cos(8.0 * xi) * np.exp(-xi**2/3.0)
            
        return result