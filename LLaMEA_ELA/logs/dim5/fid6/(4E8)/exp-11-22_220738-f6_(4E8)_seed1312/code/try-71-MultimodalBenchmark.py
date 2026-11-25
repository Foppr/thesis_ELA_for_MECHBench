import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.a = 4.02
        self.r = 0.67
        self.seed = 0.23
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with scaling
        f_val = 0.8 * np.sum(x**2)
        
        # Enhanced chaotic modulation using modified logistic map
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor) + 0.05 * np.sin(chaos_factor * x[i])
            if i < len(x):
                f_val += 1.2 * np.sin(chaos_factor * x[i]) * np.cos(0.6 * x[i]) * np.sin(0.3 * x[i])
        
        # Multiple Gaussian peaks with dynamic parameters
        peak_centers = np.linspace(-4.5, 4.5, min(9, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.2 + 0.8 * np.sin(i * 0.7)
                height = 0.3 + 0.7 * np.cos(i * 0.4)
                f_val += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Complex fractal-like oscillations with multi-scale modulation
        freq_mod = 1.1
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(freq_mod * x[i]) + 0.2 * np.cos(freq_mod * x[i]) + 0.1 * np.tan(0.5 * freq_mod)
            f_val += 0.5 * np.sin(freq_mod * x[i]) * np.cos(5.0 * x[i]) * np.tan(0.4 * x[i])
            
        # Stronger saddle point structure with non-linear coupling
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.35 * (x[i]**4 - x[i+1]**4) * np.cos(0.9 * x[i]) + 0.18 * (x[i] - x[i+1])**3
                
        # Advanced cross-dimensional coupling with polynomial interactions
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.28 * np.exp(-abs(x[i] + x[i+1] + x[i+2])) * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i+1]) * np.tan(0.2 * x[i+2])
                
        # Additional high-frequency chaotic component
        for i in range(self.dim):
            f_val += 0.25 * np.sin(12.0 * x[i]) * np.cos(8.5 * x[i]) * np.sin(0.6 * x[i])
            
        return f_val