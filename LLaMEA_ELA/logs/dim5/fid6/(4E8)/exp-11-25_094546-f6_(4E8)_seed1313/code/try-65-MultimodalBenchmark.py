import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like structure with recursive self-similarity
        f1 = np.sum(np.abs(x_norm)**(1.3 + 0.7 * np.sin(10 * x_norm)))
        
        # Dynamic frequency modulation based on position
        freq_mod = 1.0 + 0.5 * np.sin(3 * x_norm)
        f2 = np.sum(np.sin(freq_mod * 8 * np.pi * x_norm) * np.cos(freq_mod * 5 * np.pi * x_norm))
        
        # Hierarchical energy wells with varying depths
        well_depth = 2.0 + 1.5 * np.sin(2 * x_norm)
        f3 = np.sum(well_depth * np.exp(-0.5 * (x_norm**2)) * (1.0 + 0.3 * np.cos(15 * x_norm)))
        
        # Cross-dimensional fractal coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale chaotic oscillations
        f5 = np.sum(
            0.8 * np.sin(12 * np.pi * x_norm**1.2) * np.cos(7 * np.pi * x_norm**1.4) +
            0.4 * np.sin(20 * np.pi * x_norm**0.8) * np.cos(13 * np.pi * x_norm**1.1)
        )
        
        # Combine all components with scale-dependent weights
        return 1.5 * f1 + 0.7 * f2 + 0.9 * f3 + 0.3 * f4 + 0.5 * f5