import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Composite trigonometric components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        trig_comp = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Adaptive scaling with exponential decay interactions
        adaptive = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                scaling = 1.0 / (1.0 + np.exp(-5 * (dist - 0.5)))
                adaptive += scaling * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * (x_norm[i] + x_norm[j]))
        
        # Chaotic perturbation with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            logistic = 4.0 * x_norm[i] * (1.0 - x_norm[i])
            chaotic += np.sin(10 * logistic) * np.cos(7 * logistic) * np.exp(-0.5 * x_norm[i]**2)
        
        # Multimodal nested structure with logarithmic and power scaling
        nested = np.sum(np.log(1 + np.abs(x_norm)) * (np.sin(15 * x_norm)**2 + np.cos(10 * x_norm)**2))
        
        # Cross-term with phase-shifted trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:] + 0.3) * np.cos(x_norm[:-1] - x_norm[1:] + 0.7))
        
        # High-frequency oscillation with non-uniform amplitude modulation
        high_freq = np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * (1.0 + 0.2 * np.sin(10 * x_norm)))
        
        # Shifted global optimum with additional chaotic modulation
        shift = 0.05 * np.sum((x_norm - 0.2)**2 + 0.1 * np.sin(20 * x_norm))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 1.8 * trig_comp + 1.2 * adaptive + 1.0 * chaotic + 0.9 * nested + 0.7 * cross_term + 1.5 * high_freq + 0.4 * shift