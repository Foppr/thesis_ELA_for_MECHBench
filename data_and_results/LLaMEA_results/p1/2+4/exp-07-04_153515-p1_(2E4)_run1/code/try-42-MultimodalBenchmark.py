import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4)
        
        # Add logarithmic modulation to create non-smooth regions
        log_term = 0.0
        for i in range(self.dim):
            log_term += 0.5 * np.log(1.0 + np.abs(x[i])) * np.sin(3 * x[i])
        f_val += log_term
        
        # Add sine-based interactions with varying frequencies
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_interaction += 0.3 * np.sin(2 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        f_val += sine_interaction
        
        # Add high-frequency oscillations to increase local optima density
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.1 * np.sin(15 * x[i])**3
        f_val += high_freq
        
        # Add a global sinusoidal modulation based on the sum of variables
        f_val += 0.1 * np.sin(0.5 * np.sum(x)) * np.cos(0.3 * np.sum(x**2))
        
        # Add a penalty term for values near boundaries to create challenging edges
        penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty += 10.0 * (np.abs(x[i]) - 4.5)**2
        f_val += penalty
        
        return f_val