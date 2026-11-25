import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with multiple chaotic scales
        r = np.sqrt(np.sum(x_norm**2))
        fractal_term = np.sin(18 * r) * np.cos(9 * r) * np.exp(-0.25 * r**2)
        
        # Adaptive sinusoidal coupling with dynamic frequencies
        coupling = 0.0
        for i in range(self.dim - 1):
            freq = 5 + 3 * np.sin(0.6 * r)
            coupling += np.sin(freq * (x_norm[i] + x_norm[i+1])) * np.cos(freq * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale radial modulation with chaotic enhancement
        radial_mod = np.sum((np.sin(15 * r) + np.cos(12 * r) + np.sin(9 * r)) * 
                           np.exp(-0.35 * r**2))
        
        # Enhanced polynomial interactions with dynamic weighting
        poly_interaction = np.sum(x_norm**4 * (1 + 0.6 * np.sin(7 * x_norm)) * 
                                np.exp(-0.25 * np.abs(x_norm)))
        
        # Dynamic noise component with position-adaptive scaling
        noise = np.sum(0.2 * np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                      (1 + 0.5 * np.sin(3 * r)) * np.exp(-0.15 * r**2))
        
        # Saddle-point enhanced gradient field with chaotic modulation
        grad_field = np.sum((x_norm[:-1]**3 - x_norm[1:]**3)**2 * 
                          np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Additional chaotic modulation term
        chaos_term = 0.6 * np.sin(30 * r) * np.cos(22 * r) * np.exp(-0.15 * r**2)
        
        # Combined landscape with global scaling and enhanced complexity
        return 2.5 * (fractal_term + coupling + radial_mod + poly_interaction + 
                     noise + grad_field + chaos_term)