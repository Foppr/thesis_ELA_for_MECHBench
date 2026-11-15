import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested harmonic oscillations with varying frequencies
        harmonics = np.sum(np.sin(2 ** np.arange(1, self.dim + 1) * np.pi * x_norm))
        
        # Radial polynomial barrier with increasing degree
        radial_barrier = np.sum((np.linalg.norm(x_norm, axis=0) ** 2 + 0.01) ** 3)
        
        # Cross-dimensional interaction terms using product of sinusoids
        cross_interaction = np.sum(np.prod(np.sin(4 * np.pi * x_norm), axis=0))
        
        # Asymmetric multimodal peaks with varying scales
        peaks = np.sum(np.exp(-0.5 * ((x_norm - 0.3)**2 / 0.05 + (x_norm + 0.3)**2 / 0.1)) * 
                      np.cos(10 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Conditional conditioning via exponential modulation
        conditioning = np.sum(np.exp(2 * np.abs(x_norm)) * np.cos(5 * np.pi * x_norm))
        
        # Combine all components with adaptive weights
        return 0.3 * harmonics + 0.25 * radial_barrier + 0.2 * cross_interaction + 0.15 * peaks + 0.1 * conditioning