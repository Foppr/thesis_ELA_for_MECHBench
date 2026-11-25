import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-0.1 * r) * np.sin(2.0 * r) * np.cos(0.5 * r)
        
        # Multi-modal trigonometric components with varying frequencies
        modal_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            modal_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.05 * x[i]**2)
        
        # Asymmetric cross-dimensional coupling with exponential weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                coupling_term += weight * np.sin(x[i] * x[j]) * np.cos(0.2 * x[i] + 0.3 * x[j])
        
        # Polynomial and logarithmic components for additional complexity
        poly_term = np.sum(x**4) * np.exp(-0.01 * r)
        log_term = np.sum(np.log(1.0 + np.abs(x))) * np.sin(0.2 * r)
        
        # Final chaotic combination with asymmetric scaling
        result = 0.5 * radial_term + 0.3 * modal_sum + 0.2 * coupling_term + 0.1 * poly_term + 0.1 * log_term
        
        return result