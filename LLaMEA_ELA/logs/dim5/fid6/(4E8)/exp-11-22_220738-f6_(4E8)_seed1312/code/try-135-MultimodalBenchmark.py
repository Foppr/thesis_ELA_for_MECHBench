import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 3.99
        self.seed = 0.78
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dimension scaling
        f_val = 0.5 * np.sum(x**2) / self.dim
        
        # Multi-scale sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 3.1 * np.sin(3.7 * np.pi * x[i]) * np.cos(1.8 * x[i])
            f_val += 2.3 * np.sin(6.2 * np.pi * x[i]) * np.cos(3.5 * x[i])
            
        # Gaussian radial basis functions with dynamic centers and widths
        num_peaks = min(9, self.dim)
        for i in range(num_peaks):
            center = -4.8 + 2.7 * i
            width = 0.6 + 0.9 * np.sin(i * 1.1)  # Modified width range
            f_val += 2.8 * np.exp(-0.5 * ((x[i % self.dim] - center) / width)**2)
            
        # Chaotic saddle point structure with logistic map modulation
        chaos_val = self.seed
        for i in range(self.dim):
            chaos_val = self.chaos_param * chaos_val * (1 - chaos_val)
            f_val += 1.9 * chaos_val * np.sin(x[i % self.dim]) * np.cos(0.8 * x[i % self.dim])
            
        # Dynamic scaling factor based on coordinate values
        scale_factor = 1.0 + 0.8 * np.mean(np.abs(x))
        f_val *= scale_factor
        
        # Cross-dimensional coupling with polynomial interactions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 1.7 * (x[i]**3 + x[i+1]**3) * np.sin(0.9 * x[i])
                
        # Asymmetric exponential saddle points
        for i in range(self.dim):
            f_val += 1.6 * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(0.5 * x[i]) + \
                     1.4 * np.exp(-0.5 * (x[i] + 1.0)**2) * np.cos(0.5 * x[i])
        
        # Additional chaotic sine-wave interactions
        for i in range(self.dim):
            f_val += 1.5 * np.sin(4.0 * np.pi * x[i]) * np.cos(2.5 * x[i])
            
        # Enhanced noise sensitivity through higher-order polynomial terms
        for i in range(self.dim):
            f_val += 0.3 * x[i]**5 + 0.2 * x[i]**4
            
        # Introduce additional ruggedness via fractional Brownian motion inspired terms
        for i in range(self.dim):
            f_val += 0.8 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Add a novel hyperchaotic tent map component with adaptive scaling
        tent_map = 0.5
        for i in range(self.dim):
            if tent_map < 0.5:
                tent_map = 2 * tent_map
            else:
                tent_map = 2 * (1 - tent_map)
            f_val += 1.2 * tent_map * np.sin(3.0 * x[i])
            
        # Introduce cross-dimensional coupling with trigonometric interference
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 1.1 * np.sin(x[i] + x[i+1]) * np.cos(x[i+2]) * (x[i]**2 + x[i+1]**2)
                
        return f_val