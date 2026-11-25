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
        
        # Chaotic modulation using logistic map with enhanced complexity
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor)
            if i < len(x):
                f_val += 0.8 * np.sin(chaos_factor * x[i]) * np.cos(0.5 * x[i]) * np.sin(0.2 * x[i])
        
        # Radial basis function peaks with varying widths, positions, and heights
        peak_centers = np.linspace(-4, 4, min(7, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.3 + 0.7 * np.sin(i * 0.5)
                height = 0.4 + 0.6 * np.cos(i * 0.3)
                f_val += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Fractal-like oscillations with recursive frequency modulation and phase shifts
        freq_mod = 1.0
        for i in range(self.dim):
            freq_mod = 1 + 0.2 * np.sin(freq_mod * x[i]) + 0.1 * np.cos(freq_mod * x[i])
            f_val += 0.3 * np.sin(freq_mod * x[i]) * np.cos(4 * x[i]) * np.tan(0.3 * x[i])
            
        # Enhanced saddle point structure with directional dependency and non-linearity
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.2 * (x[i]**3 - x[i+1]**3) * np.cos(0.7 * x[i]) + 0.1 * (x[i] - x[i+1])**2
                
        # Cross-dimensional coupling with exponential interaction and trigonometric modulation
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.2 * np.exp(-abs(x[i] + x[i+1] + x[i+2])) * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i+1])
                
        # Additional high-frequency oscillatory component
        for i in range(self.dim):
            f_val += 0.15 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        return f_val