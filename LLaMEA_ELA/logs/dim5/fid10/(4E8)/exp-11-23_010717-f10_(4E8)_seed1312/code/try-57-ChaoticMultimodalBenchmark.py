import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like basin term with chaotic scaling and higher-order polynomials
        basin = 0.2 * np.sum(x**2) + 0.1 * np.sum(np.sin(5.0 * x)**2) + 0.05 * np.sum(x**4)
        
        # Multi-frequency sine-cosine wave interactions with exponential growth
        wave_terms = 0.0
        for i in range(self.dim):
            wave_terms += 5.0 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + \
                         2.5 * np.sin(4.0 * x[i]) * np.cos(1.5 * x[i]) + \
                         1.2 * np.sin(6.0 * x[i]) + \
                         0.8 * np.sin(3.5 * x[i])**3
        
        # Strong cross-dimensional coupling with chaotic interaction coefficients
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.5 * np.sin(2.5 * x[i]) * np.cos(3.0 * x[j]) + \
                              0.4 * np.cos(3.5 * x[i]) * np.sin(2.0 * x[j]) + \
                              0.3 * np.sin(1.8 * x[i]) * np.sin(2.2 * x[j]) + \
                              0.2 * np.cos(1.5 * x[i]) * np.cos(2.5 * x[j])
        
        # Enhanced chaotic noise term with multiple frequencies
        noise = 0.05 * np.sum(np.sin(8.0 * x) * np.cos(5.0 * x) + np.sin(6.0 * x)**2)
        
        return basin + wave_terms + cross_terms + noise