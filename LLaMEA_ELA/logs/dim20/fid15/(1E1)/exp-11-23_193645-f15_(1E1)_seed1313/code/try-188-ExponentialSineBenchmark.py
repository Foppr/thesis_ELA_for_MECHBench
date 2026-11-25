import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponential decay component with nested frequencies
        chaotic_exp_term = np.sum(np.exp(-2.0 * np.abs(x_norm)) * 
                                 np.sin(7 * np.pi * x_norm) * 
                                 np.cos(3 * np.pi * x_norm) + 
                                 0.5 * np.exp(-1.5 * x_norm ** 2) * 
                                 np.sin(11 * np.pi * x_norm))
        
        # Nested sine wave modulations with varying amplitudes and frequencies
        nested_sine_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                                 np.sin(6 * np.pi * x_norm) * 
                                 np.sin(10 * np.pi * x_norm) + 
                                 0.4 * np.sin(4 * np.pi * x_norm) * 
                                 np.sin(9 * np.pi * x_norm))
        
        # Complex asymmetric cross-dimensional coupling with chaotic weights
        complex_coupling_term = 0.5 * np.sum(np.exp(-0.8 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                            (x_norm[:-1] ** 3 + 0.6 * x_norm[1:] ** 3) * 
                                            np.sin(5 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Multi-scale interaction terms with chaotic modulation
        multi_scale_term = 0.3 * np.sum(np.sin(2.5 * np.pi * (x_norm[:-1] ** 2 - x_norm[1:] ** 2)) * 
                                      np.exp(-0.5 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
                                      (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Additional chaotic quadratic cross-term with asymmetric scaling
        chaotic_quad_term = 0.2 * np.sum((x_norm[:-1] ** 2 + 0.3 * x_norm[1:] ** 2) * 
                                        np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Combined function with chaotic weights and nested complexity
        result = 4.2 * chaotic_exp_term + 1.1 * nested_sine_term + 0.8 * complex_coupling_term + 0.55 * multi_scale_term + 0.3 * chaotic_quad_term
        
        return result