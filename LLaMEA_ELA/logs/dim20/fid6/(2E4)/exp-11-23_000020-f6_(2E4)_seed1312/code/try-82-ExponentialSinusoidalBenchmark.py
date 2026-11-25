import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency and decay parameters for each dimension
        self.freqs = np.linspace(1.0, 10.0, dim)
        self.decays = np.linspace(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Exponential decay component with dimension-wise varying rates
        exp_decay = np.sum(np.exp(-self.decays * np.abs(x_norm)) * np.cos(self.freqs * x_norm))
        
        # Sinusoidal interference pattern with multiple frequencies and amplitudes
        sin_interference = np.sum(np.sin(2 * np.pi * x_norm) + 
                                0.5 * np.sin(4 * np.pi * x_norm) + 
                                0.3 * np.sin(6 * np.pi * x_norm) +
                                0.1 * np.sin(8 * np.pi * x_norm))
        
        # Radial basis function with adaptive bandwidth and phase shift
        rbf = np.sum(np.exp(-0.5 * (x_norm**2)) * np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Multi-scale harmonic modulation with varying amplitudes
        harmonic_mod = np.sum((1 + 0.5 * np.sin(3 * x_norm)) * 
                             (1 + 0.3 * np.cos(7 * x_norm)) * 
                             (1 + 0.2 * np.sin(11 * x_norm)))
        
        # Cross-term coupling with exponential weighting
        cross_coupling = np.sum(np.exp(-0.1 * np.abs(x_norm)) * 
                               np.sin(2 * x_norm) * np.cos(3 * x_norm))
        
        # Asymmetric penalty term for large values
        penalty = np.sum(10 * (x_norm**2) * (x_norm > 0) + 5 * (x_norm**2) * (x_norm <= 0))
        
        # Combine all components with carefully tuned weights
        return 0.3 * exp_decay + 0.25 * sin_interference + 0.2 * rbf + 0.15 * harmonic_mod + 0.08 * cross_coupling + 0.02 * penalty + 1.0