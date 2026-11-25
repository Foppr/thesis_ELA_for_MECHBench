import numpy as np

class PolynomialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 20)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic term for conditioning
        f1 = 0.05 * np.sum(x**2)
        
        # Polynomial chaos expansion with mixed terms
        f2 = 0.0
        for i in range(self.dim):
            f2 += (x[i]**4 - 6*x[i]**2 + 9) * np.sin(0.5 * x[i])
            
        # Radial basis function ensemble
        f3 = 0.0
        for i in range(20):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.sum((x - center)**2)
            f3 += np.exp(-distance / (2 * width**2)) * np.sin(np.sum(center))
            
        # Dynamic saddle-point interactions
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Varying coupling strength based on position
                coupling = 0.3 + 0.2 * np.sin(0.1 * (x[i] + x[j]))
                f4 += coupling * np.sin(x[i]) * np.cos(x[j])
                
        # Multi-scale sinusoidal modulation with adaptive frequencies
        f5 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.5 * np.cos(0.2 * i)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Asymmetric penalty landscape
        f6 = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                penalty = 2.0 * x[i]**3
            else:
                penalty = -1.5 * x[i]**3
            f6 += penalty * np.exp(-0.05 * x[i]**2)
            
        # Cross-term interactions with varying exponents
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent = 1.0 + 0.5 * np.sin(0.2 * (i + j))
                f7 += (x[i]**exponent) * (x[j]**(3 - exponent))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7