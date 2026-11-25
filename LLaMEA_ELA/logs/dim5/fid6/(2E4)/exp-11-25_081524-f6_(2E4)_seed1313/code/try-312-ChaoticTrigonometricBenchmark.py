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
            freq1 = 1.5 + 0.3 * np.sin(0.4 * i + 0.15 * self.dim)
            freq2 = 1.2 + 0.4 * np.cos(0.3 * i + 0.25 * self.dim)
            result += 0.6 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.3 * np.sin(4.0 * xi))
            
        # Polynomial coupling with radial dependency - modified exponents
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**5 - 2*xi**3 + xi) * np.exp(-r/6.0)
            
        # Multi-scale harmonic interference - changed frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(12.0 * xi + 0.6 * r) * np.cos(8.0 * xi + 0.4 * r)
            
        # Cross-dimensional coupling with sine-cosine combinations - altered interaction strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.15 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.15 * np.sin(2.5 * r))
                
        # Nested polynomial structure with varying exponents - changed coefficients
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * (xi**7 - 3*xi**5 + 3*xi**3 - xi) * np.exp(-xi**2/2.5)
            
        # Enhanced radial symmetry with chaotic perturbations - modified amplitude
        result += 0.3 * r * np.sin(4.5 * r + 0.6 * self.dim) * np.cos(3.5 * r + 0.35 * self.dim)
        
        # Additional trigonometric interference terms - changed frequencies and decay
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * np.sin(14.0 * xi) * np.cos(9.0 * xi) * np.exp(-xi**2/3.5)
            
        return result