import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like basin term with higher-order polynomial and chaotic scaling
        basin = 0.3 * np.sum(x**6) + 0.2 * np.sum(np.sin(5.0 * x)**2) + 0.1 * np.sum(np.cos(3.0 * x)**2)
        
        # Modified sine-cosine wave interactions with varying frequencies and amplitudes
        wave_terms = 0.0
        for i in range(self.dim):
            wave_terms += 5.0 * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i]) + \
                         3.0 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + \
                         1.5 * np.sin(6.0 * x[i]) + \
                         0.8 * np.cos(4.5 * x[i])
        
        # Enhanced cross-dimensional coupling with higher frequency interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.5 * np.sin(3.0 * x[i]) * np.cos(3.5 * x[j]) + \
                              0.4 * np.cos(4.0 * x[i]) * np.sin(3.0 * x[j]) + \
                              0.3 * np.sin(2.5 * x[i]) * np.sin(4.0 * x[j])
        
        # Additional chaotic noise term with higher frequency components
        noise = 0.08 * np.sum(np.sin(9.0 * x) * np.cos(7.0 * x) + np.cos(8.0 * x) * np.sin(4.0 * x))
        
        return basin + wave_terms + cross_terms + noise