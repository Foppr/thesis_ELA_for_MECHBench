import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (4, dim))
        self.rbf_widths = np.random.uniform(0.2, 1.8, 4)
        self.tent_map_params = np.random.uniform(0.6, 1.4, dim)
        self.sin_poly_coeffs = np.random.uniform(0.05, 0.15, (dim, 2))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified weight
        f_val = 0.8 * np.sum(x**2)
        
        # Enhanced chaotic tent map interactions with higher sensitivity
        for i in range(self.dim):
            tent_val = 0.0
            x_temp = x[i]
            for _ in range(7):  # More iterations for stronger chaos
                if x_temp < 0.5:
                    x_temp = self.tent_map_params[i] * x_temp
                else:
                    x_temp = self.tent_map_params[i] * (1 - x_temp)
                tent_val += np.sin(7 * x_temp) * np.cos(4 * x_temp)
            f_val += 0.12 * tent_val
        
        # Modified Gaussian radial basis functions with more diverse centers
        for i in range(4):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i]))
        
        # Enhanced asymmetric sine-polynomial terms with variable coefficients
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += self.sin_poly_coeffs[i, 0] * (x[i]**3) * np.sin(5 * x[i]) + \
                         self.sin_poly_coeffs[i, 1] * (x[i]**4) * np.cos(3 * x[i])
            else:
                f_val += self.sin_poly_coeffs[i, 0] * (x[i]**5) * np.cos(4 * x[i]) + \
                         self.sin_poly_coeffs[i, 1] * (x[i]**6) * np.sin(2 * x[i])
        
        # Improved cross-variable interaction terms with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a more complex chaotic modulation factor
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.3 * np.sin(2 * x[i] + x[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Enhanced global chaotic modulation with multiple frequencies
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * norm_sq) * np.exp(-0.03 * norm_sq) + \
                 0.08 * np.sin(0.3 * norm_sq) * np.cos(0.6 * norm_sq) * np.exp(-0.02 * norm_sq)
        
        return f_val