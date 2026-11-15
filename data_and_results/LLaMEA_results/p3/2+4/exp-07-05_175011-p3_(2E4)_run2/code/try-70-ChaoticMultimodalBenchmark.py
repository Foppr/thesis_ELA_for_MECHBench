import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine-wave components with varying amplitudes and frequencies
        freqs = np.arange(1, self.dim + 1)
        chaotic_sine = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * np.sin(3 * x_norm))
        
        # Perturbed Gaussian interaction terms with dynamic weights
        gaussian_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x_norm[i]**2 + x_norm[j]**2)
                gaussian_interaction += np.exp(-0.2 * dist) * np.sin(5 * (x_norm[i] - x_norm[j])) * np.cos(2 * (x_norm[i] + x_norm[j]))
        
        # Nested multimodal structure with hyperbolic scaling
        nested = np.sum(np.arctan(x_norm) * np.sin(8 * x_norm)**2)
        
        # Cross-term with chaotic trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Slightly shifted global optimum with enhanced chaotic oscillation
        chaotic_freq = np.sum(np.sin(20 * x_norm) * np.cos(20 * x_norm))
        
        # Combine all components with different weights
        return 0.4 * quadratic + 1.8 * chaotic_sine + 1.2 * gaussian_interaction + 1.0 * nested + 0.8 * cross_term + 1.5 * chaotic_freq