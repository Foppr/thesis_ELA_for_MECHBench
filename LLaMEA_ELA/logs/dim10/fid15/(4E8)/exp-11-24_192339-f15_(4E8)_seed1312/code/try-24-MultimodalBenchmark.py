import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal modulations with varying frequencies and amplitudes
        freq1 = 2 * np.pi
        freq2 = 5 * np.pi
        freq3 = 8 * np.pi
        
        sin_term1 = np.sum(np.sin(freq1 * x_normalized)**2)
        sin_term2 = np.sum(np.sin(freq2 * x_normalized)**2)
        sin_term3 = np.sum(np.sin(freq3 * x_normalized)**2)
        
        # Cosine modulation for additional complexity
        cos_term = np.sum(np.cos(3 * np.pi * x_normalized) * np.sin(7 * np.pi * x_normalized))
        
        # Exponential decay terms to create varied landscape curvature
        exp_term1 = np.sum(np.exp(-x_normalized**2) - 1.0)
        exp_term2 = np.sum(np.exp(-2 * x_normalized**2) - 1.0)
        
        # Novel interaction term between dimensions to increase complexity
        interaction_term = np.sum(x_normalized[:-1] * x_normalized[1:] * np.sin(4 * np.pi * x_normalized[:-1]))
        
        # Combine all terms with carefully tuned weights
        return quadratic_term + 0.3 * sin_term1 + 0.2 * sin_term2 + 0.1 * sin_term3 + 0.05 * cos_term + 0.1 * exp_term1 + 0.05 * exp_term2 + 0.02 * interaction_term