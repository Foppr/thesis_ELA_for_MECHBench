import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine couplings between dimensions
        chaotic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j] * (1 + 0.1 * np.sin(x[i] + x[j]))) * np.exp(-0.1 * (x[i] - x[j])**2)
                chaotic_coupling += coupling
        
        # Adaptive Gaussian peaks with position-dependent heights
        gaussian_peaks = 0
        for i in range(self.dim):
            peak_height = 1.2 + 0.3 * np.sin(0.3 * x[i])  # Slightly increased base height
            peak_width = 0.7 + 0.3 * np.cos(0.4 * x[i])   # Slightly decreased width
            gaussian_peaks += peak_height * np.exp(-0.5 * (x[i] / peak_width)**2)
        
        # Fractal-like gradient modulation with recursive scaling
        fractal_modulation = 0
        for i in range(self.dim):
            scale = 1.2 + 0.2 * np.sin(0.5 * x[i])  # Slightly increased scale
            mod_term = np.sin(scale * x[i]) * np.cos(scale * x[i]**2) * np.exp(-0.05 * x[i]**2)
            fractal_modulation += mod_term
        
        # Dynamic multi-modal structure with varying frequencies
        multimodal = 0
        for i in range(self.dim):
            freq1 = 2.5 + 1.0 * np.sin(0.2 * x[i])  # Increased frequency base
            freq2 = 3.5 + 1.5 * np.cos(0.3 * x[i]**2)  # Increased frequency base
            multimodal += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.tanh(x[i])
        
        # Cross-dimensional interaction with cosine-based coupling
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling = np.cos(dist * (1 + 0.2 * np.sin(x[i] + x[j]))) * np.exp(-0.1 * dist**2)
                cross_interaction += coupling
        
        # Asymmetric conditioning with dimension-dependent scaling
        conditioning = 1.0 + 0.15 * np.sin(self.dim * 0.5) + 0.07 * np.cos(self.dim * 0.3)  # Increased conditioning
        
        # Combine all components with optimized weights
        return conditioning * (0.25 * chaotic_coupling + 0.3 * gaussian_peaks + 
                              0.18 * fractal_modulation + 0.17 * multimodal + 0.07 * cross_interaction)