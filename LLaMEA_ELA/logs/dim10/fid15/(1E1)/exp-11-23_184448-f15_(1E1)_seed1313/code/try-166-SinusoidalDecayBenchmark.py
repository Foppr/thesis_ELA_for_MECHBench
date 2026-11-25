import numpy as np

class SinusoidalDecayBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        quadratic = np.sum(x**2) / (2.0 * self.dim)
        
        # Periodic sinusoidal components with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            periodic += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
        
        # Exponential decay interactions between variables
        decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                decay += np.exp(-dist) * (x[i]**2 + x[j]**2)
        
        # Adaptive noise component that scales with dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2)) * np.tan(x[i] / (i + 3))
        
        # Ridge structure with exponential modulation
        ridge = 0.0
        for i in range(self.dim):
            ridge += np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(2.0 * x[i])
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (0.3 * quadratic + 0.3 * periodic + 
                              0.2 * decay + 0.1 * noise + 0.1 * ridge)