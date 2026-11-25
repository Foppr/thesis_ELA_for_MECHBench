import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator interactions with complex coupling
        quantum_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j] * (1 + 0.2 * np.sin(x[i]**2 + x[j]**2))) * \
                          np.cos(0.5 * (x[i] - x[j])**2) * \
                          np.exp(-0.05 * (x[i]**2 + x[j]**2))
                quantum_interaction += coupling
        
        # Adaptive fractal Gaussian peaks with dynamic scaling
        fractal_gaussians = 0
        for i in range(self.dim):
            peak_height = 1.5 + 0.8 * np.sin(0.4 * x[i] + self.dim * 0.1)
            peak_width = 1.0 + 0.3 * np.cos(0.6 * x[i])
            gaussian_term = peak_height * np.exp(-0.5 * (x[i] / peak_width)**2)
            fractal_gaussians += gaussian_term
        
        # Dynamic fractal gradient modulation with recursive sine-cosine patterns
        fractal_modulation = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.2)
            mod_term = np.sin(scale_factor * x[i]) * \
                      np.cos(scale_factor * x[i]**2) * \
                      np.sin(scale_factor * x[i]**3) * \
                      np.exp(-0.1 * x[i]**2)
            fractal_modulation += mod_term
        
        # Multi-scale multimodal structure with time-varying frequencies
        multimodal = 0
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * np.sin(0.1 * x[i] + self.dim * 0.15)
            freq2 = 4.0 + 3.0 * np.cos(0.2 * x[i]**2 + self.dim * 0.1)
            freq3 = 2.5 + 1.5 * np.sin(0.3 * x[i] * self.dim)
            multimodal += np.sin(freq1 * x[i]) * \
                         np.cos(freq2 * x[i]) * \
                         np.tanh(freq3 * x[i])
        
        # Cross-dimensional coupling with hyperbolic and exponential interactions
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                coupling = np.tanh(dist * (1 + 0.3 * np.sin(x[i] + x[j]))) * \
                          np.exp(-0.2 * dist**2) * \
                          np.cos(0.5 * dist)
                cross_interaction += coupling
        
        # Asymmetric conditioning with dynamic dimensionality-dependent scaling
        conditioning = 1.0 + 0.2 * np.sin(self.dim * 0.4) + 0.15 * np.cos(self.dim * 0.3) + \
                      0.08 * np.sin(self.dim * 0.6)
        
        # Add chaotic perturbations to increase landscape complexity
        chaos_perturbation = 0
        for i in range(self.dim):
            chaos_perturbation += np.sin(13.0 * x[i]) * np.cos(7.0 * x[i]**2) * \
                                np.tanh(5.0 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Combine all components with optimized weights
        return conditioning * (0.25 * quantum_interaction + 0.3 * fractal_gaussians + 
                              0.2 * fractal_modulation + 0.15 * multimodal + 0.1 * cross_interaction +
                              0.05 * chaos_perturbation)