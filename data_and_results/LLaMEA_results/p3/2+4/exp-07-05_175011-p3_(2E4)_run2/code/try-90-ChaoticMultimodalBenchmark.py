import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Periodic sinusoidal components with increasing frequency
        freqs = np.arange(1, self.dim + 1)
        periodic = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Exponential decay interaction terms with enhanced coupling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.07 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(8 * (x_norm[i] - x_norm[j])) * np.cos(4 * (x_norm[i] + x_norm[j]))
        
        # Nested multimodal structure with logarithmic scaling and additional chaos
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(13 * x_norm)**2 + np.cos(9 * x_norm)**2)
        
        # Cross-term with trigonometric interaction and phase shift
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:] + 0.6) * np.cos(x_norm[:-1] - x_norm[1:] - 0.4))
        
        # Global optimum at origin with high-frequency oscillation and chaotic perturbation
        high_freq = np.sum(np.sin(22 * x_norm)**2 + np.cos(22 * x_norm)**2 + 0.35 * np.sin(55 * x_norm))
        
        # Additional chaotic component with non-uniform scaling
        chaotic = np.sum(np.sin(27 * x_norm) * np.cos(16 * x_norm) * np.exp(-0.22 * np.abs(x_norm)))
        
        # Combine all components with different weights
        return 0.45 * quadratic + 2.1 * periodic + 1.6 * exp_interaction + 1.1 * nested + 0.85 * cross_term + 1.9 * high_freq + 0.65 * chaotic