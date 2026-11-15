import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (4, dim))
        self.rbf_widths = np.random.uniform(0.2, 1.2, 4)
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic logistic map interactions
        for i in range(self.dim):
            logistic_val = 0.0
            x_log = x[i]
            for _ in range(6):  # Iterate logistic map 6 times for chaos
                x_log = self.logistic_params[i] * x_log * (1 - x_log)
                logistic_val += np.cos(4 * x_log) * np.sin(2 * x_log)
            f_val += 0.12 * logistic_val
        
        # Add multiquadratic radial basis functions with different centers and widths
        for i in range(4):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * (dist + 1) ** (-1.5) * np.cos(3 * np.sum(x - self.rbf_centers[i]))
        
        # Add asymmetric trigonometric-polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.09 * (x[i]**2.5) * np.cos(3 * x[i]) + 0.05 * (x[i]**4.5) * np.sin(1.5 * x[i])
            else:
                f_val += 0.07 * (x[i]**3.5) * np.sin(4 * x[i]) + 0.06 * (x[i]**5.5) * np.cos(2 * x[i])
        
        # Add cross-variable interaction terms with logistic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a logistic modulation factor based on logistic map
                mod_factor = np.cos(2 * x[i]) * np.sin(3 * x[j])
                f_val += 0.18 * np.cos(2 * x[i]) * np.sin(5 * x[j]) * mod_factor * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a global logistic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.cos(0.6 * norm_sq) * np.sin(0.3 * norm_sq) * np.exp(-0.03 * norm_sq)
        
        return f_val