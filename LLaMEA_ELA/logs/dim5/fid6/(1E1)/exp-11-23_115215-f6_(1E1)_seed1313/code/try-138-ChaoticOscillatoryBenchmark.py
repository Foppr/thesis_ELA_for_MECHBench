import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 15.0, dim)
        self.chaotic_params = np.random.uniform(3.8, 3.99, dim)
        self.rbf_centers = np.random.uniform(-4.0, 4.0, dim)
        self.rbf_widths = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with complex sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.7)) * \
                (1.0 + 0.2 * np.cos(np.prod(x) * 0.3))
        
        # Enhanced sinusoidal oscillations with higher harmonics
        for i in range(self.dim):
            f_val += 0.8 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.4) + \
                     0.5 * np.sin(self.frequencies[i] * x[i] * 3.0) + \
                     0.3 * np.cos(self.frequencies[i] * x[i] * 1.5)
        
        # Exponential radial basis functions with dynamic parameters
        for i in range(self.dim):
            center = self.rbf_centers[i] * np.sin(i * 0.6 + np.sum(x) * 0.2)
            width = self.rbf_widths[i] * (1.0 + 0.3 * np.cos(i * 0.4))
            f_val += 0.6 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.8)) * \
                     (1.0 + 0.1 * np.cos(x[i] * 0.5))
        
        # Chaotic perturbations with higher sensitivity
        chaotic_val = x[0] if self.dim > 0 else 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.3 * np.sin(chaotic_val * 15 + i) * \
                     np.cos(chaotic_val * 12 + i) + \
                     0.1 * np.tan(chaotic_val * 8 + i)
        
        # Enhanced coupling terms with polynomial decay
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = np.exp(-0.5 * (j - i)**2) * np.sin(x[i] + x[j]) * \
                           np.cos(x[i] - x[j])
                f_val += 0.4 * coupling * (x[i]**3 + x[j]**3)
        
        # High-order polynomial interactions with cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * (x[i]**4) * (x[j]**3) + \
                         0.15 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric cross-terms with enhanced chaos
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.3 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.15 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         np.exp(-0.2 * np.abs(x[i]))
        
        # Final chaotic modulation with global interaction
        f_val += 0.4 * np.sin(np.sum(np.sin(x))) + \
                 0.2 * np.cos(np.prod(np.cos(x))) + \
                 0.15 * np.sin(np.sum(np.abs(x)) * 0.7) * \
                 np.exp(-0.3 * np.sum(x**2))
        
        # Add a complex multi-modal component
        for i in range(self.dim):
            f_val += 0.25 * (np.sin(20 * x[i]) + np.cos(15 * x[i])) * \
                     np.exp(-0.5 * (x[i] - 2.5)**2)
        
        return f_val