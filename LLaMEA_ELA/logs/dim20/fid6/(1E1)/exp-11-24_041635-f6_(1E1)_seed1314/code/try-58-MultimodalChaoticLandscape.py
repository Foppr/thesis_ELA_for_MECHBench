import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with oscillating amplitude
        r = np.sqrt(np.sum(x**2))
        radial_term = np.sin(5.0 * r) * np.exp(-0.1 * r)
        
        # Multimodal trigonometric components
        modal_sum = 0.0
        for i in range(self.dim):
            modal_sum += (1.0 + 0.5 * np.sin(3.0 * x[i])) * \
                        (1.0 + 0.3 * np.cos(7.0 * x[i])) * \
                        np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional interaction with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_strength = 1.0 / (1.0 + (i - j)**2)
                cross_term += coupling_strength * np.sin(x[i] + x[j]) * \
                             np.cos(0.5 * x[i] * x[j])
        
        # Exponential decay with sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-0.2 * (x[i] - 1.0)**2) * \
                        np.sin(2.0 * x[i]) * \
                        np.cos(0.3 * x[i])
        
        # Polynomial and logarithmic components
        poly_term = np.sum(x**4) * np.exp(-0.01 * r)
        log_term = np.sum(np.log(1.0 + np.abs(x))) * np.sin(0.5 * r)
        
        # Final combined landscape
        result = radial_term + modal_sum + cross_term + exp_decay + poly_term + log_term
        
        return result