import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal components with higher frequencies and interactions
        sin_component = np.sum(np.sin(10.0 * np.pi * x_norm) * np.cos(8.0 * np.pi * x_norm)) + \
                        np.sum(np.cos(12.0 * np.pi * x_norm) * np.sin(9.0 * np.pi * x_norm))
        
        # Increased polynomial cross-terms with higher degrees
        poly_cross = 0.5 * np.sum(x_norm**4) + 0.2 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Exponential decay with modified scaling and adaptive conditioning
        exp_decay = np.sum(np.exp(-3.0 * np.abs(x_norm)) * np.sin(5.0 * np.pi * x_norm)**3)
        
        # Trigonometric coupling with phase shifts and multiple interaction terms
        trig_coupling = np.sum(np.sin(6.0 * np.pi * x_norm) * np.cos(7.0 * np.pi * x_norm)) + \
                        np.sum(np.cos(5.0 * np.pi * x_norm) * np.sin(8.0 * np.pi * x_norm)) + \
                        0.3 * np.sum(np.sin(4.0 * np.pi * x_norm) * np.cos(9.0 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality with stronger scaling
        condition_factor = 1.0 + 0.1 * self.dim
        
        # Structured noise term with enhanced randomness and dimensionality dependence
        noise = 0.1 * np.random.random() * condition_factor
        
        # Combine all components to form the final landscape
        return condition_factor * (sin_component + poly_cross + exp_decay + trig_coupling) + noise