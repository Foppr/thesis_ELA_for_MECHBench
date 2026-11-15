import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (5, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 5)
        self.tent_map_params = np.random.uniform(0.5, 1.5, dim)
        self.sin_poly_weights = np.random.uniform(0.05, 0.2, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map interactions with enhanced parameters
        for i in range(self.dim):
            tent_val = 0.0
            for _ in range(10):  # Increased iterations for more chaos
                if x[i] < 0.5:
                    x[i] = self.tent_map_params[i] * x[i]
                else:
                    x[i] = self.tent_map_params[i] * (1 - x[i])
                tent_val += np.sin(9 * x[i]) * np.cos(5 * x[i])  # Changed frequencies
            f_val += 0.25 * tent_val  # Increased weight
        
        # Add Gaussian radial basis functions with more centers and stronger influence
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.4 * np.exp(-self.rbf_widths[i] * dist) * np.sin(4 * np.sum(x - self.rbf_centers[i]))  # Increased weight and frequency
        
        # Add asymmetric sine-polynomial terms with higher exponents
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += self.sin_poly_weights[i] * (x[i]**5) * np.sin(6 * x[i]) + 0.1 * (x[i]**7) * np.cos(4 * x[i])  # Changed exponents and weights
            else:
                f_val += 0.1 * (x[i]**6) * np.cos(7 * x[i]) + 0.12 * (x[i]**8) * np.sin(3 * x[i])  # Changed exponents and weights
        
        # Add cross-variable interaction terms with stronger chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic modulation factor based on tent map
                mod_factor = np.sin(5 * x[i]) * np.cos(4 * x[j])  # Changed frequencies
                f_val += 0.3 * np.sin(5 * x[i]) * np.cos(6 * x[j]) * mod_factor * np.exp(-0.2 * (x[i] - x[j])**2)  # Increased weight and changed exp
        
        # Add a global chaotic modulation based on sum of squares with higher frequency
        norm_sq = np.sum(x**2)
        f_val += 0.2 * np.sin(1.2 * norm_sq) * np.cos(0.8 * norm_sq) * np.exp(-0.1 * norm_sq)  # Increased weight and changed parameters
        
        # Add a high-frequency oscillatory component
        f_val += 0.15 * np.sin(10 * np.sum(x)) * np.cos(8 * np.sum(x**2))
        
        return f_val