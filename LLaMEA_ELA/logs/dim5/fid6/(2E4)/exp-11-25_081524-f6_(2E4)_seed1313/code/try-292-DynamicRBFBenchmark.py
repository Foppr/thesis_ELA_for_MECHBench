import numpy as np

class DynamicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.scale_factor = 1.0 + 0.5 * np.sin(0.5 * self.t)
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with dynamic scaling
        result = np.sum((x**4) * (1.0 + 0.3 * np.sin(2.0 * self.t)))
        
        # Trigonometric components with time-varying frequencies
        freqs = 2.0 + 1.5 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 2.0 * np.sin(freqs * xi + 0.3 * self.t) * np.cos(freqs * xi + 0.4 * self.t)
            
        # Radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(0.6 * self.t + i * 0.5)
            width = 0.5 + 0.3 * np.cos(0.7 * self.t + i * 0.4)
            xi = x[i]
            result += np.exp(-((xi - center)**2) / (2.0 * width**2))
            
        # Cross-dimensional interaction terms with enhanced coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                interaction = 0.8 * np.sin(3.0 * (xi + xj) + 0.2 * self.t)  # Increased coupling strength
                result += interaction * (xi**2 + xj**2)
                
        # Dynamic harmonic interference with modified frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * np.sin(5.0 * xi + 0.1 * self.t) * np.cos(4.0 * xi + 0.2 * self.t)
            
        # Multi-scale periodicity with varying amplitudes
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.sin(10.0 * xi + 0.5 * self.t) * (1.0 + 0.2 * np.cos(2.0 * self.t))
            
        # Adaptive basin structure with time-varying depth
        basin_depth = 1.5 + 0.8 * np.sin(0.9 * self.t)
        result += basin_depth * np.sum(x**2 * np.exp(-x**2/4.0))
        
        # Additional coupling between dimensions through nonlinear transformation with modified strength
        coupling_strength = 0.6 + 0.3 * np.cos(1.1 * self.t)  # Increased coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += coupling_strength * np.sin(x[i] * x[j] + 0.1 * self.t) * (x[i]**2 + x[j]**2)
                
        return result