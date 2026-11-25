import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic harmonic base with time-like evolution parameter
        t = np.sum(x**2) / self.dim
        chaotic_factor = 1.0 + 0.3 * np.sin(10.0 * t) * np.cos(7.0 * t)
        
        # Quadratic basin with chaotic scaling
        result += chaotic_factor * (np.sum(x**2) - 2.0 * np.sum(x)) + 1.0
        
        # Directional bias field with fractal-like perturbations
        for i in range(self.dim):
            xi = x[i]
            # Create asymmetric valleys using sine and cosine with varying phases
            bias_term = 0.5 * np.sin(3.0 * xi + i * 0.5) * np.cos(2.0 * xi + i * 0.3)
            result += bias_term
            
        # Multi-scale harmonic interference with dynamic frequencies
        for i in range(self.dim):
            xi = x[i]
            freq1 = 1.0 + 0.5 * np.sin(i * 0.7)
            freq2 = 1.5 + 0.3 * np.cos(i * 0.9)
            result += 0.3 * np.sin(freq1 * xi) * np.cos(freq2 * xi)
            
        # Energy valley structure with varying depths
        for i in range(self.dim):
            xi = x[i]
            valley_depth = 0.8 + 0.2 * np.sin(0.5 * i)
            result += valley_depth * (xi**2 - 2.0 * xi + 1.0) * np.exp(-0.5 * xi**2)
            
        # Cross-dimensional coupling with chaotic phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                phase_shift = 0.1 * np.sin(i * 0.3 + j * 0.4)
                coupling = np.sin(2.0 * (xi + xj + phase_shift)) * np.cos(1.5 * (xi - xj))
                result += 0.2 * coupling
                
        # Asymmetric saddle points with variable curvature
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                asymmetry = 0.5 + 0.3 * np.sin(i * 0.6)
                result += asymmetry * (xi**2 - xj**2) + 0.4 * np.sin(xi + xj)
                
        # Gaussian-like local minima with varying widths and heights
        for i in range(self.dim):
            xi = x[i]
            height = 0.6 + 0.2 * np.sin(i * 0.4)
            width = 0.8 + 0.3 * np.cos(i * 0.5)
            result += height * np.exp(-0.5 * (xi - 1.0)**2 / width**2)
            
        # Add chaotic modulation with global scaling factor
        global_mod = 1.0 + 0.2 * np.sin(0.1 * self.dim) * np.cos(0.15 * self.dim)
        result *= global_mod
        
        return result