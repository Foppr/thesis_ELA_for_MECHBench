import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + 2 * np.sin(i * 0.5)
            poly += (x[i] ** degree) * np.exp(-0.1 * np.abs(x[i]))
        
        # Exponential decay component with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i])
        
        # Logarithmic barrier component
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + np.abs(x[i])) * np.cos(x[i])
        
        # Cross-dimensional interaction with adaptive coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.4 * np.sin((i + j) * 0.2)
                cross += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Adaptive multimodal component with dynamic centers
        multi_modal = 0.0
        centers = np.linspace(-4.0, 4.0, 7)
        for i, center in enumerate(centers):
            width = 1.0 + 0.5 * np.sin(i * 0.7)
            multi_modal += np.exp(-0.5 * ((x - center) / width) ** 2) * np.cos(2 * np.pi * (x - center))
        
        # Asymmetric scaling component
        asym_scale = 0.0
        for i in range(self.dim):
            asym_scale += (x[i] ** 3) * np.exp(-0.2 * x[i] ** 2) * np.sin(0.5 * x[i])
        
        # Fractional harmonic component
        frac_harmonic = 0.0
        for i in range(self.dim):
            frac_harmonic += (np.abs(x[i]) ** 1.7) * np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Combined weighted sum
        return 0.8 * poly + 0.6 * exp_decay + 0.5 * log_barrier + 0.4 * cross + 0.7 * multi_modal + 0.3 * asym_scale + 0.2 * frac_harmonic