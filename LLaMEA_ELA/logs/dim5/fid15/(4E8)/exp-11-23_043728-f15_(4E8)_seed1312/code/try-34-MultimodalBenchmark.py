import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Enhanced quadratic term with exponential scaling
        quadratic_term = np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # Highly oscillatory sinusoidal terms with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(15 * np.pi * x_norm)**2 + 0.5 * np.sin(30 * np.pi * x_norm)**2)
        
        # Complex polynomial interactions with exponential weights
        poly_term = np.sum(np.exp(3 * np.abs(x_norm)) * x_norm**4) + 0.2 * np.sum(x_norm**6)
        
        # Cross-dimensional coupling with exponential interaction strength
        interaction_term = np.sum(np.exp(5 * np.abs(x_norm[:-1] + x_norm[1:])) * (x_norm[:-1] + x_norm[1:])**2)
        
        # Chaotic phase shifts with non-uniform distribution
        phase_shifts = np.sin(np.pi * np.arange(self.dim) / self.dim)
        shifted_term = np.sum(np.sin(5 * np.pi * (x_norm + 0.3 * phase_shifts))**2)
        
        # Additional chaotic coupling between all dimensions
        chaotic_coupling = 0.1 * np.sum((np.sin(x_norm * np.pi) + np.cos(x_norm * np.pi))**4)
        
        # Combine all terms with carefully tuned weights to create a highly complex landscape
        return quadratic_term + 0.8 * sin_term + 0.02 * poly_term + 0.5 * interaction_term + 0.6 * shifted_term + chaotic_coupling