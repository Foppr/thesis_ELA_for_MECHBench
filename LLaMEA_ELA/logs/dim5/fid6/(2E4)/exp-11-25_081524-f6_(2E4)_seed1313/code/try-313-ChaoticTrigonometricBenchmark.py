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
            freq1 = 1.0 + 0.6 * np.sin(0.35 * i + 0.12 * self.dim)
            freq2 = 1.0 + 0.35 * np.cos(0.45 * i + 0.22 * self.dim)
            result += 0.55 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.22 * np.sin(5.5 * xi))
            
        # Polynomial coupling with radial dependency - modified exponents and coefficients
        for i in range(self.dim):
            xi = x[i]
            result += 0.35 * (xi**5 - 2*xi**3 + xi) * np.exp(-r/4.0)
            
        # Multi-scale harmonic interference - altered frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(11.0 * xi + 0.55 * r) * np.cos(7.5 * xi + 0.35 * r)
            
        # Cross-dimensional coupling with sine-cosine combinations - modified interaction strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.12 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.12 * np.sin(3.5 * r))
                
        # Nested polynomial structure with varying exponents - altered coefficients
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * (xi**6 - 3*xi**4 + 3*xi**2 - 1) * np.exp(-xi**2/2.5)
            
        # Enhanced radial symmetry with chaotic perturbations - modified amplitude and phase
        result += 0.28 * r * np.sin(4.2 * r + 0.52 * self.dim) * np.cos(3.2 * r + 0.32 * self.dim)
        
        # Additional trigonometric interference terms - modified frequencies and decay
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * np.sin(14.5 * xi) * np.cos(8.5 * xi) * np.exp(-xi**2/3.5)
            
        return result