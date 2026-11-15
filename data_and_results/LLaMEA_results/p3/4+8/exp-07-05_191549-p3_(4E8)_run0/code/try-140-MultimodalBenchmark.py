import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Self-similar fractal component with recursive sine modulation
        fractal = np.sum(np.sin(2 * np.pi * x_norm * np.power(2, np.arange(1, self.dim + 1))) * 
                        np.cos(3 * np.pi * x_norm * np.power(3, np.arange(1, self.dim + 1))) * 
                        np.sin(5 * np.pi * x_norm * np.power(5, np.arange(1, self.dim + 1))))
        
        # Dynamic gradient field with time-varying frequency modulation
        r = np.linalg.norm(x_norm, axis=0)
        gradient_field = np.sum(r * np.sin(10 * np.pi * r + 0.5 * np.sin(20 * np.pi * r)) * 
                              np.cos(8 * np.pi * r + 0.3 * np.cos(16 * np.pi * r)))
        
        # Hybrid elliptic-Gaussian peaks with varying ellipticity and amplitude
        elliptic_gaussian = np.sum(0.5 * np.exp(-0.5 * ((x_norm - 0.3)**2 + 0.3 * (x_norm + 0.2)**2)) + 
                                 0.3 * np.exp(-0.3 * ((x_norm + 0.4)**2 + 0.4 * (x_norm - 0.1)**2)) + 
                                 0.4 * np.exp(-0.4 * ((x_norm - 0.5)**2 + 0.2 * (x_norm + 0.3)**2)))
        
        # Mixed hyperbolic and polynomial barrier terms with dynamic scaling
        barrier = np.sum(np.tanh(2 * x_norm) * (x_norm**4 + 0.5 * x_norm**2 + 0.1) + 
                        0.2 * np.log(1 + x_norm**2) * np.exp(-0.5 * x_norm**2))
        
        # Coupling term with non-separable interaction and chaotic modulation
        coupling = np.sum(np.sin(7 * np.pi * x_norm + 0.2 * np.sin(14 * np.pi * x_norm)) * 
                         np.cos(5 * np.pi * x_norm + 0.1 * np.cos(10 * np.pi * x_norm)) * 
                         np.exp(-0.2 * x_norm**2) * (x_norm**3 + 0.2 * x_norm + 0.05))
        
        # Asymmetric multi-peak structure with fractal-like positioning
        multi_peaks = np.sum(0.8 * np.exp(-1.5 * (x_norm - 0.4)**2) * np.sin(15 * np.pi * x_norm) + 
                           0.6 * np.exp(-2.0 * (x_norm + 0.3)**2) * np.cos(12 * np.pi * x_norm) + 
                           0.5 * np.exp(-1.0 * (x_norm - 0.6)**2) * np.sin(18 * np.pi * x_norm))
        
        # Combined objective with optimized weights for better conditioning
        return 0.25 * fractal + 0.20 * gradient_field + 0.18 * elliptic_gaussian + 0.17 * barrier + 0.15 * coupling + 0.05 * multi_peaks