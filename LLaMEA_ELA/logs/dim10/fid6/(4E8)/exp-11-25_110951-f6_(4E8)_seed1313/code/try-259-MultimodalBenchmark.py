import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic quadratic potential with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            # Chaotic modulation of quadratic terms
            chaotic_factor = 1.0 + 0.3 * np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i])
            result += chaotic_factor * (x_norm[i]**2) * (1.0 + 0.2 * np.sin(13 * x_norm[i]))
        
        # Embedded saddle points with varying curvature
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle point regions with dynamic curvature
            curvature = 1.0 + 0.5 * np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i])
            saddle_term += curvature * (x_norm[i]**4) - 2 * (x_norm[i]**2)
        
        # Adaptive dimensionality coupling with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            dim_weight = 1.0 + 0.3 * np.sin(4 * x_norm[i])
            for j in range(i+1, self.dim):
                # Dynamic interaction based on normalized coordinates
                interaction = np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                             np.sin(8 * (x_norm[i] + x_norm[j]))
                coupling += dim_weight * interaction
        
        # High-frequency oscillatory component with fractal-like structure
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(3 * x_norm[i])
            oscillatory += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Global scaling factor that adapts based on solution proximity to optima
        global_scale = 1.0 + 0.2 * np.exp(-0.5 * np.sum(x_norm**2))
        
        return global_scale * (result + 0.5 * saddle_term + 0.3 * coupling + 0.2 * oscillatory)