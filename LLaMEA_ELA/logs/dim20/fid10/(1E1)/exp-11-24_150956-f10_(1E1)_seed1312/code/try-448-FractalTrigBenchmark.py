import numpy as np

class FractalTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like composite trigonometric potentials with varying frequencies
        pot1 = np.sum(np.sin(2.0 * np.pi * x_scaled) * np.cos(3.0 * np.pi * x_scaled) + 
                     np.sin(4.0 * np.pi * x_scaled**2) * np.cos(5.0 * np.pi * x_scaled**2))
        
        # Self-similar pattern with recursive scaling
        pot2 = np.sum(np.sin(8.0 * np.pi * x_scaled) * np.cos(7.0 * np.pi * x_scaled) + 
                     0.5 * np.sin(16.0 * np.pi * x_scaled**2) * np.cos(14.0 * np.pi * x_scaled**2))
        
        # Adaptive conditioning based on dimension
        cond_factor = np.sum((1.0 + 0.3 * np.sin(2.0 * np.pi * x_scaled)) * 
                           (1.0 + 0.2 * np.cos(3.0 * np.pi * x_scaled)))
        
        # Cross-dimensional coupling with recursive interaction
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Multi-scale harmonic interference with phase modulation
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                         0.7 * np.sin(12.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                         0.3 * np.sin(24.0 * x_scaled**3) * np.cos(36.0 * x_scaled**3))
        
        # Asymmetric fractal landscape with weighted sum
        return 0.4 * pot1 + 0.3 * pot2 + 0.15 * cond_factor + 0.1 * cross_terms + 0.05 * harmonics + 2.1