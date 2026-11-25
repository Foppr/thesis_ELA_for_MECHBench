import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.5 * np.sin(10 * x[i]) + 0.3 * np.sin(20 * x[i]) + \
                     0.2 * np.sin(40 * x[i]) + 0.1 * np.sin(80 * x[i])
        
        # Add adaptive polynomial conditioning with multi-scale exponents
        f_val += 0.1 * np.sum(x**3) + 0.05 * np.sum(x**4) + 0.02 * np.sum(x**6)
        
        # Add cross-dimensional exponential penalties with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                penalty = 0.05 * np.exp(-0.1 * (x[i] - x[j])**2) + \
                          0.03 * np.exp(-0.2 * (x[i] + x[j])**2)
                f_val += penalty
        
        # Add chaotic correlation terms with sine-wave modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term = 0.04 * np.sin(5 * x[i]) * np.cos(3 * x[j]) * \
                            np.exp(-0.02 * (x[i] - x[j])**2)
                f_val += corr_term
        
        # Add global chaotic modulation with multiple sine-wave components
        f_val += 0.2 * np.sin(0.5 * np.sum(x)) + 0.15 * np.cos(0.3 * np.sum(x)**2) + \
                 0.1 * np.sin(0.7 * np.sum(x)**3)
        
        # Add sharp gradient changes with discontinuous components
        f_val += 0.3 * np.sum(np.abs(x)) + 0.2 * np.sum(np.sqrt(np.abs(x)))
        
        return f_val