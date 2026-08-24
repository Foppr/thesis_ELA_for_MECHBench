import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine-wave components with dynamic frequencies
        freqs = np.arange(1, self.dim + 1) * (1 + 0.5 * np.sin(x_norm))
        chaotic_sine = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Adaptive scaling with exponential interaction terms
        adaptive = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 + 0.3 * np.sin(x_norm[i] * x_norm[j])
                adaptive += scale * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Multimodal structure with logarithmic and polynomial components
        multimodal = np.sum(np.log(1 + np.abs(x_norm)) * (np.sin(10 * x_norm)**2 + np.cos(10 * x_norm)**2))
        
        # Cross-term with phase-shifted trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:] + 0.3) * np.cos(x_norm[:-1] - x_norm[1:] + 0.7))
        
        # Dynamic global optimum with chaotic perturbation
        dynamic_opt = np.sum(np.sin(15 * x_norm)**2 + np.cos(15 * x_norm)**2 + 0.2 * np.sin(40 * x_norm))
        
        # Additional chaotic component with varying amplitude
        chaotic_component = np.sum(np.sin(20 * x_norm) * np.cos(10 * x_norm) * np.exp(-0.15 * np.abs(x_norm)) * np.sin(8 * x_norm))
        
        # Shifted global optimum with non-uniform scaling
        shift = 0.1 * np.sum((x_norm - 0.2)**2)
        
        # Combine all components with different weights
        return 0.5 * quadratic + 1.8 * chaotic_sine + 1.2 * adaptive + 1.0 * multimodal + 0.7 * cross_term + 1.5 * dynamic_opt + 0.5 * chaotic_component + 0.4 * shift