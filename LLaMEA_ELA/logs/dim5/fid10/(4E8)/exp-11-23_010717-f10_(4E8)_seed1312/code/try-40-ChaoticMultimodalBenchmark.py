import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like basin term with chaotic scaling
        basin = 0.1 * np.sum(x**2) + 0.05 * np.sum(np.sin(3.0 * x)**2)
        
        # Chaotic sine-cosine wave interactions with varying frequencies
        wave_terms = 0.0
        for i in range(self.dim):
            wave_terms += 3.0 * np.sin(1.5 * x[i]) * np.cos(2.0 * x[i]) + \
                         1.5 * np.sin(2.5 * x[i]) * np.cos(1.0 * x[i]) + \
                         0.8 * np.sin(4.0 * x[i])
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.3 * np.sin(1.2 * x[i]) * np.cos(1.8 * x[j]) + \
                              0.2 * np.cos(2.0 * x[i]) * np.sin(1.5 * x[j])
        
        # Add a chaotic noise term
        noise = 0.03 * np.sum(np.sin(7.0 * x) * np.cos(4.0 * x))
        
        return basin + wave_terms + cross_terms + noise