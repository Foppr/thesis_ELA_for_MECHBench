import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis functions with adaptive widths
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    # Adaptive width based on dimensionality
                    width = 0.5 + 0.5 * np.sin(np.pi * (i + j) / self.dim)
                    rbf_sum += np.exp(-distance**2 / (2 * width**2))
            rbf_term += rbf_sum
        
        # Modified quaternion-inspired interactions with phase shifts
        quat_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_norm[i] - x_norm[j]
                phase = np.pi * (i + j) / self.dim
                quat_term += np.sin(diff * np.pi) * np.cos(phase) * np.exp(-0.5 * diff**2)
        
        # Increased polynomial chaos terms with higher order interactions
        poly_term = 0
        for i in range(self.dim):
            # Fourth-order polynomial with mixed interactions
            poly_term += (x_norm[i]**4 - 3*x_norm[i]**2 + 1) * np.cos(2*np.pi*x_norm[i])
            
        # Cross-dimensional coupling with cosine modulation
        coupling_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                coupling_term += np.cos(np.pi * (x_norm[i] + x_norm[i+1])) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Additional trigonometric interference patterns
        interference_term = 0
        for i in range(self.dim):
            interference_term += np.sin(3 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])
            
        # Combined result with dynamic weighting and conditioning
        weight1, weight2, weight3, weight4, weight5 = 0.25, 0.2, 0.25, 0.15, 0.15
        result = weight1 * rbf_term + weight2 * quat_term + weight3 * poly_term + weight4 * coupling_term + weight5 * interference_term
        
        # Add conditioning term to improve ill-conditioning
        condition_term = 0.01 * np.sum(x_norm**2)
        result += condition_term
        
        return result