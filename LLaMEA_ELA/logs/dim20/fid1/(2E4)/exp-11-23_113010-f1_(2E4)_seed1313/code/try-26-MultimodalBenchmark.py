import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(10 * np.pi * r) * np.exp(-r**2)
        
        # Trigonometric sum with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * 2 * np.pi * x_norm[i])
        
        # Piecewise penalty based on quadrant regions
        penalty = 0.0
        for i in range(self.dim):
            if x_norm[i] > 0:
                penalty += np.exp(-x_norm[i]**2)
            else:
                penalty += np.exp(x_norm[i]**2) * 0.5
        
        # Cross-dimensional interaction using a chaotic map
        chaos = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            chaos += np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j])
        
        # Add noise term from a heavy-tailed distribution
        noise = 0.05 * np.random.standard_t(3)
        
        return radial + 0.7 * trig_sum + 0.3 * penalty + 0.4 * chaos + noise