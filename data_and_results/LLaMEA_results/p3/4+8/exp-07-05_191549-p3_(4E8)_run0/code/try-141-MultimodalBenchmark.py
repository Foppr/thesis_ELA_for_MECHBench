import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested sinusoidal modulations with varying frequencies and amplitudes
        nested_sin = np.sum(np.sin(15 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                           np.sin(3 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm))
        
        # Radial harmonic potential with multiple harmonic components
        r = np.linalg.norm(x_norm, axis=0)
        radial_harmonic = np.sum((r**2 + 0.1) * np.sin(10 * np.pi * r) * 
                                np.cos(5 * np.pi * r) * np.sin(3 * np.pi * r))
        
        # Cross-dimensional coupling with chaotic interaction terms
        cross_coupling = np.sum(np.sin(8 * np.pi * x_norm) * 
                               np.cos(6 * np.pi * np.roll(x_norm, 1, axis=0)) * 
                               np.sin(4 * np.pi * np.roll(x_norm, 2, axis=0)) * 
                               np.cos(2 * np.pi * np.roll(x_norm, 3, axis=0)))
        
        # Multi-scale exponential barrier with varying decay rates
        barrier = np.sum(np.exp(-3.5 * x_norm**2) * (x_norm**8 + 0.5 * x_norm**6 + 0.3 * x_norm**4 + 0.1 * x_norm**2 + 0.05))
        
        # Asymmetric Gaussian peaks with multi-modal positioning
        gaussian_peaks = np.sum(0.7 * np.exp(-2.5 * (x_norm - 0.3)**2) * 
                               np.sin(13 * np.pi * x_norm) + 
                               0.5 * np.exp(-3.0 * (x_norm + 0.4)**2) * 
                               np.cos(9 * np.pi * x_norm) + 
                               0.4 * np.exp(-2.0 * (x_norm - 0.6)**2) * 
                               np.sin(17 * np.pi * x_norm))
        
        # Chaotic interference with nested frequency modulation
        chaotic_interf = np.sum(np.sin(20 * np.pi * x_norm + 0.5 * np.sin(40 * np.pi * x_norm)) * 
                               np.cos(15 * np.pi * x_norm + 0.3 * np.cos(30 * np.pi * x_norm)) * 
                               np.sin(10 * np.pi * x_norm + 0.2 * np.sin(20 * np.pi * x_norm)))
        
        # Combined objective with optimized weights
        return 0.25 * nested_sin + 0.20 * radial_harmonic + 0.18 * cross_coupling + \
               0.15 * barrier + 0.12 * gaussian_peaks + 0.10 * chaotic_interf