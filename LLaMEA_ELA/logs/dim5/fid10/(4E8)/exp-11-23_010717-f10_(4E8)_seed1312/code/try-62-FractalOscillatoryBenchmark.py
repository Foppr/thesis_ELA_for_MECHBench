import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal basin terms with exponential scaling
        basin = 0.05 * np.sum(x**2) + 0.02 * np.sum(np.exp(-x**2) * np.sin(5.0 * x)**2)
        
        # Multi-frequency oscillatory wave interactions with varying amplitudes
        wave_terms = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        amplitudes = [2.0, 1.5, 1.0, 0.7, 0.5]
        for i in range(self.dim):
            for freq, amp in zip(frequencies, amplitudes):
                wave_terms += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Asymmetric cross-dimensional coupling with fractal-like scaling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling: different weights for i->j and j->i
                cross_terms += 0.2 * np.sin(1.5 * x[i]) * np.cos(2.5 * x[j]) + \
                              0.15 * np.sin(2.0 * x[j]) * np.cos(1.8 * x[i])
        
        # Add a self-similar noise term with fractal scaling
        noise = 0.02 * np.sum(np.sin(6.0 * x) * np.cos(3.0 * x) * np.exp(-x**2))
        
        return basin + wave_terms + cross_terms + noise