import numpy as np

class PolynomialChaosRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths for complexity
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed monomials
        f1 = 0.2 * np.sum((x**3 + 0.5 * x**2 - 0.3 * x) / self.dim)
        
        # Radial basis function ensemble with adaptive widths
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf_sum += np.exp(-dist / (2 * self.widths[i]**2))
        f2 = 0.3 * rbf_sum / 10
        
        # Spectral clustering inspired interference terms
        f3 = 0.25 * np.sum(np.sin(10.0 * x + np.cos(5.0 * x)) * 
                          np.cos(8.0 * x - np.sin(4.0 * x)) * 
                          (1.0 + 0.1 * np.sin(2.0 * np.sum(x**2))))
        
        # Multi-scale harmonic modulation with frequency coupling
        f4 = 0.15 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * 
                          (1.0 + 0.05 * np.cos(3.0 * x)) * 
                          (1.0 + 0.08 * np.sin(0.5 * np.sum(x))))
        
        # Fractional polynomial with variable exponents and scaling
        exponents = 2.0 + 0.4 * np.sin(0.3 * x)
        f5 = 0.2 * np.sum((x**exponents) / self.dim)
        
        # Cross-dimensional coupling with chaotic modulation
        coupling_weights = 1.0 + 0.3 * np.sin(0.7 * x[:-1] + 0.4 * x[1:])
        f6 = 0.18 * np.sum(coupling_weights * x[:-1]**1.5 * x[1:]**2.0 / self.dim)
        
        # Adaptive exponential modulation with multi-frequency interference
        f7 = 0.12 * np.sum((np.exp(0.4 * x) - np.exp(-0.6 * x)) * 
                          (np.sin(3.0 * x) + 0.5 * np.cos(2.0 * x)) * 
                          (1.0 + 0.1 * np.cos(0.8 * np.sum(x))))
        
        # Multi-scale chaotic interference with varying amplitudes
        f8 = 0.1 * np.sum(np.sin(20.0 * x + np.cos(10.0 * x)) * 
                         np.cos(18.0 * x - np.sin(9.0 * x)) * 
                         np.sin(0.2 * np.sum(x**3)))
        
        # Combined polynomial and trigonometric modulation with separable structure
        f9 = 0.14 * np.sum((x**2.5 + 0.3 * x**1.7) * np.sin(4.0 * x) / self.dim)
        
        # Enhanced non-separability through higher-order coupling
        f10 = 0.08 * np.sum(np.sin(x[:-1] + 0.5 * x[1:]) * 
                           np.cos(0.7 * x[:-1] - 0.3 * x[1:]) * 
                           (1.0 + 0.15 * np.cos(2.0 * np.sum(x))))
        
        # Fractional cross-dimensional interaction with dynamic scaling
        f11 = 0.16 * np.sum((x[:-1]**1.8 * x[1:]**2.3 + x[:-1]**2.5 * x[1:]**1.9) / self.dim)
        
        # Additional chaotic modulation with time-varying parameters
        f12 = 0.1 * np.sum(np.sin(12.0 * x + np.cos(6.0 * x)) * 
                          np.cos(14.0 * x - np.sin(7.0 * x)) * 
                          (1.0 + 0.06 * np.sin(0.3 * np.sum(x**2))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12