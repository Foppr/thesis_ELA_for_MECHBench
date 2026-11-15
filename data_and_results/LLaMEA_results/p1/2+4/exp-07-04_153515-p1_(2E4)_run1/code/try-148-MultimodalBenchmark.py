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
        
        # Add chaotic tent map interactions with enhanced dynamics
        for i in range(self.dim):
            tent_val = 0.0
            x_temp = x[i]
            for _ in range(10):  # Increased iterations for more chaos
                if x_temp < 0.5:
                    x_temp = self.tent_map_params[i] * x_temp
                else:
                    x_temp = self.tent_map_params[i] * (1 - x_temp)
                tent_val += np.sin(9 * x_temp) * np.cos(5 * x_temp)  # Changed frequencies
            f_val += 0.2 * tent_val  # Increased weight
        
        # Add Gaussian radial basis functions with different centers and widths
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.4 * np.exp(-self.rbf_widths[i] * dist) * np.sin(4 * np.sum(x - self.rbf_centers[i]))  # Increased weight and frequency
        
        # Add asymmetric sine-polynomial terms with modified exponents and weights
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += self.sin_poly_weights[i] * (x[i]**5) * np.sin(6 * x[i]) + 0.08 * (x[i]**7) * np.cos(4 * x[i])  # Changed exponents and weights
            else:
                f_val += 0.09 * (x[i]**6) * np.cos(7 * x[i]) + 0.1 * (x[i]**8) * np.sin(3 * x[i])  # Changed exponents and weights
        
        # Add cross-variable interaction terms with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic modulation factor based on tent map
                mod_factor = np.sin(5 * x[i]) * np.cos(4 * x[j])  # Changed frequencies
                f_val += 0.25 * np.sin(5 * x[i]) * np.cos(6 * x[j]) * mod_factor * np.exp(-0.2 * (x[i] - x[j])**2)  # Increased weight and changed exp
        
        # Add a global chaotic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.2 * np.sin(1.0 * norm_sq) * np.cos(0.6 * norm_sq) * np.exp(-0.1 * norm_sq)  # Increased weight and changed parameters
        
        # Add a novel hyperbolic tangent interaction term
        tanh_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tanh_term += np.tanh(x[i] + x[j]) * np.sin(3 * (x[i] - x[j]))
        f_val += 0.15 * tanh_term
        
        # Add a high-frequency oscillation component
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(20 * x[i]) * np.cos(15 * x[i])
        f_val += 0.1 * freq_term
        
        return f_val