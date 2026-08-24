import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (5, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 5)
        self.tent_map_params = np.random.uniform(0.3, 1.7, dim)
        self.sin_poly_coeffs = np.random.uniform(-0.1, 0.1, (dim, 4))
        self.delayed_tent_states = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map interactions with delayed states
        for i in range(self.dim):
            tent_val = 0.0
            # Update delayed state
            self.delayed_tent_states[i] = x[i]
            for _ in range(7):  # Iterate tent map 7 times for stronger chaos
                if x[i] < 0.5:
                    x[i] = self.tent_map_params[i] * x[i]
                else:
                    x[i] = self.tent_map_params[i] * (1 - x[i])
                tent_val += np.sin(7 * x[i]) * np.cos(4 * x[i])
            f_val += 0.12 * tent_val
        
        # Add Gaussian radial basis functions with more centers and time-delayed modulation
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            # Add time-delayed modulation
            delay_mod = np.sin(2 * np.sum(self.delayed_tent_states - self.rbf_centers[i]))
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * delay_mod
        
        # Add asymmetric sine-polynomial terms with higher-order powers and cross-terms
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += self.sin_poly_coeffs[i, 0] * (x[i]**4) * np.sin(5 * x[i]) + \
                         self.sin_poly_coeffs[i, 1] * (x[i]**6) * np.cos(3 * x[i]) + \
                         self.sin_poly_coeffs[i, 2] * (x[i]**3) * np.sin(2 * x[i]) * np.cos(4 * x[i])
            else:
                f_val += self.sin_poly_coeffs[i, 3] * (x[i]**5) * np.cos(6 * x[i]) + \
                         self.sin_poly_coeffs[i, 0] * (x[i]**7) * np.sin(1.5 * x[i]) + \
                         self.sin_poly_coeffs[i, 1] * (x[i]**4) * np.cos(3 * x[i]) * np.sin(5 * x[i])
        
        # Add cross-variable interaction terms with time-delayed chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity
                # Use a time-delayed chaotic modulation factor
                delay_mod = np.sin(4 * self.delayed_tent_states[i]) * np.cos(3 * self.delayed_tent_states[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * delay_mod * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Add a global chaotic modulation with multiple time-delayed components
        norm_sq = np.sum(x**2)
        delay_norm = np.sum(self.delayed_tent_states**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * delay_norm) * np.exp(-0.08 * norm_sq)
        
        # Add a novel multi-scale periodic component
        for i in range(self.dim):
            f_val += 0.05 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i]) * np.cos(4 * x[i])
        
        return f_val