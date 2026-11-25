import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(2.0 * r) * np.cos(0.5 * r)
        
        # Asymmetric trigonometric components with varying frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            asymmetry = (-1)**i * 0.5
            trig_sum += asymmetry * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional asymmetric coupling with exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = (i + 1) / (j + 1)
                coupling_term += coupling_factor * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j]) * np.cos(0.2 * x[i])
        
        # Polynomial and logarithmic components for additional complexity
        poly_term = np.sum(x**4) * np.exp(-0.05 * r)
        log_term = np.sum(np.log(np.abs(x) + 1.0)) * np.sin(0.3 * r)
        
        # Final multimodal combination with chaotic weighting
        result = radial_term + trig_sum + coupling_term + poly_term + log_term
        
        return result