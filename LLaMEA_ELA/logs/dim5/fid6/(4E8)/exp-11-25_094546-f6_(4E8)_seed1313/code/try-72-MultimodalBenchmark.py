import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal structure with fractional exponents and chaos
        f1 = np.sum(np.abs(x_norm)**(1.2 + 0.8 * np.sin(15 * x_norm)) + 
                   0.3 * np.sin(25 * x_norm) * np.cos(18 * x_norm))
        
        # Dynamic frequency modulation with exponential scaling
        freq_mod = 1.0 + 0.6 * np.sin(4 * x_norm) * np.exp(-0.5 * x_norm**2)
        f2 = np.sum(np.sin(freq_mod * 10 * np.pi * x_norm) * 
                   np.cos(freq_mod * 7 * np.pi * x_norm) * 
                   np.exp(-0.3 * np.abs(x_norm)))
        
        # Hierarchical energy wells with adaptive depth and position
        well_depth = 2.5 + 1.2 * np.sin(3 * x_norm) + 0.8 * np.cos(5 * x_norm)
        well_position = 1.0 + 0.5 * np.sin(2 * x_norm)
        f3 = np.sum(well_depth * np.exp(-0.5 * (x_norm - well_position)**2) * 
                   (1.0 + 0.4 * np.cos(20 * x_norm)))
        
        # Cross-dimensional coupling with chaotic interaction terms
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * 
                  np.cos(np.pi * (x_norm[i] - x_norm[i+1])) * 
                  (1.0 + 0.2 * np.sin(12 * x_norm[i]) * np.cos(8 * x_norm[i+1]))
        
        # Multi-scale chaotic oscillations with varying amplitude
        f5 = np.sum(
            0.9 * np.sin(15 * np.pi * x_norm**1.3) * np.cos(8 * np.pi * x_norm**1.5) +
            0.5 * np.sin(25 * np.pi * x_norm**0.7) * np.cos(15 * np.pi * x_norm**1.2) +
            0.3 * np.sin(35 * np.pi * x_norm**0.9) * np.cos(20 * np.pi * x_norm**1.1)
        )
        
        # Adaptive radial barrier terms
        radial_barrier = np.sum(1.0 / (1.0 + np.exp(5 * (np.abs(x_norm) - 0.8))))
        f6 = 0.4 * radial_barrier
        
        # Combine all components with optimized weights for better performance
        return 1.2 * f1 + 0.8 * f2 + 1.0 * f3 + 0.4 * f4 + 0.6 * f5 + 0.3 * f6