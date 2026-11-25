import numpy as np

class QuaternionExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Quaternion-based rotational symmetry with exponential decay
            rot_sym = np.sin(xi * 2.0) * np.cos(xi * 3.0) + \
                     np.cos(xi * 2.0) * np.sin(xi * 3.0) + \
                     0.5 * (np.sin(xi * 4.0) * np.cos(xi * 5.0) - 
                            np.cos(xi * 4.0) * np.sin(xi * 5.0))
            
            # Exponential decay interference patterns with dynamic scaling
            exp_decay = np.exp(-abs(xi) * (1.0 + 0.3 * np.sin(7 * xi))) * \
                       (1.0 + 0.4 * np.cos(11 * xi**2))
            
            # Dynamic conditioning factor with adaptive coupling
            cond_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3 + i * 0.2) * \
                         np.cos(self.dim * 0.4 + i * 0.15)
            
            # Multi-scale exponential modulation with cross-dimensional coupling
            coupling_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling_term = np.exp(-abs(xi - x_norm[j]) * (1.5 + 0.2 * np.sin(i+j))) * \
                                   np.cos((xi + x_norm[j]) * 2.0)
                    coupling_sum += coupling_term / (1.0 + abs(xi - x_norm[j])**1.5)
            
            # Modified exponential gradient modulation
            grad_mod = 0.3 * np.exp(-abs(xi) * 2.0) * np.sin(13 * xi) + \
                      0.2 * np.exp(-abs(xi**2) * 1.5) * np.cos(9 * xi) + \
                      0.1 * np.exp(-abs(xi**3) * 1.2) * np.sin(17 * xi)
            
            # Enhanced exponential basin boundary
            basin_boundary = 1.0 + 0.6 * np.exp(-abs(xi) * 3.0) * np.cos(8 * xi) + \
                           0.3 * np.exp(-abs(xi**2) * 2.5) * np.sin(6 * xi) + \
                           0.15 * np.exp(-abs(xi**3) * 2.0) * np.cos(4 * xi)
            
            # Final contribution for this dimension
            term = cond_factor * (basin_boundary * (xi**2 + rot_sym * exp_decay + coupling_sum + grad_mod)**2)
            result += term
            
        # Global exponential scaling with quaternion-based correction
        global_scale = 1.0 + 0.4 * np.exp(-self.dim * 0.2) * np.sin(self.dim * 0.5) + \
                      0.3 * np.exp(-self.dim * 0.15) * np.cos(self.dim * 0.3) + \
                      0.2 * np.exp(-self.dim * 0.1) * np.sin(self.dim * 0.4)
        
        # Global exponential coupling term
        global_coupling = 0.25 * np.exp(-abs(np.sum(x_norm)) * 0.5) * np.cos(np.mean(x_norm) * 3.0) + \
                         0.15 * np.exp(-abs(np.std(x_norm)) * 0.7) * np.sin(np.var(x_norm) * 2.0)
        
        return global_scale * (result / self.dim + global_coupling)