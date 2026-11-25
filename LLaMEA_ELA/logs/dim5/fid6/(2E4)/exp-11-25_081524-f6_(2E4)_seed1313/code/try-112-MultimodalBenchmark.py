import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like radial basis functions with self-similarity
        rbfs = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            rbfs += np.exp(-0.3 * dist / (1.0 + 0.2 * np.abs(x[i]) + 0.1 * i)) * np.sin(0.5 * i + x[i])**2
        
        # Time-varying cross-dimensional coupling with fractal scaling
        exp_coupling = 0.0
        for i in range(self.dim-2):
            coupling_strength = 0.5 + 0.5 * np.sin(0.3 * i + self.dim)
            exp_coupling += np.exp(-0.4 * np.abs(x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2) * coupling_strength
        
        # Dynamic global skewness with multi-scale modulation
        skewness = 0.0
        for i in range(self.dim):
            skewness += (x[i]**4) * np.sin(0.7 * self.dim + x[i]) * np.cos(0.3 * i)
        
        # Polynomial ridge structures with fractal exponents and self-similarity
        ridges = 0.0
        for i in range(self.dim-1):
            exponent = 2.5 + 0.3 * np.sin(0.4 * i + self.dim) + 0.2 * np.cos(0.6 * i)
            ridges += (np.abs(x[i] - x[i+1])**exponent) * (1.0 + 0.2 * np.sin(0.5 * i))
        
        # Multi-scale sinusoidal modulation with chaotic frequency variations
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.4 * i + self.dim) + 0.8 * np.cos(0.6 * i)
            sin_mod += np.sin(freq * x[i] + 0.7 * self.dim) * np.cos(2.0 * x[i] + 0.3 * i)
        
        # Adaptive chaotic modulation with basin-hopping dynamics
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += np.sin(5.0 * x[i] + 0.8 * self.dim) * np.tan(1.2 * x[i]) * np.exp(-0.1 * i)
        
        # Self-similar scaling factor with fractal dimension
        dim_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(0.3 * self.dim)
        
        return (rbfs + exp_coupling + skewness + ridges + sin_mod + chaos_mod) * dim_scale