import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Gaussian peaks with varying widths and heights
        gaussian_peaks = np.sum(np.exp(-5 * (x_scaled - 0.5)**2) + 
                               0.5 * np.exp(-3 * (x_scaled + 0.3)**2) + 
                               0.3 * np.exp(-2 * (x_scaled - 0.8)**2))
        
        # Logarithmic barrier terms to encourage boundary adherence
        log_barrier = np.sum(np.log(1 + 10 * x_scaled**2))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_coupling = 0.2 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * 
                                    (1 + 0.5 * np.sin(3 * np.pi * x_scaled[:-1])))
        
        # Sine wave modulation with varying frequency
        sine_modulation = np.sum(np.sin(7 * np.pi * x_scaled) * 
                               np.exp(-0.5 * x_scaled**2))
        
        # Combine all terms with appropriate weights
        return condition_factor * (poly_term + 0.8 * gaussian_peaks + 
                                 0.3 * log_barrier + cross_coupling + 
                                 0.2 * sine_modulation)