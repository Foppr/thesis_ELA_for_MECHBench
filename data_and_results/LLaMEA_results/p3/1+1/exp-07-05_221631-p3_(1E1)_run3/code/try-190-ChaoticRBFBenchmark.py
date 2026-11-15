import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for chaotic behavior
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        self.saddle_positions = np.random.uniform(-5.0, 5.0, dim)
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        self.exponential_decay = np.random.uniform(0.1, 0.5, dim)
        self.asymmetry_factor = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component
        exp_decay = np.sum(self.exponential_decay * np.exp(-self.exponential_decay * np.abs(x)))
        
        # Radial Basis Functions
        rbf_sum = 0.0
        for i in range(10):
            diff = x - self.rbf_centers[:, i]
            rbf_sum += np.exp(-0.5 * np.sum((diff**2) / (self.rbf_widths[i]**2)))
        
        # Chaotic sinusoidal modulation
        chaotic_mod = np.sum(self.chaotic_params * np.sin(np.pi * x) * np.cos(2 * np.pi * x))
        
        # Asymmetric saddle points
        saddle_sum = 0.0
        for i in range(self.dim):
            pos_diff = x[i] - self.saddle_positions[i]
            asym_term = pos_diff * np.exp(-0.5 * pos_diff**2)
            saddle_sum += self.saddle_strengths[i] * asym_term * np.sin(self.asymmetry_factor[i] * x[i])
        
        # Combined fitness
        f_val = exp_decay + rbf_sum + chaotic_mod + saddle_sum
        
        # Add a global minimum bias
        f_val += 0.1 * np.sum(x**4)
        
        return f_val