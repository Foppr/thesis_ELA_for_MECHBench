import numpy as np

class NovelMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial radial component with multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        poly_radial = 0.5 * r**4 - 2.0 * r**2 + 1.0
        
        # Trigonometric angular component with multiple frequencies
        trig_angular = 0.0
        for i in range(self.dim):
            trig_angular += np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            if i > 0:
                trig_angular += 0.3 * np.sin(5 * np.pi * x_norm[i-1]) * np.sin(4 * np.pi * x_norm[i])
        
        # Exponential cross-term component
        exp_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_cross += np.exp(-2.0 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # High-frequency oscillatory component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])
        
        # Mixed polynomial and exponential term for added complexity
        mixed = 0.0
        for i in range(self.dim):
            mixed += (x_norm[i]**3) * np.exp(-0.5 * x_norm[i]**2)
        
        # Combine all components with different weights
        return 0.4 * poly_radial + 0.3 * trig_angular + 0.2 * exp_cross + 0.05 * high_freq + 0.05 * mixed