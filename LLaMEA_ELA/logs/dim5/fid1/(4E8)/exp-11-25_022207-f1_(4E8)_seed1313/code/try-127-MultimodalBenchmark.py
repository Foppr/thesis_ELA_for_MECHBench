import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis with chaotic modulation
        radial = np.sum(np.exp(-3 * (x_norm**2).sum()) * 
                       np.cos(5 * np.pi * x_norm.sum()) * 
                       np.sin(2 * np.pi * x_norm.sum()))
        
        # Modified sinusoidal component with fractal-like frequency variations
        sin_mod = np.sum(np.sin(3 * np.pi * x_norm) * 
                        np.cos(7 * np.pi * x_norm) * 
                        (1 + 0.5 * np.sin(9 * np.pi * x_norm)) * 
                        np.exp(-0.2 * np.abs(x_norm)))
        
        # Asymmetric cubic interactions with chaotic coupling
        asym_cubic = np.sum(x_norm**3 * (1 + 0.3 * np.cos(8 * x_norm)) * 
                           np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Perturbed saddle point structure with exponential gradient variations
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 * 
                       np.cos(0.7 * (x_norm[:-1] + x_norm[1:])) * 
                       np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                       (1 + 0.2 * np.sin(6 * np.pi * x_norm[:-1])))
        
        # Enhanced polynomial coupling with chaotic repulsive forces
        poly_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**4 * 
                              np.exp(-0.6 * (x_norm[:-1] - x_norm[1:])**2) * 
                              (1 + 0.4 * np.cos(10 * np.pi * x_norm[:-1])))
        
        # Novel chaotic repulsive force field
        repulsion = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                          np.sin(8 * np.pi * x_norm) * 
                          np.cos(3 * np.pi * x_norm.sum()) * 
                          np.tan(0.5 * x_norm))
        
        # Additional chaotic noise for robustness testing
        noise = 0.15 * np.random.normal(0, 1)
        
        return radial + sin_mod + asym_cubic + saddle + poly_coupling + repulsion + noise