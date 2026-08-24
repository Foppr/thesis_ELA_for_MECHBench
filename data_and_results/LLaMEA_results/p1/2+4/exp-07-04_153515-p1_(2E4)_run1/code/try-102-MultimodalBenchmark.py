import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random parameters for reproducibility
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5, 5, (5, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.0, 5)
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        self.time_varying_centers = np.random.uniform(-5, 5, (10, dim))
        self.time_varying_widths = np.random.uniform(0.1, 1.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic logistic map interactions
        for i in range(self.dim):
            logistic_val = 0.0
            x_temp = x[i]
            for _ in range(10):  # Iterate logistic map 10 times for stronger chaos
                x_temp = self.logistic_params[i] * x_temp * (1 - x_temp)
                logistic_val += np.sin(7 * x_temp) * np.cos(5 * x_temp)
            f_val += 0.15 * logistic_val
        
        # Add multiple Gaussian radial basis functions with time-varying parameters
        for i in range(5):
            dist = np.sum((x - self.rbf_centers[i])**2)
            f_val += 0.3 * np.exp(-self.rbf_widths[i] * dist) * np.cos(3 * np.sum(x - self.rbf_centers[i]))
        
        # Add time-varying Gaussian components
        for i in range(10):
            dist = np.sum((x - self.time_varying_centers[i])**2)
            f_val += 0.1 * np.exp(-self.time_varying_widths[i] * dist) * np.sin(4 * np.sum(x - self.time_varying_centers[i]))
        
        # Add asymmetric trigonometric-polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.1 * (x[i]**4) * np.sin(5 * x[i]) + 0.05 * (x[i]**6) * np.cos(3 * x[i])
            else:
                f_val += 0.09 * (x[i]**5) * np.cos(6 * x[i]) + 0.07 * (x[i]**7) * np.sin(2 * x[i])
        
        # Add cross-variable interaction terms with time-varying chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a time-varying chaotic modulation factor
                mod_factor = np.sin(4 * x[i]) * np.cos(3 * x[j]) + 0.1 * np.sin(2 * x[i] + x[j])
                f_val += 0.2 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * mod_factor * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Add a global time-varying chaotic modulation based on sum of squares
        norm_sq = np.sum(x**2)
        f_val += 0.15 * np.sin(0.8 * norm_sq) * np.cos(0.5 * norm_sq) * np.exp(-0.08 * norm_sq)
        
        # Add a high-frequency chaotic modulation term
        freq_mod = 0.0
        for i in range(self.dim):
            freq_mod += np.sin(10 * x[i]) * np.cos(8 * x[i])
        f_val += 0.05 * freq_mod * np.exp(-0.1 * norm_sq)
        
        return f_val