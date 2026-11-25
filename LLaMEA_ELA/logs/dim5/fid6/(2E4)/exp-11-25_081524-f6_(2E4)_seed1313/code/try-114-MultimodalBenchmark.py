import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component with varying exponents
        poly_valley = 0.0
        for i in range(self.dim):
            poly_valley += (x[i] ** (2 + i % 3)) * np.cos(0.5 * x[i])
        
        # Gaussian peak component with adaptive heights and widths
        gaussian_peak = 0.0
        for i in range(self.dim):
            height = 1.0 + 0.5 * np.sin(i)
            width = 0.5 + 0.3 * np.cos(i)
            gaussian_peak += height * np.exp(-0.5 * ((x[i] - 1.0) ** 2) / (width ** 2))
        
        # Logarithmic barrier component with exponential scaling
        log_barrier = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                log_barrier += np.log(-x[i] + 5.0) * np.exp(-0.1 * x[i])
            else:
                log_barrier += np.log(x[i] + 5.0) * np.exp(0.1 * x[i])
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim-1):
            cross_coupling += np.sin(x[i] * x[i+1]) * np.cos(0.3 * (x[i] + x[i+1]))
        
        # Global scaling factor with dimension-dependent modulation
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return (poly_valley + gaussian_peak + log_barrier + cross_coupling) * scale_factor