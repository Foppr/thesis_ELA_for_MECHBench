import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(2.0, 15.0, dim)
        self.chaotic_params = np.random.uniform(3.8, 4.0, dim)
        # Additional chaotic sequence for more complexity
        self.chaotic_sequence = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.7))
        
        # Enhanced sinusoidal oscillations with phase shifts and amplitudes
        for i in range(self.dim):
            f_val += 0.8 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.4) + \
                     0.5 * np.sin(self.frequencies[i] * x[i] * 3.0) + \
                     0.2 * np.cos(self.frequencies[i] * x[i] * 1.5)
        
        # Enhanced radial basis functions with time-varying centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.6 + np.sum(x) * 0.2) + \
                     1.5 * np.cos(i * 0.4)
            width = 0.7 + 0.3 * np.sin(i * 0.5)
            f_val += 0.6 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.8))
        
        # Chaotic perturbations using logistic maps with feedback
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.4 * np.sin(chaotic_val * 15 + i * 0.7) * \
                     np.cos(chaotic_val * 12 + i * 0.5)
        
        # Enhanced coupling terms with exponential decay and interaction weights
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = np.exp(-0.4 * (j - i)) * np.sin(x[i] + x[j]) * \
                           np.cos(x[i] - x[j])
                f_val += 0.3 * coupling * (x[i]**2 + x[j]**2 + 0.5 * x[i] * x[j])
        
        # High-order polynomial interactions with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * (x[i]**4) * (x[j]**3) + \
                         0.15 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         np.sin(np.sum(x))
        
        # Asymmetric cross-terms with enhanced chaotic modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.3 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.2 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         np.sin(np.sum(x))
        
        # Final chaotic modulation with global interaction and higher-order terms
        f_val += 0.5 * np.sin(np.sum(np.sin(x))) + \
                 0.3 * np.cos(np.prod(np.cos(x))) + \
                 0.2 * np.sin(np.sum(np.abs(x)) * 0.7) + \
                 0.1 * np.cos(np.sum(x**3))
        
        # Add a complex interaction term between all dimensions
        f_val += 0.25 * np.prod(np.sin(x + 0.5)) * \
                 np.sum(np.exp(-0.1 * (x - 1.0)**2))
        
        return f_val