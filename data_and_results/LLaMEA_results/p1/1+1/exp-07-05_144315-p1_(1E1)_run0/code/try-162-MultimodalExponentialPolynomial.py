import numpy as np

class MultimodalExponentialPolynomial:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly = np.sum(x**4 + 0.5 * x**3 - 2 * x**2 + 0.1 * x)
        
        # Exponential decay component with varying rates
        exp_decay = 0.0
        rates = np.linspace(0.1, 1.5, self.dim)
        for i in range(self.dim):
            exp_decay += np.exp(-rates[i] * np.abs(x[i])) * np.cos(rates[i] * x[i])
        
        # Logarithmic barrier component
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1 + np.abs(x[i]) + 0.1) * np.sin(x[i])
        
        # Cross-dimensional interaction with sine-cosine products
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Dynamic scaling component with periodic modulation
        dynamic_scale = 0.0
        for i in range(self.dim):
            dynamic_scale += (1 + 0.3 * np.sin(0.5 * i)) * x[i]**2 * np.exp(-0.05 * x[i]**2)
        
        # Multimodal peaks with varying heights and widths
        peaks = 0.0
        peak_centers = np.linspace(-4.0, 4.0, 7)
        for center in peak_centers:
            peaks += 2.0 * np.exp(-0.5 * np.sum(((x - center) / 1.2) ** 2)) + 0.5 * np.sin(2 * center)
        
        # Asymmetric component with cubic terms
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += 0.8 * x[i]**3 + 0.2 * x[i]**2 - 0.5 * x[i]
        
        # Combined fitness with weighted components
        return 0.7 * poly + 0.6 * exp_decay + 0.5 * log_barrier + 0.4 * cross_interaction + 0.8 * dynamic_scale + 0.3 * peaks + 0.2 * asymmetric