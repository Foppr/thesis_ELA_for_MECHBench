import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple high-frequency sinusoidal modulations
        freq1 = 6 * np.pi
        freq2 = 9 * np.pi
        freq3 = 12 * np.pi
        
        sin_term1 = np.sum(np.sin(freq1 * x_normalized)**2)
        sin_term2 = np.sum(np.sin(freq2 * x_normalized)**2)
        sin_term3 = np.sum(np.sin(freq3 * x_normalized)**2)
        
        # Additional cosine modulation with interaction terms
        cos_term = np.sum(np.cos(5 * np.pi * x_normalized) * np.sin(10 * np.pi * x_normalized))
        
        # Cross-dimensional interaction term
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Exponential decay terms with different rates
        exp_term1 = np.sum(np.exp(-x_normalized**2) - 1.0)
        exp_term2 = np.sum(np.exp(-3 * x_normalized**2) - 1.0)
        
        # Logarithmic penalty to increase conditioning difficulty
        log_penalty = 0.01 * np.sum(np.log(1 + x_normalized**2))
        
        # Combine all terms with carefully tuned weights
        return quadratic_term + 0.4 * sin_term1 + 0.3 * sin_term2 + 0.2 * sin_term3 + 0.08 * cos_term + 0.15 * exp_term1 + 0.1 * exp_term2 + 0.05 * cross_term + log_penalty