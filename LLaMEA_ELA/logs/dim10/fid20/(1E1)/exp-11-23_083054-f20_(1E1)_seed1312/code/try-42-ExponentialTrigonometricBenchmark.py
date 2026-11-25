import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_term = np.sum(np.exp(-2.0 * np.abs(x_norm)) + 0.5 * np.exp(-5.0 * np.abs(x_norm)))
        
        # Trigonometric interaction terms with varying frequencies
        trig_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) + 
                          0.3 * np.sin(11 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Polynomial coupling with mixed exponents
        poly_term = np.sum(2.0 * x_norm**3 + 0.8 * x_norm**5 + 0.2 * x_norm**7)
        
        # Cross-terms creating sharp ridges and valleys
        ridge_term = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**2 + 
                           0.5 * np.abs(x_norm[:-1] + x_norm[1:])**3)
        
        # Gaussian-like peaks with varying heights and widths
        peak_term = np.sum(0.5 * np.exp(-0.5 * (x_norm - 0.3)**2) + 
                          0.3 * np.exp(-0.3 * (x_norm + 0.4)**2) + 
                          0.2 * np.exp(-0.7 * (x_norm - 0.8)**2))
        
        # Combine all terms with different weights
        return 0.4 * exp_term + 0.3 * trig_term + 0.15 * poly_term + 0.1 * ridge_term - 0.05 * peak_term