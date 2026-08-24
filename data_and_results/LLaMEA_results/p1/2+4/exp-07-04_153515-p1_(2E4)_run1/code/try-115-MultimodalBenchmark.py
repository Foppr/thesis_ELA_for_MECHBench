import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (4, dim))
        self.rbf_widths = np.random.uniform(0.2, 1.8, 4)
        self.tent_map_params = np.random.uniform(0.6, 1.4, dim)
        self.sine_poly_coeffs = np.random.uniform(0.05, 0.15, (dim, 2))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = 0.8 * np.sum(x**2)
        
        # Enhanced chaotic tent map interactions with multiple iterations
        for i in range(self.dim):
            tent_val = 0.0
            x_temp = x[i]
            for _ in range(7):  # Increased iterations for more chaos
                if x_temp < 0.5:
                    x_temp = self.tent_map_params[i] * x_temp
                else:
                    x_temp = self.tent_map_params[i] * (1 - x_temp)
                tent_val += np.sin(7 * x_temp) * np.cos(4 * x_temp)
            f_val += 0.12 * tent_val
        
        # Enhanced Gaussian radial basis functions with more centers
        for i in range(4):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i]))
        
        # Improved asymmetric sine-polynomial terms with different exponents
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += self.sine_poly_coeffs[i, 0] * (x[i]**3.5) * np.sin(5 * x[i]) + \
                         self.sine_poly_coeffs[i, 1] * (x[i]**4.5) * np.cos(3 * x[i])
            else:
                f_val += self.sine_poly_coeffs[i, 0] * (x[i]**4.2) * np.cos(6 * x[i]) + \
                         self.sine_poly_coeffs[i, 1] * (x[i]**5.8) * np.sin(2.5 * x[i])
        
        # Enhanced cross-variable interaction terms with higher frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.3 * np.sin(2 * x[i]) * np.cos(5 * x[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Global chaotic modulation with higher frequency components
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * norm_sq) * np.exp(-0.08 * norm_sq)
        
        # Add a small noise component to increase ruggedness
        noise = 0.02 * np.sum(np.sin(10 * x) * np.cos(8 * x))
        f_val += noise
        
        return f_val