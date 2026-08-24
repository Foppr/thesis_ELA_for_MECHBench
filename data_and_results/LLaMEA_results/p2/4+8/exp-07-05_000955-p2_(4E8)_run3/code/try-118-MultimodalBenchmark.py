import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for irregular dynamics
        tent_map = np.sum(np.where(np.abs(x) < 0.5, 2 * np.abs(x), 2 * (1 - np.abs(x))))
        
        # Spherical harmonic interaction with varying degrees
        r = np.sqrt(np.sum(x**2))
        if r == 0:
            sph_harm = 0.0
        else:
            sph_harm = np.sum(np.sin((np.arange(1, self.dim + 1) + 1) * np.arctan2(x[1], x[0])) * 
                             np.cos((np.arange(1, self.dim + 1) + 1) * r))
        
        # Adaptive ridge structure with varying curvature
        ridge = np.sum((x**2 + 0.1 * x**4) * np.cos(3.0 * x))
        
        # Multi-scale oscillatory component with frequency modulation
        oscillatory = np.sum(np.sin(2.0 * np.pi * x * (1 + 0.1 * np.sin(0.5 * x))) * 
                            np.cos(1.5 * np.pi * x * (1 + 0.05 * np.cos(0.3 * x))))
        
        # Gaussian mixture with adaptive variances
        gaussian_mixture = np.sum(np.exp(-0.5 * (x**2 + 0.05 * x**4)) * 
                                 np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Hyperbolic tangent based saddle points
        saddle = np.sum(np.tanh(x) * (x**3 - 0.5 * x))
        
        # Logarithmic spiral component for complex path behavior
        log_spiral = np.sum(np.log(np.abs(x) + 1.0) * np.sin(2.0 * np.pi * np.log(np.abs(x) + 1.0)))
        
        # Polynomial coupling with non-integer exponents
        poly_coupling = np.sum((x**1.7 + 0.3 * x**2.3 + 0.05 * x**3.1) * 
                              np.abs(x)**0.8)
        
        return 0.2 * tent_map + 0.15 * sph_harm + 0.2 * ridge + 0.1 * oscillatory + \
               0.15 * gaussian_mixture + 0.1 * saddle + 0.05 * log_spiral + 0.05 * poly_coupling