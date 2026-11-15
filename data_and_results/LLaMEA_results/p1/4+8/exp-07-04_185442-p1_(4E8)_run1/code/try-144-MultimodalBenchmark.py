import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * (1 + 0.5 * np.sin(5 * x_norm)))
        
        # Polynomial potential with mixed degrees
        poly_potential = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Logarithmic barrier terms to penalize boundary violations
        log_barrier = np.sum(-np.log(1 - x_norm**2 / 25.0 + 1e-10))
        
        # Multi-scale harmonic interactions
        harmonic_interaction = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.1 * np.abs(x_norm[0] - x_norm[1])) * (x_norm[0]**2 + x_norm[1]**2))
        
        # Add a global scaling factor and noise
        noise = 0.01 * np.random.random()
        
        # Combine all components
        return sin_modulation + poly_potential + log_barrier + harmonic_interaction + cross_coupling + noise