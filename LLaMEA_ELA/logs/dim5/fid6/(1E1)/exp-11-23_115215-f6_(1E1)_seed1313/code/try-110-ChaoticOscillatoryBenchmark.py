import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 12.0, dim)
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.4))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.6 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.3) + \
                     0.4 * np.sin(self.frequencies[i] * x[i] * 1.8)
        
        # Radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.6 + np.sum(x) * 0.12)
            width = 0.6 + 0.4 * np.cos(i * 0.35)
            f_val += 0.5 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.15 * np.sin(i * 0.75))
        
        # Chaotic perturbations using logistic maps
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.25 * np.sin(chaotic_val * 12 + i) * \
                     np.cos(chaotic_val * 8 + i)
        
        # Enhanced coupling terms with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.4 * (j - i)) * np.sin(x[i] + x[j])
                f_val += 0.3 * coupling * (x[i]**2 + x[j]**2)
        
        # Modified high-order polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * (x[i]**4) * (x[j]**2) + \
                         0.08 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric cross-terms with enhanced chaotic modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.25 * (diff**3 + 0.4 * np.abs(diff)**2) + \
                         0.15 * np.sin(x[i]) * np.cos(x[i-1])
        
        # Final enhanced chaotic modulation with global interaction
        f_val += 0.35 * np.sin(np.sum(np.sin(x))) + \
                 0.2 * np.cos(np.prod(np.cos(x))) + \
                 0.12 * np.sin(np.sum(np.abs(x)) * 0.6)
        
        return f_val