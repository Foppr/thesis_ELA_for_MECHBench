import numpy as np

class AdaptiveSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Asymmetric quadratic basin with dynamic curvature
            curvature = 1.0 + 0.5 * np.sin(self.dim * 0.2 + i * 0.3) + 0.3 * np.cos(self.dim * 0.15 + i * 0.4)
            basin = 0.5 * curvature * xi**2
            
            # Embedded saddle point with varying strength
            saddle_strength = 0.8 + 0.4 * np.sin(i * 0.5 + self.dim * 0.3)
            saddle = saddle_strength * xi * np.cos(3 * xi) * np.exp(-0.5 * xi**2)
            
            # Asymmetric cubic term for complex landscape
            asymmetry = 0.3 * np.sin(i * 0.7 + self.dim * 0.25)
            cubic = (1.0 + asymmetry) * xi**3
            
            # Dynamic multimodal component with dimension-dependent frequency
            freq_factor = 1.0 + 0.4 * np.cos(self.dim * 0.1 + i * 0.2)
            modal_term = 0.5 * freq_factor * np.sin(5 * xi + i * 0.3)**2
            
            # Cross-dimensional interaction with adaptive coupling
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling += 0.1 * np.sin(xi + x_norm[j] + 0.2 * i) * np.cos(2 * xi - x_norm[j] + 0.1 * j)
            
            # Dimensionally adaptive scaling factor
            scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.4 + i * 0.25)
            
            # Add all components to the result
            result += scale_factor * (basin + saddle + cubic + modal_term + coupling)
        
        # Global adaptive correction based on problem dimensionality
        global_correction = 1.0 + 0.2 * np.sin(self.dim * 0.3) + 0.1 * np.cos(self.dim * 0.2)
        
        return global_correction * result / self.dim