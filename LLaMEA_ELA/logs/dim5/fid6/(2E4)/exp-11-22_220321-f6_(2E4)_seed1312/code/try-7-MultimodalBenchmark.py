import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal perturbations with varying frequencies
        chaotic_perturbation = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barriers to create rugged landscape
        barrier_term = np.sum(np.exp(-5 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Additional high-frequency oscillations
        high_freq_osc = np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled))
        
        # Combine all terms with different weights
        return quadratic + 0.5 * chaotic_perturbation + 0.3 * barrier_term + 0.1 * high_freq_osc