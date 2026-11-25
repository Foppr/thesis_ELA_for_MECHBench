import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**2 + 0.5 * x[i]**4 + 0.3 * x[i]**6) * np.exp(-0.1 * x[i]**2)
            
        # Radial harmonic interactions with time-varying weights
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.2 * i + 0.1 * r)
            f2 += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional coupling with dynamic interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.4 * np.sin(0.15 * (i + j) + 0.2 * r)
                interaction = np.sin(x[i] + x[j]) + np.cos(x[i] - x[j])
                f3 += coupling_strength * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction with polynomial penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 2.0 * (np.abs(x[i]) - 4.0)**3
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Time-varying weights with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            time_weight = 1.0 + 0.3 * np.sin(0.3 * i + 0.2 * r + 0.4 * np.random.uniform(-1, 1))
            f5 += time_weight * x[i]**5 * np.exp(-0.08 * x[i]**2)
            
        # Multi-scale fractal-like interactions with sine modulation
        f6 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(0.5 * i + 0.3 * r)
            f6 += scale_factor * np.sin(5.0 * x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Enhanced cross-dimensional quartic terms
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.cos(0.2 * (i - j) + 0.3 * r)
                f7 += weight * x[i]**4 * x[j]**2 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with exponential decay
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 1.5 * np.exp(-0.2 * (np.abs(x[i]) - 4.5)**2)
                f8 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Adaptive radial conditioning with polynomial scaling
        radial_factor = 1.0 + 0.6 * np.sin(0.3 * r) * np.cos(0.2 * r)
        f9 = 0.0
        for i in range(self.dim):
            f9 += radial_factor * x[i]**3 * np.exp(-0.03 * x[i]**2)
            
        # Combined harmonic and polynomial terms with dynamic coupling
        f10 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.1 * i + 0.05 * r)
            f10 += np.sin(freq * x[i]) * (x[i]**2 + 1.0) * np.exp(-0.07 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10