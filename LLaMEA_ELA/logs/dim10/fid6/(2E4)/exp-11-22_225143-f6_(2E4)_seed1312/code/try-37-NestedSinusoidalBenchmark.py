import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with extreme conditioning
        f_val = 10.0 * np.sum(x_norm**2)
        
        # Chaotic coupled oscillator wells with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * np.pi / self.dim)
            amp = 0.8 + 0.4 * np.cos(i * np.pi / 4)
            phase = 0.5 * np.sin(i * np.pi / 3)
            f_val += amp * np.exp(-freq * (x_norm - phase)**2) * np.sin(5 * np.pi * x_norm[i])
        
        # Adaptive ridge structures with exponentially decaying amplitudes
        for i in range(self.dim):
            ridge_amp = 2.0 * np.exp(-0.1 * i)
            ridge_freq = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            f_val += ridge_amp * np.cos(ridge_freq * x_norm[i]) * np.sin(3 * np.pi * x_norm[i]**2)
        
        # Cross-dimensional exponentially decaying interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                decay = np.exp(-0.5 * (i + j))
                f_val += decay * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j]) * np.exp(-(x_norm[i] - x_norm[j])**2)
        
        # Multi-scale chaotic modulations with varying periods
        for i in range(self.dim):
            f_val += 1.5 * np.sin(7 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[i]) * np.exp(-x_norm[i]**2)
            f_val += 0.8 * np.sin(9 * np.pi * x_norm[i]**3) * np.cos(8 * np.pi * x_norm[i]**2)
        
        # Exponentially decaying higher-order polynomial interactions
        for i in range(self.dim):
            f_val += 0.5 * (x_norm[i]**5 + x_norm[i]**6) * np.exp(-0.1 * i) * np.sin(4 * np.pi * x_norm[i])
        
        # Complex basin boundary structures with sharp transitions
        for i in range(self.dim):
            f_val += 3.0 * np.exp(-20.0 * (x_norm[i] - np.sin(i * np.pi / self.dim))**2) * np.cos(10 * np.pi * x_norm[i])
        
        # Global chaotic coupling term
        f_val += 2.5 * np.prod(np.sin(2 * np.pi * x_norm)) * np.exp(-0.5 * np.sum(x_norm**2))
        
        return f_val