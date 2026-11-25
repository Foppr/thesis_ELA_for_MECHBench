import numpy as np

class AdaptiveWaveletBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wavelet parameters
        self.wavelet_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.wavelet_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term
        f_val = np.sum(x**4) * 0.1
        
        # Adaptive wavelet components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += self.wavelet_amplitudes[i] * np.sin(self.wavelet_frequencies[i] * x[i]) * \
                     np.cos(self.wavelet_frequencies[i] * x[i] * 0.7) + \
                     0.3 * np.sin(self.wavelet_frequencies[i] * x[i] * 2.0)
        
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f_val += 0.2 * (x[i]**2) * (x[j]**3) * np.sin(x[i] + x[j])
        
        # Trigonometric coupling terms with dynamic phase shifts
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.5 + np.sum(x) * 0.1)
            f_val += 0.25 * np.cos(x[i] * 2.0 + phase_shift) * \
                     np.sin(x[i] * 1.5 + phase_shift) * \
                     (1.0 + 0.2 * np.sin(i * 0.3))
        
        # Adaptive noise modulation based on position
        for i in range(self.dim):
            noise = self.noise_levels[i] * np.random.uniform(-1, 1)
            f_val += noise * np.exp(-0.5 * (x[i] / 2.0)**2) * \
                     np.sin(x[i] * 3.0 + i)
        
        # High-order cross-terms with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                f_val += weight * x[i]**2 * x[j]**4 * np.cos(x[i] - x[j])
        
        # Asymmetric coupling with local minima
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.15 * (diff**3 + 0.2 * np.abs(diff)**1.5) * \
                         np.cos(x[i]) * np.sin(x[i-1])
        
        # Global sinusoidal modulation
        f_val += 0.2 * np.sin(np.sum(x**2) * 0.1) + \
                 0.1 * np.cos(np.prod(x)) * \
                 (1.0 + 0.1 * np.sin(np.sum(x)))
        
        return f_val