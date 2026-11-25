import numpy as np

class AdaptiveWaveletBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wavelet parameters
        self.wavelet_freqs = np.random.uniform(0.5, 3.0, dim)
        self.wavelet_ampls = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial landscape
        f_val = np.sum(x**4) * (1.0 + 0.1 * np.sin(np.sum(x)))
        
        # Trigonometric wave components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            f_val += self.wavelet_ampls[i] * (
                np.sin(self.wavelet_freqs[i] * x[i]) + 
                0.5 * np.cos(2.0 * self.wavelet_freqs[i] * x[i]) +
                0.3 * np.sin(3.0 * self.wavelet_freqs[i] * x[i])
            )
        
        # Coupling terms with distance-based weighting
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                weight = 1.0 / (1.0 + dist)
                f_val += weight * (
                    0.5 * np.sin(x[i] * x[j]) + 
                    0.2 * np.cos(x[i] + x[j])
                )
        
        # Polynomial interaction terms with varying degrees
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.3 * (x[i]**2) * (x[j]**3) + \
                         0.2 * np.sin(x[i]) * np.cos(x[j])
        
        # Adaptive noise components
        for i in range(self.dim):
            noise = self.noise_levels[i] * np.random.normal(0, 1)
            f_val += 0.1 * x[i] * noise + \
                     0.05 * np.sin(x[i] * noise)
        
        # Global correlation terms
        f_val += 0.2 * np.sum(np.sin(x)) * np.sum(np.cos(x)) + \
                 0.1 * np.prod(np.sin(x)) + \
                 0.15 * np.abs(np.sum(x**3))
        
        # Asymmetric interactions
        for i in range(1, self.dim):
            f_val += 0.2 * (x[i] - x[i-1])**4 + \
                     0.1 * np.sin(x[i]) * np.cos(x[i-1])
        
        return f_val