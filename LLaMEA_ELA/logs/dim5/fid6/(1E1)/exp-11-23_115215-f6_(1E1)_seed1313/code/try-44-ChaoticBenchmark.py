import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.r = 3.99  # Logistic map parameter for chaos
        self.sigma = 0.1
        self.alpha = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic component using logistic map dynamics
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Use a portion of the input as seed for logistic map
            seed = (x[i] + 5.0) / 10.0  # Normalize to [0,1]
            # Apply logistic map iteratively
            chaotic_val = seed
            for _ in range(20):  # Iterate enough times to reach chaos
                chaotic_val = self.r * chaotic_val * (1 - chaotic_val)
            chaotic_sum += chaotic_val
        
        f_val += 0.5 * chaotic_sum
        
        # Add radial basis function components with varying centers and widths
        centers = np.linspace(-5, 5, min(10, self.dim))
        widths = np.logspace(-2, 1, min(10, self.dim))
        
        for i in range(min(10, self.dim)):
            rbf_val = np.exp(-0.5 * np.sum(((x - centers[i]) / widths[i])**2))
            f_val += 0.3 * rbf_val
            
        # Introduce asymmetric coupling terms
        asym_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_term = (x[i]**2) * np.sin(x[j]) + (x[j]**3) * np.cos(x[i])
                asym_sum += asym_term * np.exp(-0.1 * (i + j))
        f_val += 0.2 * asym_sum
        
        # Add a non-convex penalty using inverse distance to multiple global minima
        global_mins = np.random.uniform(-4, 4, (5, self.dim))
        penalty = 0.0
        for gmin in global_mins:
            dist = np.sqrt(np.sum((x - gmin)**2))
            penalty += 1.0 / (dist + 0.1)  # Avoid division by zero
        f_val += 0.4 * penalty
        
        # Add high-frequency oscillatory behavior with amplitude modulation
        freq_mod = 0.0
        for i in range(self.dim):
            mod_term = np.sin(20 * x[i]) * np.cos(15 * x[i])
            freq_mod += mod_term * (1 + 0.2 * np.sin(7 * x[i]))
        f_val += 0.3 * freq_mod
        
        # Add a final exponential interaction term
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        f_val += 0.1 * exp_interaction
        
        return f_val