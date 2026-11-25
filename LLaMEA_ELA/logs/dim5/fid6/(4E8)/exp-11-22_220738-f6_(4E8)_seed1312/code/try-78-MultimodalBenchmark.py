import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with improved complexity
        self.a = 3.92
        self.r = 0.62
        self.seed = 0.15
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with slight modification
        f_val = 0.8 * np.sum(x**2)
        
        # Chaotic modulation using logistic map with enhanced complexity and better distribution
        chaos_factor = self.seed
        for i in range(self.dim):
            chaos_factor = self.a * chaos_factor * (1 - chaos_factor)
            if i < len(x):
                f_val += 0.85 * np.sin(chaos_factor * x[i]) * np.cos(0.35 * x[i]) * np.sin(0.3 * x[i])
        
        # Radial basis function peaks with varying widths, positions, and heights
        peak_centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        for i in range(len(peak_centers)):
            if i < self.dim:
                center = peak_centers[i % len(peak_centers)]
                width = 0.4 + 0.6 * np.sin(i * 0.6)
                height = 0.5 + 0.5 * np.cos(i * 0.4)
                f_val += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Fractal-like oscillations with recursive frequency modulation and phase shifts
        freq_mod = 1.1
        for i in range(self.dim):
            freq_mod = 1 + 0.3 * np.sin(freq_mod * x[i]) + 0.2 * np.cos(freq_mod * x[i])
            f_val += 0.4 * np.sin(freq_mod * x[i]) * np.cos(5.0 * x[i]) * np.tan(0.4 * x[i])
            
        # Enhanced saddle point structure with directional dependency and non-linearity
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.25 * (x[i]**3 - x[i+1]**3) * np.cos(0.8 * x[i]) + 0.15 * (x[i] - x[i+1])**2
                
        # Cross-dimensional coupling with exponential interaction and trigonometric modulation
        if self.dim >= 3:
            for i in range(self.dim - 2):
                f_val += 0.25 * np.exp(-abs(x[i] + x[i+1] + x[i+2])) * np.sin(0.6 * x[i]) * np.cos(0.25 * x[i+1])
                
        # Additional high-frequency oscillatory component with improved amplitude
        for i in range(self.dim):
            f_val += 0.18 * np.sin(11.0 * x[i]) * np.cos(7.5 * x[i])
            
        # Add a small noise term to avoid perfect symmetry and improve challenge
        noise = 0.02 * np.sum(np.sin(x) * np.cos(x))
        f_val += noise
            
        return f_val