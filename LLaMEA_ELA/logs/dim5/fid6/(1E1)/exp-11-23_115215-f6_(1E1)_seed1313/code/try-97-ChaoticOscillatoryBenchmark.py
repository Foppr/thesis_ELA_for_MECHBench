import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 10.0, dim)
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.2 * np.sin(np.sum(x) * 0.5))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.5 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.3) + \
                     0.3 * np.sin(self.frequencies[i] * x[i] * 2.0)
        
        # Radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.5 + np.sum(x) * 0.1)
            width = 0.5 + 0.5 * np.cos(i * 0.3)
            f_val += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.1 * np.sin(i * 0.7))
        
        # Chaotic perturbations using logistic maps
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.2 * np.sin(chaotic_val * 10 + i) * \
                     np.cos(chaotic_val * 7 + i)
        
        # Coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.exp(-0.3 * (j - i)) * np.sin(x[i] + x[j])
                f_val += 0.25 * coupling * (x[i]**2 + x[j]**2)
        
        # High-order polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (x[i]**3) * (x[j]**2) + \
                         0.05 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric cross-terms with chaotic modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.2 * (diff**3 + 0.3 * np.abs(diff)**2) + \
                         0.1 * np.sin(x[i]) * np.cos(x[i-1])
        
        # Final chaotic modulation with global interaction
        f_val += 0.3 * np.sin(np.sum(np.sin(x))) + \
                 0.15 * np.cos(np.prod(np.cos(x))) + \
                 0.1 * np.sin(np.sum(np.abs(x)) * 0.5)
        
        return f_val