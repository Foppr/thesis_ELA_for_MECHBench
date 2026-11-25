import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.a = 3.9
        self.r = 0.5
        self.seed = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Chaotic modulation using logistic map
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor)
            if i < len(x):
                f_val += 0.5 * np.sin(chaos_factor * x[i]) * np.cos(0.3 * x[i])
        
        # Radial basis function peaks with varying widths and positions
        peak_centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.5 + 0.5 * np.sin(i)
                f_val += 0.3 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Fractal-like oscillations with recursive frequency modulation
        freq_mod = 1.0
        for i in range(self.dim):
            freq_mod = 1 + 0.1 * np.sin(freq_mod * x[i])
            f_val += 0.2 * np.sin(freq_mod * x[i]) * np.cos(3 * x[i])
            
        # Saddle point structure with directional dependency
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.1 * (x[i]**2 - x[i+1]**2) * np.cos(0.5 * x[i])
                
        # Cross-dimensional coupling with exponential interaction
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.15 * np.exp(-abs(x[i] + x[i+1] + x[i+2])) * np.sin(0.4 * x[i])
                
        return f_val