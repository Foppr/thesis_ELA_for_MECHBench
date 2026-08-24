import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        chaotic = np.sum(np.sin(freqs * x_norm * np.exp(-0.1 * x_norm**2)) * np.cos(freqs * x_norm * np.exp(-0.05 * x_norm**2)))
        
        # Exponential decay interaction terms with chaotic modulation
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * (x_norm[i] - x_norm[j]) * np.cos(0.5 * (x_norm[i] + x_norm[j])))
        
        # Nested multimodal structure with chaotic scaling
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(10 * x_norm * np.exp(-0.2 * np.abs(x_norm)))**2)
        
        # Cross-term with chaotic trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:] * np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2))) * np.cos(x_norm[:-1] - x_norm[1:] * np.exp(-0.05 * (x_norm[:-1]**2 + x_norm[1:]**2))))
        
        # Global optimum at origin with chaotic high-frequency oscillation
        high_freq = np.sum(np.sin(15 * x_norm * np.exp(-0.3 * x_norm**2))**2 + np.cos(15 * x_norm * np.exp(-0.3 * x_norm**2))**2)
        
        # Additional chaotic cross-dimensional interaction
        cross_dim = np.sum(np.sin(3 * np.sum(x_norm**2)) * np.cos(2 * np.prod(x_norm)))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 2.0 * chaotic + 1.5 * exp_interaction + 1.0 * nested + 0.8 * cross_term + 1.8 * high_freq + 0.6 * cross_dim