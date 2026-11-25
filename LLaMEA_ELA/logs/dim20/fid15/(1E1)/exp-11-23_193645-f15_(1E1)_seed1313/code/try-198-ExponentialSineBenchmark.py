import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponential interactions with varying decay rates and amplitudes
        chaotic_exp_term = np.sum(np.exp(-2.0 * np.abs(x_norm)) * np.sin(3.0 * np.pi * x_norm) * 
                                 np.cos(7.0 * np.pi * x_norm) + 0.5 * np.exp(-1.5 * x_norm ** 2))
        
        # Nested sine wave modulations with fractal-like frequency variations
        nested_sine_term = np.sum(np.sin(2.5 * np.pi * x_norm) * 
                                 np.sin(4.0 * np.pi * np.sin(1.5 * np.pi * x_norm)) + 
                                 0.3 * np.sin(6.0 * np.pi * x_norm) * 
                                 np.sin(9.0 * np.pi * np.sin(2.0 * np.pi * x_norm)))
        
        # Complex asymmetric cross-dimensional coupling with chaotic weights
        complex_coupling_term = 0.5 * np.sum(np.exp(-1.2 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                            (x_norm[:-1] ** 3 + 0.8 * x_norm[1:] ** 3) * 
                                            np.sin(4.0 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Hyperbolic tangent interaction terms with multiple frequency components
        tanh_interaction_term = 0.6 * np.sum(np.tanh(2.0 * x_norm[:-1]) * np.tanh(3.0 * x_norm[1:]) * 
                                           np.sin(5.0 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Additional chaotic quadratic cross-term with varying coefficients
        chaotic_quad_term = 0.2 * np.sum((np.exp(-0.5 * x_norm[:-1] ** 2) + 
                                         0.3 * np.exp(-0.8 * x_norm[1:] ** 2)) * 
                                        (x_norm[:-1] + x_norm[1:]) ** 2)
        
        # Combined function with chaotic weights and complex interactions
        result = 4.0 * chaotic_exp_term + 1.2 * nested_sine_term + 0.8 * complex_coupling_term + 0.5 * tanh_interaction_term + 0.3 * chaotic_quad_term
        
        return result