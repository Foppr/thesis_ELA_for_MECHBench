import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (5, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 5)
        self.tent_map_params = np.random.uniform(0.3, 1.7, dim)
        self.poly_coeffs = np.random.uniform(-0.1, 0.1, (3, dim))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = 0.5 * np.sum(x**2)
        
        # Enhanced chaotic tent map interactions with multiple iterations
        for i in range(self.dim):
            tent_val = 0.0
            x_temp = x[i]
            for _ in range(8):  # More iterations for stronger chaos
                if x_temp < 0.5:
                    x_temp = self.tent_map_params[i] * x_temp
                else:
                    x_temp = self.tent_map_params[i] * (1 - x_temp)
                tent_val += np.sin(7 * x_temp) * np.cos(4 * x_temp) + 0.5 * np.sin(11 * x_temp)
            f_val += 0.2 * tent_val
        
        # Multiple Gaussian radial basis functions with different configurations
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            width = self.rbf_widths[i]
            f_val += 0.3 * np.exp(-width * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i])) * np.cos(2 * np.sum(x - self.rbf_centers[i]))
        
        # Complex asymmetric polynomial terms with multiple degrees
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += (0.1 * x[i]**4 * np.sin(5 * x[i]) + 
                         0.05 * x[i]**6 * np.cos(3 * x[i]) + 
                         0.02 * x[i]**8 * np.sin(2 * x[i]))
            else:
                f_val += (0.08 * x[i]**5 * np.cos(6 * x[i]) + 
                         0.04 * x[i]**7 * np.sin(4 * x[i]) + 
                         0.03 * x[i]**9 * np.cos(1.5 * x[i]))
        
        # Cross-variable interaction terms with higher-order chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                # Use a more complex chaotic modulation factor
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.3 * np.sin(2 * x[i]) * np.cos(5 * x[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Global chaotic modulation with multiple frequencies
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * norm_sq) * np.exp(-0.03 * norm_sq) + \
                 0.08 * np.sin(1.2 * norm_sq) * np.cos(0.9 * norm_sq) * np.exp(-0.02 * norm_sq)
        
        # Add a high-frequency oscillatory component to increase ruggedness
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(20 * x[i]) * np.cos(15 * x[i])
        f_val += 0.1 * oscillation
        
        return f_val