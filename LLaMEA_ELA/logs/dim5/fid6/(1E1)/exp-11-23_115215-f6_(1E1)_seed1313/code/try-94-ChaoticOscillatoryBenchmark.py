import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 15.0, dim)
        self.chaotic_params = np.random.uniform(3.8, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.7))
        
        # Enhanced sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.8 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.4) + \
                     0.5 * np.sin(self.frequencies[i] * x[i] * 3.0)
        
        # Enhanced radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.6 + np.sum(x) * 0.15)
            width = 0.7 + 0.3 * np.cos(i * 0.4)
            f_val += 0.6 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.8))
        
        # Chaotic perturbations using logistic maps with enhanced coupling
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.4 * np.sin(chaotic_val * 12 + i) * \
                     np.cos(chaotic_val * 9 + i)
        
        # Enhanced coupling terms with exponential decay and additional cross-terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = np.exp(-0.4 * (j - i)) * np.sin(x[i] + x[j]) * \
                          np.cos(x[i] - x[j])
                f_val += 0.35 * coupling * (x[i]**2 + x[j]**2)
        
        # High-order polynomial interactions with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * (x[i]**4) * (x[j]**3) + \
                         0.15 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric cross-terms with chaotic modulation and additional non-linearity
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.3 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.15 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         np.exp(-0.2 * np.abs(x[i]))
        
        # Final chaotic modulation with global interaction and additional complexity
        f_val += 0.5 * np.sin(np.sum(np.sin(x))) + \
                 0.3 * np.cos(np.prod(np.cos(x))) + \
                 0.2 * np.sin(np.sum(np.abs(x)) * 0.7) + \
                 0.1 * np.exp(-0.5 * np.sum((x - np.mean(x))**2))
        
        return f_val