import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for fractal structure
        self.chaos_seq = np.array([np.sin(1.5**i) for i in range(dim)])
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like radial component with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        fractal_radial = np.sin(10 * r) * np.exp(-0.5 * r**2) * (1.0 + 0.2 * np.sum(self.chaos_seq * np.sin(3 * x_norm)))
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            if i > 0:
                saddle += 0.1 * np.tanh(x_norm[i-1] * x_norm[i]) * np.sin(5 * x_norm[i])
        
        # Multi-scale periodicity with varying amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3)
            amp = 1.0 / (1.0 + i * 0.1)
            periodic += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] + i)
        
        # Cross-dimensional coupling with asymmetric weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.03 * (x_norm[i]**3) * np.sin(4 * x_norm[j]) * (i + 1) / (j + 1)
        
        # Global minimum at origin with additional penalty for distance from origin
        penalty = 0.5 * r**2
        
        return 0.3 * fractal_radial + 0.4 * saddle + 0.2 * periodic + 0.05 * coupling + penalty