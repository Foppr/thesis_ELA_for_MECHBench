import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis with chaotic modulation and dynamic scaling
        radial = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                       np.cos(7 * np.pi * x_norm.sum()) * 
                       np.sin(3 * np.pi * x_norm.sum()) * 
                       (1 + 0.4 * np.sin(11 * np.pi * x_norm.sum())))
        
        # Modified sinusoidal component with fractal-like frequency variations and adaptive scaling
        sin_mod = np.sum(np.sin(5 * np.pi * x_norm) * 
                        np.cos(9 * np.pi * x_norm) * 
                        (1 + 0.6 * np.sin(13 * np.pi * x_norm)) * 
                        np.exp(-0.3 * np.abs(x_norm)) * 
                        (1 + 0.2 * np.cos(17 * np.pi * x_norm)))
        
        # Asymmetric cubic interactions with chaotic coupling and dynamic modulation
        asym_cubic = np.sum(x_norm**3 * (1 + 0.4 * np.cos(10 * x_norm)) * 
                           np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           np.sin(6 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                           (1 + 0.3 * np.sin(14 * np.pi * x_norm[:-1])))
        
        # Perturbed saddle point structure with exponential gradient variations and adaptive scaling
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4 * 
                       np.cos(0.9 * (x_norm[:-1] + x_norm[1:])) * 
                       np.exp(-0.6 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                       (1 + 0.3 * np.sin(8 * np.pi * x_norm[:-1])) * 
                       (1 + 0.2 * np.cos(12 * np.pi * x_norm[1:])))
        
        # Enhanced polynomial coupling with chaotic repulsive forces and dynamic scaling
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**5 * 
                              np.exp(-0.7 * (x_norm[:-1] - x_norm[1:])**2) * 
                              (1 + 0.5 * np.cos(15 * np.pi * x_norm[:-1])) * 
                              (1 + 0.3 * np.sin(19 * np.pi * x_norm[1:])))
        
        # Novel chaotic repulsive force field with dynamic modulation and adaptive noise
        repulsion = np.sum(np.exp(-3 * (x_norm**2).sum()) * 
                          np.sin(10 * np.pi * x_norm) * 
                          np.cos(4 * np.pi * x_norm.sum()) * 
                          np.tan(0.7 * x_norm) * 
                          (1 + 0.4 * np.sin(23 * np.pi * x_norm)))
        
        # Additional chaotic noise for robustness testing with dynamic scaling
        noise = 0.2 * np.random.normal(0, 1) * (1 + 0.3 * np.sin(29 * np.pi * x_norm[0] if len(x_norm) > 0 else 0))
        
        return radial + sin_mod + asym_cubic + saddle + poly_coupling + repulsion + noise