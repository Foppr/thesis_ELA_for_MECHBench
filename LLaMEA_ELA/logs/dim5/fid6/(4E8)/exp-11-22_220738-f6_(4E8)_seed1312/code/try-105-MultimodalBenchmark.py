import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.99
        self.seed = 0.123
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dimension scaling
        f_val = 0.5 * np.sum(x**2) / self.dim
        
        # Multi-scale sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 3.1 * np.sin(4.2 * np.pi * x[i]) * np.cos(1.1 * x[i])
            f_val += 1.8 * np.sin(7.3 * np.pi * x[i]) * np.cos(2.3 * x[i])
            f_val += 0.9 * np.sin(2.5 * np.pi * x[i]) * np.cos(0.5 * x[i])
            
        # Gaussian radial basis functions with dynamic centers and widths
        num_peaks = min(8, self.dim)
        for i in range(num_peaks):
            center = -4.8 + 1.2 * i
            width = 0.1 + 1.1 * np.sin(i * 1.3)  # Modified width range
            f_val += 2.5 * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic saddle point structure with logistic map modulation
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 1.3 * chaos_val * np.sin(1.5 * x[i % self.dim]) * np.cos(0.6 * x[i % self.dim])
            
        # Dynamic scaling factor based on coordinate values
        scale_factor = 1.0 + 0.7 * np.mean(np.abs(x))
        f_val *= scale_factor
        
        # Cross-dimensional coupling with polynomial interactions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 1.1 * (x[i]**4 + x[i+1]**4) * np.sin(0.9 * x[i])
                
        # Asymmetric exponential saddle points
        for i in range(self.dim):
            f_val += 1.5 * np.exp(-0.3 * x[i]**2) * np.sin(2.1 * x[i]) * np.cos(0.8 * x[i])
            
        # High-frequency chaotic modulation
        chaos_mod = self.seed
        for i in range(self.dim):
            chaos_mod = self.chaos_param * chaos_mod * (1 - chaos_mod)
            f_val += 0.7 * np.sin(10.0 * chaos_mod + x[i % self.dim])
            
        return f_val