import numpy as np

class MultimodalFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like basin term with varying exponents
        basin = 0.0
        for i in range(self.dim):
            basin += 0.1 * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.05 * x[i])
        
        # Chaotic sine-cosine interactions with fractal-like frequency modulation
        chaotic_terms = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            chaotic_terms += 3.0 * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) + \
                            1.5 * np.sin(2.0 * freq_mod * x[i]) * np.cos(1.5 * freq_mod * x[i])
        
        # Cross-dimensional coupling with fractal-like interaction strength
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_strength = 0.5 + 0.2 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[j])
                cross_terms += interaction_strength * np.sin(0.7 * x[i] + 0.3 * x[j]) * np.cos(0.5 * x[i] - 0.2 * x[j])
        
        # Add a small fractal noise term
        noise = 0.01 * np.sum(np.sin(7 * x) * np.cos(4 * x) * np.sin(3 * x))
        
        return basin + chaotic_terms + cross_terms + noise