import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal structure with variable dimensionality
        fractal_exp = 1.2 + 0.8 * np.sin(5 * x_norm)
        f1 = np.sum(np.abs(x_norm)**fractal_exp)
        
        # Adaptive curvature modulation based on position
        curvature = 1.0 + 0.3 * np.cos(4 * x_norm)
        f2 = np.sum(curvature * np.sin(6 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Hierarchical energy wells with dynamic depth
        well_depth = 1.5 + 1.0 * np.sin(3 * x_norm)
        f3 = np.sum(well_depth * np.exp(-0.3 * x_norm**2) * (1.0 + 0.4 * np.sin(10 * x_norm)))
        
        # Cross-dimensional coupling with varying strength
        f4 = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.5 + 0.5 * np.cos(np.pi * (x_norm[i] + x_norm[i+1]))
            f4 += coupling_strength * np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale chaotic oscillations with adaptive frequencies
        freq1 = 8.0 + 4.0 * np.sin(2 * x_norm)
        freq2 = 12.0 + 6.0 * np.cos(3 * x_norm)
        f5 = np.sum(
            0.6 * np.sin(freq1 * x_norm**1.1) * np.cos(freq2 * x_norm**1.3) +
            0.3 * np.sin(freq2 * x_norm**0.9) * np.cos(freq1 * x_norm**1.5)
        )
        
        # Combine all components with optimized weights
        return 1.2 * f1 + 0.8 * f2 + 1.0 * f3 + 0.4 * f4 + 0.6 * f5