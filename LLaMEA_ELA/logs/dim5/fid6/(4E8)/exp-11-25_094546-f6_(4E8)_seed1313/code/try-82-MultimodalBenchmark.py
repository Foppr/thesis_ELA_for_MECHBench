import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal structure with variable dimensionality and adaptive scaling
        fractal_exp = 1.5 + 0.7 * np.sin(3 * x_norm) * np.cos(2 * x_norm)
        f1 = np.sum(np.abs(x_norm)**fractal_exp)
        
        # Adaptive curvature modulation with dynamic phase shifts
        curvature = 1.2 + 0.4 * np.sin(5 * x_norm + np.pi/4)
        f2 = np.sum(curvature * np.sin(7 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Hierarchical energy wells with dynamic depth and radial barriers
        well_depth = 2.0 + 1.5 * np.sin(4 * x_norm)
        barrier = 1.0 + 0.8 * np.exp(-0.5 * x_norm**2) * np.cos(6 * x_norm)
        f3 = np.sum(well_depth * barrier * np.exp(-0.4 * x_norm**2) * (1.0 + 0.5 * np.sin(12 * x_norm)))
        
        # Cross-dimensional coupling with adaptive strength and chaotic modulation
        f4 = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.8 + 0.6 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + np.pi/3)
            phase_shift = 0.5 * np.cos(2 * np.pi * (x_norm[i] - x_norm[i+1]))
            f4 += coupling_strength * np.sin(np.pi * (x_norm[i] + x_norm[i+1]) + phase_shift) * np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale chaotic oscillations with adaptive frequencies and amplitude modulation
        freq1 = 10.0 + 5.0 * np.sin(3 * x_norm) * np.cos(2 * x_norm)
        freq2 = 15.0 + 7.0 * np.sin(4 * x_norm) * np.cos(3 * x_norm)
        amp1 = 0.8 + 0.3 * np.sin(2 * x_norm)
        amp2 = 0.6 + 0.4 * np.cos(3 * x_norm)
        f5 = np.sum(
            amp1 * np.sin(freq1 * x_norm**1.2) * np.cos(freq2 * x_norm**1.4) +
            amp2 * np.sin(freq2 * x_norm**1.0) * np.cos(freq1 * x_norm**1.6)
        )
        
        # Add chaotic noise component for increased complexity
        noise = 0.1 * np.random.rand(self.dim)
        f6 = np.sum(noise * np.sin(8 * x_norm))
        
        # Combine all components with optimized weights
        return 1.5 * f1 + 0.9 * f2 + 1.2 * f3 + 0.5 * f4 + 0.7 * f5 + 0.3 * f6