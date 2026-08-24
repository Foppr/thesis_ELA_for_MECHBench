import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (3, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.5, 3)
        self.tent_map_params = np.random.uniform(0.5, 1.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map interactions
        for i in range(self.dim):
            tent_val = 0.0
            for _ in range(5):  # Iterate tent map 5 times for chaos
                if x[i] < 0.5:
                    x[i] = self.tent_map_params[i] * x[i]
                else:
                    x[i] = self.tent_map_params[i] * (1 - x[i])
                tent_val += np.sin(5 * x[i]) * np.cos(3 * x[i])
            f_val += 0.1 * tent_val
        
        # Add Gaussian radial basis functions with different centers and widths
        for i in range(3):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.25 * np.exp(-self.rbf_widths[i] * dist) * np.sin(2 * np.sum(x - self.rbf_centers[i]))
        
        # Add asymmetric sine-polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.08 * (x[i]**3) * np.sin(4 * x[i]) + 0.04 * (x[i]**5) * np.cos(2 * x[i])
            else:
                f_val += 0.06 * (x[i]**4) * np.cos(5 * x[i]) + 0.05 * (x[i]**6) * np.sin(1.5 * x[i])
        
        # Add cross-variable interaction terms with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic modulation factor based on tent map
                mod_factor = np.sin(3 * x[i]) * np.cos(2 * x[j])
                f_val += 0.15 * np.sin(3 * x[i]) * np.cos(4 * x[j]) * mod_factor * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a global chaotic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.1 * np.sin(0.7 * norm_sq) * np.cos(0.4 * norm_sq) * np.exp(-0.05 * norm_sq)
        
        return f_val