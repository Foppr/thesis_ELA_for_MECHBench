import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with different rates and positions
        exp_terms = 0
        decay_rates = np.array([1.0, 2.0, 3.0, 0.5, 1.5])
        peak_positions = np.linspace(-1, 1, 5)
        
        for rate, pos in zip(decay_rates, peak_positions):
            exp_terms += np.exp(-rate * np.abs(x_norm - pos))
            
        # Trigonometric wave terms with varying frequencies
        wave_terms = 0
        frequencies = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        
        for freq in frequencies:
            wave_terms += np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm)
            
        # Combine terms with different weights
        result = 0.4 * exp_terms + 0.6 * wave_terms
        
        # Add a quartic term to create a more complex landscape
        quartic_term = 0.2 * np.sum(x_norm**4)
        
        return result + quartic_term