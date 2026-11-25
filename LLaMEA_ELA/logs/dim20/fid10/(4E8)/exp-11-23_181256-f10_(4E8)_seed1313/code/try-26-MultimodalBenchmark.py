import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees and added sharp minimum
        poly_term = np.sum(x_scaled**6 + 0.7 * x_scaled**5 + 0.3 * x_scaled**4 + 0.1 * x_scaled**3)
        
        # Enhanced trigonometric term with multiple frequencies
        trig_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) + 
                          np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Exponential terms creating multiple steep gradients and peaks
        exp_term1 = np.sum(np.exp(-x_scaled**2 / 0.3) + np.exp(-(x_scaled - 0.3)**2 / 0.2) + 
                          np.exp(-(x_scaled + 0.4)**2 / 0.15))
        
        # Additional exponential barrier near boundaries
        exp_barrier = np.sum(np.exp(-x_scaled**2 / 0.4) + np.exp(-(x_scaled - 0.6)**2 / 0.25))
        
        # Complex cross-term interaction with sine modulation
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(3 * np.pi * x_scaled[:-1]) * 
                           np.cos(2 * np.pi * x_scaled[1:]))
        
        # Quadratic coupling term to increase conditioning difficulty
        quad_coupling = np.sum((x_scaled[:-1] - x_scaled[1:]) ** 2 * np.exp(-x_scaled[:-1]**2))
        
        # Combine all terms with different weights
        result = 3.0 * poly_term + 1.2 * trig_term - 0.5 * exp_term1 - 0.4 * exp_barrier + 0.15 * cross_term + 0.1 * quad_coupling
        
        return result