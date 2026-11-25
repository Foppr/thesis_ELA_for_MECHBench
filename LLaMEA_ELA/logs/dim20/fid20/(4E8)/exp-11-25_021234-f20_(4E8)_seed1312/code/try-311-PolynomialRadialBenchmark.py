import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion terms with varying degrees and weights
        f1 = 0.0
        for i in range(self.dim):
            degree = 3 + int(2 * np.sin(0.5 * i))
            weight = 1.0 + 0.5 * np.cos(0.3 * i)
            f1 += weight * (x[i] ** degree) * np.exp(-0.1 * x[i]**2)
            
        # Radial symmetry breaking with adaptive scaling
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            scale = 1.5 + 0.8 * np.sin(0.4 * i + 0.3 * r)
            f2 += scale * np.exp(-0.5 * ((x[i] - 0.5 * np.sin(0.6 * i)) / (0.8 + 0.2 * np.cos(0.4 * i)))**2)
            
        # Dynamic gradient modulation with time-varying coefficients
        f3 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
            f3 += mod * x[i]**2 * np.cos(2.0 * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional coupling with harmonic interaction
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                strength = 0.8 + 0.4 * np.sin(0.2 * (i + j))
                f4 += strength * coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Adaptive conditioning with radial dependence
        f5 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.7 * np.sin(0.3 * r + 0.2 * i)
            f5 += cond * x[i]**6
            
        # Multi-scale oscillatory components with phase shifts
        f6 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.4 * i + 0.1 * r)
            f6 += np.sin(3.0 * x[i] + phase) * np.exp(-0.2 * x[i]**2)
            
        # Boundary handling with repulsive forces
        f7 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                dist = np.abs(x[i]) - 4.5
                f7 += 3.0 * dist**2.5 * np.exp(-0.3 * dist)
                
        # Fractal-like recursive structure with self-similarity
        f8 = 0.0
        for i in range(self.dim):
            scale = 0.8 + 0.3 * np.sin(0.6 * i + 0.2 * r)
            f8 += scale * np.sin(5.0 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f8