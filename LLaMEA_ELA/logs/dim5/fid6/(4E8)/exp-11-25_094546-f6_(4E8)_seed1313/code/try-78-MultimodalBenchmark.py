import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested exponential decay with chaotic modulation
        exp_decay = np.sum(np.exp(-np.abs(x_norm)**(1.8 + 0.4 * np.sin(25 * x_norm))) * 
                          (1.0 + 0.3 * np.sin(17 * x_norm)))
        
        # Adaptive radial barriers with fractal scaling
        radial_barrier = np.sum((1.0 + 0.5 * np.sin(8 * np.pi * x_norm)) * 
                               np.exp(-0.5 * (x_norm**2) / (0.1 + 0.2 * np.abs(x_norm))))
        
        # Multi-scale sinusoidal interference with varying amplitudes
        sin_interfere = np.sum(
            1.2 * np.sin(15 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) +
            0.8 * np.sin(23 * np.pi * x_norm**1.3) * np.cos(14 * np.pi * x_norm**1.7) +
            0.5 * np.sin(31 * np.pi * x_norm**0.9) * np.cos(19 * np.pi * x_norm**1.2)
        )
        
        # Cross-dimensional coupling with chaotic phase shifts
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            phase_shift = 0.5 * np.sin(np.pi * (x_norm[i] + x_norm[i+1]))
            cross_coupling += np.sin(np.pi * (x_norm[i] - x_norm[i+1]) + phase_shift) * \
                             np.cos(np.pi * (x_norm[i] + x_norm[i+1]) + phase_shift)
        
        # Hierarchical energy wells with self-similar structure
        well_structure = np.sum(
            (2.0 + 1.2 * np.sin(5 * x_norm)) * 
            np.exp(-0.3 * (x_norm**2)) * 
            (1.0 + 0.4 * np.cos(20 * x_norm))
        )
        
        # Combine all components with chaotic weight scaling
        return 2.1 * exp_decay + 1.3 * radial_barrier + 0.8 * sin_interfere + \
               0.4 * cross_coupling + 1.7 * well_structure