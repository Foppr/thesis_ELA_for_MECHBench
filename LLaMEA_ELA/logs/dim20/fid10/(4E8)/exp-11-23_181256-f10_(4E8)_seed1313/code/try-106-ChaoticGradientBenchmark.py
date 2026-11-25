import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic logistic map component for non-linearity
        chaos = np.sum(4 * x_norm * (1 - x_norm))
        
        # Multi-scale harmonic oscillations with varying amplitudes
        harmonics = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(4 * np.pi * x_norm) + 
                          0.3 * np.sin(8 * np.pi * x_norm))
        
        # Saddle point inducing term with hyperbolic tangent
        saddle = np.sum(np.tanh(x_norm) * x_norm**2)
        
        # Radial component with exponential decay and periodic modulation
        radial = np.sum(np.exp(-0.5 * x_norm**2) * (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Cross-terms creating complex interaction patterns
        cross = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(x_norm[:-1] + x_norm[1:]))
        
        # Asymmetric barrier with varying steepness
        barrier = np.sum(0.5 * (x_norm + 0.1)**2 + 0.3 * np.abs(x_norm))
        
        # Combined function with diverse curvature and mixed extrema types
        return 2.0 * chaos + 1.5 * harmonics + 0.8 * saddle + 0.6 * radial + 0.4 * cross + 0.3 * barrier