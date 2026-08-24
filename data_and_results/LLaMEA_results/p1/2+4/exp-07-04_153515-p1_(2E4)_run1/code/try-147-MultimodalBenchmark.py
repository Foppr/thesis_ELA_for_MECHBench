import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (3, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, 3)
        self.tent_map_params = np.random.uniform(0.6, 1.4, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map interactions with modified parameters
        for i in range(self.dim):
            tent_val = 0.0
            for _ in range(7):  # Increased iterations for more chaos
                if x[i] < 0.5:
                    x[i] = self.tent_map_params[i] * x[i]
                else:
                    x[i] = self.tent_map_params[i] * (1 - x[i])
                tent_val += np.sin(7 * x[i]) * np.cos(4 * x[i])  # Changed frequencies
            f_val += 0.15 * tent_val  # Increased weight
        
        # Add Gaussian radial basis functions with different centers and widths
        for i in range(3):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.sin(3 * np.sum(x - self.rbf_centers[i]))  # Increased weight and frequency
        
        # Add asymmetric sine-polynomial terms with modified exponents
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.1 * (x[i]**4) * np.sin(5 * x[i]) + 0.06 * (x[i]**6) * np.cos(3 * x[i])  # Changed exponents and weights
            else:
                f_val += 0.07 * (x[i]**5) * np.cos(6 * x[i]) + 0.08 * (x[i]**7) * np.sin(2 * x[i])  # Changed exponents and weights
        
        # Add cross-variable interaction terms with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic modulation factor based on tent map
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j])  # Changed frequencies
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)  # Increased weight and changed exp
        
        # Add a global chaotic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * norm_sq) * np.exp(-0.08 * norm_sq)  # Increased weight and changed parameters
        
        return f_val