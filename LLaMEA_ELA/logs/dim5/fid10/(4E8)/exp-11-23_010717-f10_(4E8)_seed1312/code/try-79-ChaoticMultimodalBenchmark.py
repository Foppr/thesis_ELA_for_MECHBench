import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like basin term with higher-order polynomial and chaotic scaling
        basin = 0.35 * np.sum(x**6) + 0.25 * np.sum(np.sin(5.0 * x)**3) + 0.15 * np.sum(np.cos(3.0 * x)**3)
        
        # Complex sine-cosine wave interactions with varying frequencies and amplitudes
        wave_terms = 0.0
        for i in range(self.dim):
            wave_terms += 5.5 * np.sin(3.2 * x[i]) * np.cos(2.1 * x[i]) + \
                         3.5 * np.sin(4.2 * x[i]) * np.cos(3.7 * x[i]) + \
                         1.8 * np.sin(6.3 * x[i]) + \
                         0.9 * np.cos(4.7 * x[i]) + \
                         2.3 * np.sin(2.7 * x[i])**2 * np.cos(1.7 * x[i])
        
        # Enhanced cross-dimensional coupling with higher frequency interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.65 * np.sin(3.2 * x[i]) * np.cos(3.7 * x[j]) + \
                              0.55 * np.cos(4.2 * x[i]) * np.sin(3.2 * x[j]) + \
                              0.45 * np.sin(2.7 * x[i]) * np.sin(4.2 * x[j]) + \
                              0.35 * np.cos(2.2 * x[i]) * np.cos(3.7 * x[j])
        
        # Additional chaotic noise term with higher frequency components and fractal-like scaling
        noise = 0.12 * np.sum(np.sin(10.5 * x) * np.cos(7.5 * x) + 
                            np.cos(8.5 * x) * np.sin(4.5 * x) + 
                            np.sin(6.5 * x)**3 * np.cos(5.5 * x)**2)
        
        # Add a global scaling factor to increase the overall landscape complexity
        scaling_factor = 1.0 + 0.25 * np.sum(np.sin(x)**2)
        
        return scaling_factor * (basin + wave_terms + cross_terms + noise)