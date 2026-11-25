import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine couplings with increased nonlinearity
        chaotic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j] * (1 + 0.2 * np.sin(x[i] + x[j] + 0.1 * x[i]**2))) * np.exp(-0.15 * (x[i] - x[j])**2)
                chaotic_coupling += coupling
        
        # Shifted Gaussian peaks with dynamic position-dependent heights
        gaussian_peaks = 0
        for i in range(self.dim):
            peak_height = 1.2 + 0.3 * np.sin(0.4 * x[i] + 1.0)
            peak_width = 0.9 + 0.1 * np.cos(0.5 * x[i] - 0.5)
            gaussian_peaks += peak_height * np.exp(-0.5 * ((x[i] - 0.5) / peak_width)**2)
        
        # Modified fractal-like gradient modulation with different scaling
        fractal_modulation = 0
        for i in range(self.dim):
            scale = 1.2 + 0.2 * np.sin(0.6 * x[i] + 0.3)
            mod_term = np.sin(scale * x[i]) * np.cos(scale * x[i]**1.5) * np.exp(-0.08 * x[i]**2)
            fractal_modulation += mod_term
        
        # Dynamic multi-modal structure with varying frequencies and added hyperbolic terms
        multimodal = 0
        for i in range(self.dim):
            freq1 = 2.5 + 1.0 * np.sin(0.25 * x[i])
            freq2 = 3.5 + 1.5 * np.cos(0.35 * x[i]**2)
            multimodal += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.tanh(x[i]) * np.cosh(0.1 * x[i])
        
        # Cross-dimensional interaction with modified cosine coupling and additional exponential term
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling = np.cos(dist * (1 + 0.3 * np.sin(x[i] + x[j] + 0.2 * x[i]*x[j]))) * np.exp(-0.15 * dist**2) * np.sin(0.1 * x[i])
                cross_interaction += coupling
        
        # Asymmetric conditioning with dimension-dependent scaling and added sine modulation
        conditioning = 1.0 + 0.15 * np.sin(self.dim * 0.5 + 0.2) + 0.08 * np.cos(self.dim * 0.3 - 0.1)
        
        # Combine all components with adjusted weights
        return conditioning * (0.35 * chaotic_coupling + 0.2 * gaussian_peaks + 
                              0.25 * fractal_modulation + 0.1 * multimodal + 0.1 * cross_interaction)