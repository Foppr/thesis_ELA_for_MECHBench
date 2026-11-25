import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like basin term with higher-order polynomial and chaotic scaling
        basin = 0.4 * np.sum(x**8) + 0.3 * np.sum(np.sin(6.0 * x)**4) + 0.2 * np.sum(np.cos(4.0 * x)**4)
        
        # Complex sine-cosine wave interactions with varying frequencies and amplitudes
        wave_terms = 0.0
        for i in range(self.dim):
            wave_terms += 6.0 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + \
                         4.0 * np.sin(4.5 * x[i]) * np.cos(4.0 * x[i]) + \
                         2.0 * np.sin(7.0 * x[i]) + \
                         1.0 * np.cos(5.0 * x[i]) + \
                         2.5 * np.sin(3.0 * x[i])**2 * np.cos(2.0 * x[i])
        
        # Enhanced cross-dimensional coupling with higher frequency interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.7 * np.sin(4.0 * x[i]) * np.cos(4.5 * x[j]) + \
                              0.6 * np.cos(5.0 * x[i]) * np.sin(4.0 * x[j]) + \
                              0.5 * np.sin(3.0 * x[i]) * np.sin(5.0 * x[j]) + \
                              0.4 * np.cos(3.0 * x[i]) * np.cos(4.5 * x[j])
        
        # Additional chaotic noise term with higher frequency components and fractal-like scaling
        noise = 0.15 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) + 
                            np.cos(10.0 * x) * np.sin(5.0 * x) + 
                            np.sin(7.0 * x)**4 * np.cos(6.0 * x)**3)
        
        # Novel hybrid fitness aggregation mechanism combining geometric and harmonic means
        geometric_mean = np.prod(np.abs(x) + 1e-10)**(1.0/self.dim) if self.dim > 0 else 0
        harmonic_mean = self.dim / np.sum(1.0 / (np.abs(x) + 1e-10)) if np.any(x != 0) else 0
        
        # Combine all terms with adaptive weighting based on input magnitude
        adaptive_weight = 1.0 + 0.3 * np.mean(np.sin(x)**2)
        
        return adaptive_weight * (basin + wave_terms + cross_terms + noise) + \
               0.5 * (geometric_mean**2 + harmonic_mean**2)