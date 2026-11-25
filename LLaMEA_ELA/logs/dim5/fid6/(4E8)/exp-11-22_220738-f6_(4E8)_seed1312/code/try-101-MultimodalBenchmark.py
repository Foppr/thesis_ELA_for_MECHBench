import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.92
        self.seed = 0.15
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dimension scaling
        f_val = 0.5 * np.sum(x**2) / self.dim
        
        # Multi-scale sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.1 * np.sin(3 * np.pi * x[i]) * np.cos(0.7 * x[i])
            f_val += 1.2 * np.sin(5 * np.pi * x[i]) * np.cos(1.5 * x[i])
            
        # Gaussian radial basis functions with dynamic centers and widths
        num_peaks = min(6, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 1.5 * i
            width = 0.2 + 0.8 * np.sin(i * 0.9)  # Modified width range
            f_val += 1.8 * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic saddle point structure with logistic map modulation
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 0.9 * chaos_val * np.sin(1.2 * x[i % self.dim]) * np.cos(0.4 * x[i % self.dim])
            
        # Dynamic scaling factor based on coordinate values
        scale_factor = 1.0 + 0.5 * np.mean(np.abs(x))
        f_val *= scale_factor
        
        # Cross-dimensional coupling with polynomial interactions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.6 * (x[i]**3 + x[i+1]**3) * np.sin(0.7 * x[i])
                
        return f_val