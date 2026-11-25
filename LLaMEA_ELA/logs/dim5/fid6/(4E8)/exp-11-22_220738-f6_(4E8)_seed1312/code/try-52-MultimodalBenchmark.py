import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.a = 3.8
        self.r = 0.6
        self.seed = 0.15
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2) * 0.8
        
        # Chaotic modulation using logistic map with enhanced complexity
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor)
            if i < len(x):
                f_val += 0.6 * np.sin(chaos_factor * x[i]) * np.cos(0.4 * x[i])
        
        # Enhanced radial basis function peaks with dynamic widths and positions
        peak_centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.3 + 0.7 * np.sin(i * 0.5)
                f_val += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Fractal-like oscillations with recursive frequency modulation and additional harmonics
        freq_mod = 1.0
        for i in range(self.dim):
            freq_mod = 1 + 0.15 * np.sin(freq_mod * x[i])
            f_val += 0.25 * np.sin(freq_mod * x[i]) * np.cos(3 * x[i]) + 0.1 * np.sin(5 * x[i])
            
        # Enhanced saddle point structure with directional dependency and nonlinearity
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.15 * (x[i]**3 - x[i+1]**3) * np.cos(0.6 * x[i])
                
        # Improved cross-dimensional coupling with polynomial interaction and increased nonlinearity
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.2 * (x[i] + x[i+1] + x[i+2])**3 * np.sin(0.5 * x[i])
                
        # Additional chaotic perturbation term to increase landscape complexity
        chaos_pert = 0.0
        for i in range(min(3, self.dim)):
            chaos_pert += np.sin(self.a * (x[i] + 0.1) * (1 - x[i])) if i < len(x) else 0
        f_val += 0.1 * chaos_pert
        
        return f_val