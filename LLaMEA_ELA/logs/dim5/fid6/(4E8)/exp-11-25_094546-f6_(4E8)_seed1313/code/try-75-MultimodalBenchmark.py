import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like structure with recursive self-similarity and modified exponents
        f1 = np.sum(np.abs(x_norm)**(1.4 + 0.6 * np.sin(12 * x_norm)))
        
        # Dynamic frequency modulation with altered scaling factors
        freq_mod = 1.2 + 0.3 * np.sin(4 * x_norm)
        f2 = np.sum(np.sin(freq_mod * 9 * np.pi * x_norm) * np.cos(freq_mod * 6 * np.pi * x_norm))
        
        # Hierarchical energy wells with modified depth and scaling
        well_depth = 1.8 + 1.7 * np.sin(2.5 * x_norm)
        f3 = np.sum(well_depth * np.exp(-0.4 * (x_norm**2)) * (1.0 + 0.4 * np.cos(18 * x_norm)))
        
        # Cross-dimensional fractal coupling with altered interaction terms
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(np.pi * (x_norm[i] - x_norm[i+1])) * np.exp(-0.1 * (i+1))
        
        # Multi-scale chaotic oscillations with modified amplitudes and exponents
        f5 = np.sum(
            0.9 * np.sin(14 * np.pi * x_norm**1.3) * np.cos(8 * np.pi * x_norm**1.5) +
            0.3 * np.sin(22 * np.pi * x_norm**0.7) * np.cos(15 * np.pi * x_norm**1.2)
        )
        
        # Combine all components with updated weights
        return 1.6 * f1 + 0.8 * f2 + 1.0 * f3 + 0.4 * f4 + 0.6 * f5