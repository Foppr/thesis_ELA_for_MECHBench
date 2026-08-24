import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (5, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 5)
        self.tent_map_params = np.random.uniform(0.5, 1.5, dim)
        self.poly_exponents = np.random.uniform(2.0, 8.0, dim)
        self.sin_frequencies = np.random.uniform(2.0, 10.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified coefficient
        f_val = 0.8 * np.sum(x**2)
        
        # Add enhanced chaotic tent map interactions with increased iterations
        for i in range(self.dim):
            tent_val = 0.0
            for _ in range(12):  # Increased iterations for more chaos
                if x[i] < 0.5:
                    x[i] = self.tent_map_params[i] * x[i]
                else:
                    x[i] = self.tent_map_params[i] * (1 - x[i])
                tent_val += np.sin(9 * x[i]) * np.cos(6 * x[i]) + 0.5 * np.sin(12 * x[i])  # Changed frequencies and added term
            f_val += 0.25 * tent_val  # Increased weight
        
        # Add enhanced Gaussian radial basis functions with more centers and modified interaction
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.4 * np.exp(-self.rbf_widths[i] * dist) * np.sin(4 * np.sum(x - self.rbf_centers[i])) * np.cos(2 * dist)  # Increased weight, added cos term
        
        # Add enhanced asymmetric sine-polynomial terms with modified exponents and frequencies
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.15 * (x[i]**self.poly_exponents[i]) * np.sin(self.sin_frequencies[i] * x[i]) + 0.1 * (x[i]**(self.poly_exponents[i] + 1)) * np.cos(self.sin_frequencies[i] * x[i] / 2)  # Changed exponents and weights
            else:
                f_val += 0.12 * (x[i]**(self.poly_exponents[i] + 0.5)) * np.cos(self.sin_frequencies[i] * x[i]) + 0.09 * (x[i]**(self.poly_exponents[i] + 2)) * np.sin(self.sin_frequencies[i] * x[i] / 3)  # Changed exponents and weights
        
        # Add enhanced cross-variable interaction terms with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic modulation factor based on tent map and additional sine terms
                mod_factor = np.sin(5 * x[i]) * np.cos(4 * x[j]) + 0.3 * np.sin(7 * x[i]) * np.cos(5 * x[j])  # Changed frequencies and added term
                f_val += 0.3 * np.sin(5 * x[i]) * np.cos(6 * x[j]) * mod_factor * np.exp(-0.2 * (x[i] - x[j])**2)  # Increased weight and changed exp
        
        # Add enhanced global chaotic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.2 * np.sin(1.2 * norm_sq) * np.cos(0.8 * norm_sq) * np.exp(-0.12 * norm_sq) + 0.05 * np.sin(2 * norm_sq) * np.cos(1.5 * norm_sq)  # Increased weight and added term
        
        # Add a novel hyperbolic tangent modulation term
        tanh_term = np.sum(np.tanh(x))
        f_val += 0.1 * tanh_term * np.exp(-0.05 * norm_sq)  # Added new modulation
        
        return f_val