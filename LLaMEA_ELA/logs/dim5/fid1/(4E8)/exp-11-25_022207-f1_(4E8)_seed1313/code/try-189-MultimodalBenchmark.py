import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with multiple chaotic scales
        r = np.sqrt(np.sum(x_norm**2))
        fractal_term = np.sin(20 * r) * np.cos(10 * r) * np.exp(-0.3 * r**2)
        
        # Adaptive sinusoidal coupling with dynamic frequencies
        coupling = 0.0
        for i in range(self.dim - 1):
            freq = 6 + 4 * np.sin(0.7 * r)
            coupling += np.sin(freq * (x_norm[i] + x_norm[i+1])) * np.cos(freq * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale radial modulation with chaotic enhancement
        radial_mod = np.sum((np.sin(20 * r) + np.cos(15 * r) + np.sin(10 * r)) * 
                           np.exp(-0.4 * r**2))
        
        # Enhanced polynomial interactions with dynamic weighting
        poly_interaction = np.sum(x_norm**5 * (1 + 0.7 * np.sin(8 * x_norm)) * 
                                np.exp(-0.3 * np.abs(x_norm)))
        
        # Dynamic noise component with position-adaptive scaling
        noise = np.sum(0.25 * np.sin(30 * x_norm) * np.cos(25 * x_norm) * 
                      (1 + 0.6 * np.sin(4 * r)) * np.exp(-0.2 * r**2))
        
        # Saddle-point enhanced gradient field with chaotic modulation
        grad_field = np.sum((x_norm[:-1]**4 - x_norm[1:]**4)**2 * 
                          np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Additional chaotic modulation term
        chaos_term = 0.7 * np.sin(35 * r) * np.cos(25 * r) * np.exp(-0.2 * r**2)
        
        # Combined landscape with global scaling and enhanced complexity
        return 3.0 * (fractal_term + coupling + radial_mod + poly_interaction + 
                     noise + grad_field + chaos_term)