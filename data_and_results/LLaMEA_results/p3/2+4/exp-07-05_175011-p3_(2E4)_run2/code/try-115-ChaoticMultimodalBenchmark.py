import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial quadratic base with adaptive conditioning
        r = np.sqrt(np.sum(x_norm**2))
        quadratic = r**2 * (1 + 0.5 * np.sin(5 * r))
        
        # Chaotic phase-shifted sinusoidal components with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        chaotic_phase = np.sum(np.sin(freqs * x_norm + np.sin(3 * x_norm)) * np.cos(freqs * x_norm + np.cos(2 * x_norm)))
        
        # Radial symmetry breaking with exponential decay interactions
        radial_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.1)
                radial_interaction += np.exp(-dist) * np.sin(10 * dist) * np.cos(5 * (x_norm[i] + x_norm[j]))
        
        # Adaptive frequency modulation with chaotic perturbations
        adaptive_freq = np.sum(np.sin(2 * freqs * x_norm + 0.3 * np.sin(7 * x_norm)) * np.cos(freqs * x_norm + 0.2 * np.cos(4 * x_norm)))
        
        # Multimodal structure with radial peaks and cross-term coupling
        peaks = np.sum(np.exp(-5 * (x_norm - np.sin(x_norm))**2) * np.sin(8 * x_norm)**2)
        
        # Cross-term with radial coupling and phase modulation
        cross_term = np.sum(np.sin(x_norm[:-1] * x_norm[1:] + 0.5 * np.sin(x_norm[:-1] + x_norm[1:])) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Global optimum shift with chaotic scaling
        shift = 0.2 * np.sum((x_norm - 0.2 * np.sin(x_norm))**2)
        
        # Combine all components with dynamic weights
        return 1.2 * quadratic + 1.8 * chaotic_phase + 1.0 * radial_interaction + 0.9 * adaptive_freq + 1.5 * peaks + 0.7 * cross_term + 0.4 * shift