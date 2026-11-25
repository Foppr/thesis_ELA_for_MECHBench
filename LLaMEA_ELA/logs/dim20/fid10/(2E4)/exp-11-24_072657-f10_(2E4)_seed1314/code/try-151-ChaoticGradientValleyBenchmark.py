import numpy as np

class ChaoticGradientValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced composite trigonometric-gaussian terms with nested chaos
        trig_gauss_terms = np.sum(np.exp(-0.3 * x_norm**2) * 
                                np.cos(4.0 * np.pi * x_norm) * 
                                (1.0 + 0.4 * np.sin(3.0 * x_norm**2)) * 
                                np.tanh(2.0 * x_norm) * 
                                np.exp(-0.1 * np.abs(x_norm)))
        
        # Nested chaotic gradient interactions with fractal frequency modulation
        nested_grad = np.sum(np.exp(-0.4 * np.abs(x_norm)) * 
                           np.sin(5.0 * x_norm + 0.6 * np.sin(2.0 * x_norm) + 
                                  0.3 * np.sin(4.0 * x_norm)) * 
                           np.cos(3.0 * x_norm + 0.4 * np.cos(1.5 * x_norm) + 
                                  0.2 * np.cos(3.0 * x_norm)))
        
        # Multi-scale fractal exponential decay with dynamic frequency modulation
        freq_mod = 3.0 + 2.0 * np.sin(0.6 * self.dim) + 1.2 * np.cos(0.4 * self.dim) + \
                   0.8 * np.sin(0.3 * self.dim**1.5)
        fractal_terms = np.sum(np.exp(-freq_mod * np.abs(x_norm)**2.2) * 
                             np.sin(freq_mod * x_norm**1.7) * 
                             np.cos(freq_mod * x_norm**1.4) * 
                             np.tanh(0.5 * x_norm**2))
        
        # Higher-order cross-dimensional interference with nested coupling
        coupling_strength = 0.8 + 0.4 * np.sin(0.5 * self.dim) * np.cos(0.3 * self.dim)
        cross_terms = np.sum(coupling_strength * np.exp(-0.6 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           (x_norm[:-1] * x_norm[1:] + 0.7 * (x_norm[:-1]**2 - x_norm[1:]**2) + 
                            0.3 * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                           np.sin(4.0 * (x_norm[:-1] - x_norm[1:]) + 
                                  0.5 * np.sin(2.0 * (x_norm[:-1] - x_norm[1:]))))
        
        # Adaptive dimensional conditioning with chaotic scaling and fractal structure
        dim_conditioning = 1.2 + 0.6 * np.sin(0.4 * self.dim) * np.cos(0.3 * self.dim) * \
                          np.tanh(0.1 * self.dim)
        
        # Combined landscape with enhanced multi-modality and fractal complexity
        result = (trig_gauss_terms + 0.8 * nested_grad + 0.9 * fractal_terms + 
                 0.7 * cross_terms) * dim_conditioning
        
        # Add fractal-like noise for increased complexity and algorithm discrimination
        noise = 0.002 * np.random.random() * (1.0 + 0.3 * np.sin(self.dim * 1.2)) * \
                (1.0 + 0.2 * np.cos(self.dim * 0.7))
        
        return result + noise