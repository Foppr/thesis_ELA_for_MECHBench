import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add radial sinusoidal components
        r = np.sqrt(np.sum(x**2))
        f_val += 0.5 * np.sin(3 * r) * np.exp(-0.1 * r)
        
        # Add multi-modal sinusoidal terms with varying frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(4 * x[i]) * np.cos(2 * x[i]) + 0.2 * np.sin(6 * x[i])**2
        
        # Add polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interactions to avoid overcomplication
                f_val += 0.05 * (x[i]**2 + x[j]**2) * np.sin(3 * (x[i] - x[j]))
        
        # Add higher-order polynomial terms with exponential decay
        for i in range(self.dim):
            f_val += 0.01 * (x[i]**6) * np.exp(-0.5 * x[i]**2)
        
        # Add a global sinusoidal modulation based on the sum of variables
        f_val += 0.2 * np.sin(0.5 * np.sum(x)) * np.cos(0.3 * np.sum(x**2))
        
        # Add localized peaks using Gaussian-like functions with varying centers and scales
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i, c in enumerate(centers):
            if i < self.dim:
                f_val += 0.1 * np.exp(-0.5 * (x[i] - c)**2) * np.sin(5 * (x[i] - c))
        
        return f_val