import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 15.0, dim)
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        self.adaptive_widths = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with sinusoidal modulation
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.7))
        
        # Enhanced sinusoidal oscillations with frequency coupling
        for i in range(self.dim):
            f_val += 0.6 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.4) + \
                     0.4 * np.sin(self.frequencies[i] * x[i] * 2.5) + \
                     0.2 * np.cos(self.frequencies[i] * x[i] * 3.0)
        
        # Advanced radial basis functions with adaptive widths and dynamic centers
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.6 + np.sum(x) * 0.15)
            width = self.adaptive_widths[i] * (0.8 + 0.4 * np.cos(i * 0.4))
            f_val += 0.5 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.6))
        
        # Coupled chaotic perturbations using logistic maps with memory
        chaotic_vals = []
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            chaotic_vals.append(chaotic_val)
            f_val += 0.3 * np.sin(chaotic_val * 12 + i) * \
                     np.cos(chaotic_val * 8 + i) + \
                     0.15 * np.tan(chaotic_val * 5 + i)
        
        # Multi-scale coupling terms with varying decay rates
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = np.exp(-0.4 * (j - i)) * np.sin(x[i] + x[j])
                f_val += 0.3 * coupling * (x[i]**2 + x[j]**2) + \
                         0.15 * np.cos(x[i] * x[j]) * np.sin(x[i] - x[j])
        
        # Complex high-order polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * (x[i]**4) * (x[j]**3) + \
                         0.15 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric cross-terms with dynamic modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.3 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.2 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         np.exp(-0.2 * np.abs(x[i] - x[i-1]))
        
        # Global interaction with multiple chaotic components
        f_val += 0.4 * np.sin(np.sum(np.sin(x))) + \
                 0.2 * np.cos(np.prod(np.cos(x))) + \
                 0.15 * np.sin(np.sum(np.abs(x)) * 0.7) + \
                 0.1 * np.tan(np.sum(x**3) * 0.05)
        
        # Add noise-like perturbations for increased complexity
        f_val += 0.05 * np.random.uniform(-1, 1) * np.sum(np.sin(x * 2))
        
        return f_val