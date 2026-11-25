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
        harmonics = np.sum(np.sin(2.5 * np.pi * x_norm) + 0.6 * np.sin(3.8 * np.pi * x_norm) + 
                          0.25 * np.sin(7.2 * np.pi * x_norm))
        
        # Saddle point inducing term with hyperbolic tangent
        saddle = np.sum(np.tanh(x_norm) * x_norm**2)
        
        # Radial component with exponential decay and periodic modulation
        radial = np.sum(np.exp(-0.4 * x_norm**2) * (1 + 0.15 * np.cos(2.7 * x_norm)))
        
        # Cross-terms creating complex interaction patterns
        cross = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(1.3 * (x_norm[:-1] + x_norm[1:])))
        
        # Asymmetric barrier with varying steepness
        barrier = np.sum(0.4 * (x_norm + 0.12)**2 + 0.25 * np.abs(x_norm))
        
        # Combined function with diverse curvature and mixed extrema types
        return 1.8 * chaos + 1.7 * harmonics + 0.9 * saddle + 0.5 * radial + 0.35 * cross + 0.25 * barrier