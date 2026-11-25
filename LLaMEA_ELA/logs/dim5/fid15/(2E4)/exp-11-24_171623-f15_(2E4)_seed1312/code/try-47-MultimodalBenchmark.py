import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis functions with varying widths
        rbf_term = 0
        for i in range(self.dim):
            rbf_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    rbf_sum += np.exp(-10 * distance**2) * np.cos(5 * np.pi * (x_norm[i] + x_norm[j]))
            rbf_term += rbf_sum
            
        # Modified quaternion-inspired interactions
        quat_term = 0
        for i in range(0, self.dim - 3, 4):
            if i + 3 < self.dim:
                quat_term += (np.sin(x_norm[i]) * np.cos(x_norm[i+1]) * 
                             np.sin(x_norm[i+2]) * np.cos(x_norm[i+3])) * \
                            np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2 + x_norm[i+2]**2 + x_norm[i+3]**2))
        
        # Increased polynomial chaos terms with higher-order interactions
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x_norm[i]**5 - 3*x_norm[i]**3 + 2*x_norm[i]) * np.sin(2*np.pi*x_norm[i])
            
        # Cross-dimensional coupling with sine-cosine interactions
        coupling_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                coupling_term += np.sin(np.pi * x_norm[i]) * np.cos(np.pi * x_norm[i+1]) * \
                               (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Combined result with dynamic weighting
        weight1, weight2, weight3, weight4 = 0.25, 0.3, 0.2, 0.25
        result = weight1 * rbf_term + weight2 * quat_term + weight3 * poly_term + weight4 * coupling_term
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.05 * np.sum(x_norm ** 2)
        
        return result