import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic radial basis functions with dynamic conditioning
        rbfs = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            rbfs += np.exp(-0.3 * dist / (1.0 + 0.2 * np.abs(x[i]) + 0.05 * i)) * np.sin(0.7 * x[i] + i)
        
        # Stronger cross-dimensional exponential coupling with chaotic modulation
        exp_coupling = 0.0
        for i in range(self.dim-1):
            coupling_strength = 0.5 + 0.5 * np.sin(0.3 * i + self.dim)
            exp_coupling += coupling_strength * np.exp(-0.4 * np.abs(x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2 + 0.1 * x[i] * x[i+1])
        
        # Enhanced global skewness with dynamic phase shifts
        skewness = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.2 * i + self.dim)
            skewness += (x[i]**4) * np.cos(phase_shift + 0.6 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Dynamic polynomial ridges with chaotic exponents and multi-scale modulation
        ridges = 0.0
        for i in range(self.dim-2):
            exponent = 2.5 + 0.8 * np.sin(0.4 * i + self.dim) + 0.3 * np.cos(0.6 * i)
            ridge_strength = 1.0 + 0.3 * np.sin(0.5 * i + self.dim)
            ridges += ridge_strength * (np.abs(x[i] - x[i+1])**exponent) * (1.0 + 0.2 * np.cos(x[i]) + 0.1 * np.sin(x[i+1]))
        
        # Chaotic sinusoidal modulation with adaptive frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.5 * np.sin(0.3 * i + self.dim)
            sin_mod += np.sin(freq * x[i] + 0.4 * self.dim) * np.cos(freq * x[i] + 0.3 * i)
        
        # Multi-scale adaptive scaling factor
        dim_scale = 1.5 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(0.5 * self.dim)
        
        return (rbfs + exp_coupling + skewness + ridges + sin_mod) * dim_scale