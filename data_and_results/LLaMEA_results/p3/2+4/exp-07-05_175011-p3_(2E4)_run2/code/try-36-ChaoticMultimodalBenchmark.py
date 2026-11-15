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
        
        # Exponential decay interaction terms with modified decay rate
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.12 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Nested multimodal structure with logarithmic scaling
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(10 * x_norm)**2)
        
        # Cross-term with trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Global optimum at origin with high-frequency oscillation
        high_freq = np.sum(np.sin(18 * x_norm)**2 + np.cos(18 * x_norm)**2)
        
        # Additional chaotic component with shifted optimum
        shift = 0.15
        chaotic = np.sum(np.sin(22 * (x_norm + shift)) * np.cos(22 * (x_norm + shift)))
        
        # Modified harmonic interaction term for better conditioning
        harmonic = np.sum(np.sin(7 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.05 * x_norm**2))
        
        # Asymmetric multimodal component to increase challenge
        asym = np.sum(np.abs(x_norm)**1.5 * np.sin(15 * x_norm)**2)
        
        # Combine all components with different weights
        return 0.35 * quadratic + 1.7 * periodic + 1.6 * exp_interaction + 0.85 * nested + 0.65 * cross_term + 1.7 * high_freq + 0.55 * chaotic + 0.4 * harmonic + 0.3 * asym