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
            # Chaotic modulation of quadratic terms with altered coefficients
            chaotic_factor = 1.0 + 0.5 * np.sin(7 * x_norm[i]) * np.cos(5 * x_norm[i])
            result += chaotic_factor * (x_norm[i]**2) * (1.0 + 0.4 * np.sin(13 * x_norm[i]))
        
        # Enhanced saddle points with increased curvature variation
        saddle_term = 0.0
        for i in range(self.dim):
            # More complex saddle point regions
            curvature = 1.0 + 0.7 * np.sin(3.0 * x_norm[i]) * np.cos(4.0 * x_norm[i])
            saddle_term += curvature * (x_norm[i]**4) - 2.0 * (x_norm[i]**2)
        
        # Modified dimensionality coupling with different interaction weights
        coupling = 0.0
        for i in range(self.dim):
            dim_weight = 1.0 + 0.5 * np.sin(4 * x_norm[i])
            for j in range(i+1, self.dim):
                # Altered interaction based on normalized coordinates
                interaction = np.exp(-0.2 * (x_norm[i] - x_norm[j])**2) * \
                             np.sin(8 * (x_norm[i] + x_norm[j]))
                coupling += dim_weight * interaction
        
        # Modified high-frequency oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15 + 5 * np.sin(3.0 * x_norm[i])
            oscillatory += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.7)
        
        # Global scaling factor with different proximity sensitivity
        global_scale = 1.0 + 0.4 * np.exp(-0.3 * np.sum(x_norm**2))
        
        return global_scale * (result + 0.7 * saddle_term + 0.5 * coupling + 0.4 * oscillatory)