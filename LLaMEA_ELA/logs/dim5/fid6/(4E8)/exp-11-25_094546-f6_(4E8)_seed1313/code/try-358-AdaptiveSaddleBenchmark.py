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
            
            # Enhanced asymmetric quadratic basin with dynamic curvature
            curvature = 1.0 + 0.6 * np.sin(self.dim * 0.25 + i * 0.35) + 0.4 * np.cos(self.dim * 0.2 + i * 0.45)
            basin = 0.6 * curvature * xi**2
            
            # Stronger embedded saddle point with variable strength and frequency
            saddle_strength = 1.0 + 0.5 * np.sin(i * 0.6 + self.dim * 0.35)
            saddle_freq = 3.5 + 0.5 * np.cos(i * 0.4 + self.dim * 0.2)
            saddle = saddle_strength * xi * np.cos(saddle_freq * xi) * np.exp(-0.3 * xi**2)
            
            # Enhanced asymmetric cubic term
            asymmetry = 0.4 * np.sin(i * 0.8 + self.dim * 0.3)
            cubic = (1.0 + asymmetry) * xi**3
            
            # Improved multimodal component with stronger frequency modulation
            freq_factor = 1.2 + 0.5 * np.cos(self.dim * 0.15 + i * 0.25)
            modal_term = 0.6 * freq_factor * np.sin(6 * xi + i * 0.35)**2
            
            # Enhanced cross-dimensional interaction with stronger coupling
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling += 0.15 * np.sin(xi + x_norm[j] + 0.25 * i) * np.cos(2.5 * xi - x_norm[j] + 0.15 * j)
            
            # Enhanced dimensionally adaptive scaling factor
            scale_factor = 1.0 + 0.4 * np.sin(self.dim * 0.45 + i * 0.3)
            
            # Add all components to the result
            result += scale_factor * (basin + saddle + cubic + modal_term + coupling)
        
        # Enhanced global adaptive correction based on problem dimensionality
        global_correction = 1.0 + 0.25 * np.sin(self.dim * 0.35) + 0.15 * np.cos(self.dim * 0.25)
        
        return global_correction * result / self.dim