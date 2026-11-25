import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator interactions with chaotic coupling
        quantum_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j] * (1 + 0.3 * np.sin(x[i]**2 + x[j]**2))) * \
                          np.cos(0.5 * (x[i] - x[j])**2) * \
                          np.exp(-0.07 * (x[i]**2 + x[j]**2)) * \
                          np.tanh(0.1 * x[i] * x[j])
                quantum_interaction += coupling
        
        # Adaptive fractal Gaussian peaks with dynamic scaling and chaotic modulation
        fractal_gaussians = 0
        for i in range(self.dim):
            peak_height = 2.0 + 1.2 * np.sin(0.5 * x[i] + self.dim * 0.15)
            peak_width = 1.2 + 0.4 * np.cos(0.7 * x[i])
            gaussian_term = peak_height * np.exp(-0.5 * (x[i] / peak_width)**2) * \
                           (1 + 0.2 * np.sin(self.dim * 0.3 * x[i]))
            fractal_gaussians += gaussian_term
        
        # Dynamic fractal gradient modulation with recursive sine-cosine patterns and chaotic perturbations
        fractal_modulation = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.6 * np.sin(0.4 * x[i] + self.dim * 0.25)
            mod_term = np.sin(scale_factor * x[i]) * \
                      np.cos(scale_factor * x[i]**2) * \
                      np.sin(scale_factor * x[i]**3) * \
                      np.exp(-0.15 * x[i]**2) * \
                      (1 + 0.1 * np.cos(0.8 * x[i]))
            fractal_modulation += mod_term
        
        # Multi-scale multimodal structure with time-varying frequencies and chaotic sine-cosine interactions
        multimodal = 0
        for i in range(self.dim):
            freq1 = 4.0 + 3.0 * np.sin(0.15 * x[i] + self.dim * 0.2)
            freq2 = 5.0 + 4.0 * np.cos(0.25 * x[i]**2 + self.dim * 0.15)
            freq3 = 3.0 + 2.0 * np.sin(0.35 * x[i] * self.dim)
            multimodal += np.sin(freq1 * x[i]) * \
                         np.cos(freq2 * x[i]) * \
                         np.tanh(freq3 * x[i]) * \
                         np.exp(-0.05 * x[i]**2) * \
                         (1 + 0.15 * np.sin(0.5 * x[i]))
        
        # Cross-dimensional coupling with hyperbolic and exponential interactions, enhanced with chaotic terms
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                coupling = np.tanh(dist * (1 + 0.4 * np.sin(x[i] + x[j]))) * \
                          np.exp(-0.25 * dist**2) * \
                          np.cos(0.5 * dist) * \
                          (1 + 0.1 * np.cos(0.3 * dist))
                cross_interaction += coupling
        
        # Asymmetric conditioning with dynamic dimensionality-dependent scaling and chaotic perturbations
        conditioning = 1.2 + 0.3 * np.sin(self.dim * 0.5) + 0.2 * np.cos(self.dim * 0.4) + \
                      0.1 * np.sin(self.dim * 0.7) + 0.05 * np.cos(self.dim * 0.6)
        
        # Combine all components with optimized weights
        return conditioning * (0.3 * quantum_interaction + 0.25 * fractal_gaussians + 
                              0.2 * fractal_modulation + 0.15 * multimodal + 0.1 * cross_interaction)