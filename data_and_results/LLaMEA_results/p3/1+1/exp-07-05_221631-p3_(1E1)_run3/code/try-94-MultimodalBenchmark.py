import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Additional random scaling for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
        # Chaotic parameters for enhanced complexity
        self.chaos_factor = 3.8
        self.interference_strength = 1.5
        self.hierarchical_scale = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add chaotic sine-wave perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 6.0 * np.sin(self.chaos_factor * x_transformed[i] + 
                                  2.0 * np.sin(3.0 * x_transformed[i])) * \
                     np.cos(3.5 * x_transformed[i] + 
                            1.5 * np.cos(2.5 * x_transformed[i])) + \
                     3.0 * np.sin(6.0 * x_transformed[i] + 
                                  1.2 * np.sin(4.0 * x_transformed[i]))
            
        # Add complex interaction terms between dimensions with higher-order and chaotic coupling
        for i in range(self.dim - 2):
            f_val += self.interference_strength * x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * \
                     (np.sin(0.8 * x_transformed[i] + 0.5 * np.sin(2.0 * x_transformed[i])) + 
                      np.cos(0.9 * x_transformed[i+1] + 0.6 * np.cos(1.8 * x_transformed[i+1])) + 
                      np.sin(1.1 * x_transformed[i+2] + 0.4 * np.sin(3.0 * x_transformed[i+2])))
            
        # Add a hierarchical perturbed quartic term with chaotic modulation for increased complexity
        f_val += self.hierarchical_scale * np.sum((x_transformed**4) * (1.0 + 0.3 * np.sin(6.0 * x_transformed)) * 
                                                   (1.0 + 0.2 * np.cos(4.0 * x_transformed)))
        
        # Add cross-dimensional interference patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i + 3:  # Only nearby dimensions interact
                    f_val += 0.5 * np.sin(2.0 * (x_transformed[i] + x_transformed[j])) * \
                             np.cos(1.5 * (x_transformed[i] - x_transformed[j]))
        
        # Add a highly oscillatory chaotic term to increase ruggedness
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * x_transformed[i] + 
                                   3.0 * np.sin(7.0 * x_transformed[i]) + 
                                   2.0 * np.cos(5.0 * x_transformed[i]))
        f_val += 0.8 * chaotic_term**2
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.2
        
        return f_val