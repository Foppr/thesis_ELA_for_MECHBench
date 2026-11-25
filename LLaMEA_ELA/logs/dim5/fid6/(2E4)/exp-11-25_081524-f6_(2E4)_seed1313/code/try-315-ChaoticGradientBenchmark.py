import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        result += (r**3) * np.sin(4.0 * r) * np.cos(3.0 * r) * np.exp(-r/10.0)
        
        # Intensified chaotic trigonometric terms with dynamic frequencies
        for i in range(self.dim):
            xi = x[i]
            freq1 = 2.0 + 1.5 * np.sin(0.4 * i + 0.2 * self.dim)
            freq2 = 1.5 + 0.8 * np.cos(0.5 * i + 0.3 * self.dim)
            result += 0.8 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.3 * np.sin(7.0 * xi))
            
        # Enhanced polynomial coupling with radial dependency
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * (xi**5 - 2*xi**3 + xi) * np.exp(-r/8.0)
            
        # Multi-scale harmonic interference with variable amplitudes
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(12.0 * xi + 0.6 * r) * np.cos(9.0 * xi + 0.4 * r) * (1.0 + 0.2 * np.cos(4.0 * r))
            
        # Enhanced cross-dimensional coupling with sine-cosine combinations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.2 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.2 * np.sin(5.0 * r)) * np.exp(-abs(xi-xj)/5.0)
                
        # Nested polynomial structure with varying exponents and chaotic perturbations
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**7 - 4*xi**5 + 6*xi**3 - 4*xi) * np.exp(-xi**2/3.0)
            
        # Enhanced radial symmetry with chaotic perturbations and additional harmonics
        result += 0.4 * r**2 * np.sin(5.0 * r + 0.6 * self.dim) * np.cos(4.0 * r + 0.4 * self.dim) * np.exp(-r/15.0)
        
        # Additional high-frequency trigonometric interference terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(20.0 * xi) * np.cos(12.0 * xi) * np.exp(-xi**2/4.0)
            
        # Cross-dimensional chaotic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.15 * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/3.0) * (1.0 + 0.1 * np.sin(6.0 * r))
                
        # High-order polynomial with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * (xi**8 - 5*xi**6 + 10*xi**4 - 10*xi**2 + 1) * np.exp(-xi**2/5.0)
            
        return result