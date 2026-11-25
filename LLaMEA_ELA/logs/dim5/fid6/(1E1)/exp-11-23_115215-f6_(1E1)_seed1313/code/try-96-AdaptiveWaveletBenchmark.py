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
        
        # Wavelet-like trigonometric terms with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += self.wavelet_ampls[i] * np.sin(self.wavelet_freqs[i] * x[i]) * \
                     np.cos(self.wavelet_freqs[i] * x[i] * 0.7) + \
                     0.3 * np.sin(self.wavelet_freqs[i] * x[i] * 2.0)
        
        # Adaptive noise terms that depend on the current solution
        for i in range(self.dim):
            noise = self.noise_levels[i] * np.random.uniform(-1.0, 1.0)
            f_val += noise * (1.0 + 0.5 * np.sin(x[i]))
        
        # Cross-dimensional polynomial interactions with varying exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                exponent = 1.0 + 0.5 * np.sin(i * 0.5)
                f_val += 0.2 * (x[i]**exponent) * (x[j]**(3.0 - exponent)) + \
                         0.1 * np.cos(x[i] + x[j])
        
        # Asymmetric coupling terms with distance-dependent weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = 1.0 / (1.0 + dist**2)
                f_val += weight * (np.sin(x[i]) * np.cos(x[j]) + 
                                   np.cos(x[i]) * np.sin(x[j]))
        
        # Global sinusoidal modulation with dynamic phase
        phase = np.sum(np.sin(x)) * 0.3
        f_val += 0.5 * np.sin(np.sum(x) + phase) * \
                 np.cos(np.sum(x**2) * 0.1)
        
        # Non-linear scaling based on dimensionality
        f_val *= (1.0 + 0.2 * np.log(self.dim + 1))
        
        return f_val