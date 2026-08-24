import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (4, dim))
        self.rbf_widths = np.random.uniform(0.2, 1.8, 4)
        self.tent_map_params = np.random.uniform(0.6, 1.4, dim)
        self.poly_coeffs = np.random.uniform(-0.1, 0.1, (dim, 3))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with slight modification
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
                tent_val += np.sin(7 * x_temp) * np.cos(4 * x_temp) + 0.1 * np.sin(13 * x_temp)
            f_val += 0.12 * tent_val
        
        # Modified Gaussian radial basis functions with more diverse centers
        for i in range(4):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i]) + 0.5 * i)
        
        # Enhanced asymmetric sine-polynomial terms with different exponents
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.1 * (x[i]**3.5) * np.sin(5 * x[i]) + 0.08 * (x[i]**4.5) * np.cos(3 * x[i])
            else:
                f_val += 0.09 * (x[i]**3.8) * np.cos(6 * x[i]) + 0.07 * (x[i]**5.2) * np.sin(2 * x[i])
        
        # Improved cross-variable interaction terms with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling for complexity control
                # Use a chaotic modulation factor based on multiple variables
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.2 * np.sin(2 * x[i] + x[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Global chaotic modulation with higher frequency components
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.9 * norm_sq) * np.cos(0.6 * norm_sq) * np.exp(-0.03 * norm_sq) + 0.05 * np.sin(1.2 * norm_sq)
        
        # Add a small noise component to increase ruggedness
        noise = 0.01 * np.sum(np.sin(10 * x) * np.cos(8 * x))
        f_val += noise
        
        return f_val