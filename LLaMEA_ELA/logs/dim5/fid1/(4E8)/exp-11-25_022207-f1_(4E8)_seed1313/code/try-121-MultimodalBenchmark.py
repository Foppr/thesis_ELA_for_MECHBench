import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic structure with higher frequency modulations
        chaotic_term = np.sum(np.exp(-np.abs(x_norm)) * 
                             np.sin(3 * np.pi * x_norm) * 
                             np.cos(5 * np.pi * x_norm) * 
                             (1 + 0.5 * np.sin(7 * x_norm)) * 
                             np.log(1 + np.abs(x_norm)))
        
        # Fractal-like gradient variations with multi-fractal scaling
        fractal_term = np.sum((x_norm**3 + 0.2 * x_norm) * 
                             np.sin(15 * np.pi * x_norm) * 
                             np.cos(8 * np.pi * x_norm) * 
                             np.exp(-0.3 * x_norm**2) * 
                             (1 + 0.1 * np.sin(12 * x_norm)))
        
        # Perturbed exponential coupling with asymmetric repulsion
        coupling_term = np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                              (x_norm[:-1] - x_norm[1:])**4 * 
                              np.sin(0.7 * (x_norm[:-1] + x_norm[1:])) * 
                              (1 + 0.2 * np.cos(3 * (x_norm[:-1] - x_norm[1:]))))
        
        # Multi-scale harmonic modulation with varying amplitudes and frequencies
        multi_scale = np.sum(np.sin(4 * np.pi * x_norm) * 
                            np.cos(6 * np.pi * x_norm) * 
                            np.sin(10 * np.pi * x_norm) * 
                            (1 + 0.3 * np.cos(8 * np.pi * x_norm)) * 
                            np.exp(-0.2 * x_norm**2))
        
        # Asymmetric polynomial landscape with logarithmic and hyperbolic perturbations
        poly_term = np.sum((x_norm**5 - 0.6 * x_norm**3 + 0.15 * x_norm**2) * 
                          np.log(1 + np.abs(x_norm)) * 
                          np.tanh(2 * x_norm) * 
                          np.exp(-0.4 * x_norm**2))
        
        # Additional chaotic repulsion field
        repulsion = np.sum(0.5 * np.exp(-x_norm**2) * 
                          np.sin(10 * x_norm) * 
                          np.cos(15 * x_norm) * 
                          (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Combined landscape with global conditioning
        return chaotic_term + fractal_term - coupling_term + multi_scale + poly_term + repulsion