import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potentials with varying degrees
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**2 + x[i]**4 + 0.5 * x[i]**6) * np.exp(-0.1 * x[i]**2)
            
        # Radial harmonic interactions with time-varying weights
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
            f2 += weight * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional coupling with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.8 + 0.4 * np.sin(0.3 * (i - j) + 0.1 * r)
                f3 += coeff * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                f4 += 0.5 * dist**2 * np.exp(-0.1 * dist)
                
        # Time-varying weights based on global fitness
        f5 = 0.0
        global_fitness = f1 + f2 + f3 + f4
        for i in range(self.dim):
            time_weight = 1.0 + 0.2 * np.sin(0.1 * i + 0.05 * global_fitness)
            f5 += time_weight * x[i]**3 * np.exp(-0.04 * x[i]**2)
            
        # Enhanced chaotic modulation
        f6 = 0.0
        for i in range(self.dim):
            chaos = 0.3 * np.sin(1.7 * x[i] + 0.2 * r) * np.cos(2.3 * x[i] + 0.1 * r)
            f6 += chaos * np.exp(-0.02 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6