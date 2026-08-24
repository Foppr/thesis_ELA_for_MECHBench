import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for chaos
        np.random.seed(42)
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        self.exponents = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with chaotic coefficients
        f_val = np.sum(self.coeffs * np.exp(-self.freqs * np.abs(x)))
        
        # Polynomial interactions with varying exponents
        for i in range(self.dim):
            f_val += x[i]**self.exponents[i]
            
        # Cross-dimensional sinusoidal modulations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.5 * np.sin(self.freqs[i] * x[i] + self.freqs[j] * x[j]) * \
                         np.cos(0.5 * x[i] * x[j])
                
        # Add a chaotic logistic map component
        logistic_seq = 0.0
        r = 3.9  # Chaos parameter
        x_log = 0.5  # Initial value
        for _ in range(self.dim):
            x_log = r * x_log * (1 - x_log)
            logistic_seq += x_log
            
        f_val += 0.1 * logistic_seq * np.sum(x**2)
        
        # Add noise to increase ruggedness
        noise = np.random.normal(0, 0.05, self.dim)
        f_val += np.sum(noise * np.sin(x))
        
        return f_val