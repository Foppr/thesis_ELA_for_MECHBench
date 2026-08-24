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
        
        # Exponential decay interaction terms with enhanced chaos
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.05 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(7 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Nested multimodal structure with logarithmic scaling and chaotic modulation
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(12 * x_norm)**2 * np.exp(-0.5 * np.abs(x_norm)))
        
        # Cross-term with trigonometric interaction and chaotic perturbation
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]) * np.sin(2 * x_norm[:-1]) * np.cos(2 * x_norm[1:]))
        
        # Global optimum at origin with high-frequency oscillation and chaotic shift
        high_freq = np.sum(np.sin(20 * x_norm)**2 + np.cos(20 * x_norm)**2 + 0.1 * np.sin(50 * x_norm))
        
        # Chaotic modulation term with time-like dependency
        chaotic_mod = np.sum(np.sin(10 * x_norm) * np.cos(10 * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with different weights
        return 0.4 * quadratic + 2.0 * periodic + 1.5 * exp_interaction + 1.1 * nested + 0.8 * cross_term + 1.8 * high_freq + 0.6 * chaotic_mod