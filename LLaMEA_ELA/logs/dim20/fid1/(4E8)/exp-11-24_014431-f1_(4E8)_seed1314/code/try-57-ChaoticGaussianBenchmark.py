import numpy as np

class ChaoticGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos generation
        self.logistic_seq = np.array([0.5])
        for _ in range(dim * 10):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Chaotic logistic map interactions with varying control parameters
        for i in range(self.dim):
            chaos_param = self.logistic_seq[i % len(self.logistic_seq)]
            f_val += 0.5 * np.sin(2 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2) + \
                     0.3 * np.cos(3 * np.pi * x[i]) * np.log(1 + np.abs(x[i]))
        
        # Multi-scale Gaussian interactions with adaptive variances
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Limited interaction scope
                sigma = 0.5 + 0.5 * np.sin(0.1 * (i + j))
                distance = np.sqrt((x[i] - x[j])**2)
                f_val += 0.4 * np.exp(-distance**2 / (2 * sigma**2)) * np.cos(2 * np.pi * (x[i] + x[j]))
        
        # Adaptive gradient modulation with dynamic conditioning
        for i in range(self.dim):
            mod_factor = 1.0 + 0.3 * np.sin(0.2 * x[i])
            f_val += 0.2 * x[i]**4 * mod_factor + 0.1 * x[i]**6 * (1 + 0.2 * np.cos(0.5 * x[i]))
        
        # Cross-dimensional polynomial coupling with dynamic exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_val = 1 + 0.5 * np.sin(0.3 * (i + j))
                f_val += 0.1 * (x[i] * x[j])**exp_val * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add noise sensitivity term with chaotic amplitude modulation
        noise_amp = np.abs(np.sin(0.1 * np.sum(x)))
        f_val += noise_amp * 0.05 * np.sum(np.sin(10 * x)**2)
        
        # Global conditioning with varying difficulty levels
        f_val += 0.02 * np.sum(x**8) + 0.01 * np.sum(np.abs(x)**10)
        
        return f_val