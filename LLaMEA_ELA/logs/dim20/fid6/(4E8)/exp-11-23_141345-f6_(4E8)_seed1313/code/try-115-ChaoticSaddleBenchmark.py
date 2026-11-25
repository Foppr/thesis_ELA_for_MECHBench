import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with cubic and quartic terms
        poly_term = np.sum(0.8 * x**4 + 1.2 * x**3 - 0.5 * x**2 + 0.3 * x + 0.05)
        
        # Modified sinusoidal modulation with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(1.5 * x) * np.cos(0.7 * x))
        
        # Improved fractal-like scaling with logarithmic components (slightly modified)
        fractal_term = np.sum(np.abs(x) ** (1.45 + 0.25 * np.sin(4.0 * x)) + 0.12 * np.log(1.0 + np.abs(x)))
        
        # Enhanced multi-scale geometric interactions with Gaussian kernels (adjusted weight)
        geo_term = np.sum(np.exp(-0.22 * (x[:-1] - x[1:]) ** 2) * (x[:-1]**2 + x[1:]**2))
        
        # Modified chaotic saddle-point component with hyperbolic tangent scaling
        chaotic_term = np.sum(np.tanh(2.0 * x) * np.exp(-0.32 * x**2) * np.cos(3.0 * x))
        
        # Enhanced cross-dimensional coupling with asymmetric and non-linear interactions (modified)
        cross_term = np.sum(x[:-1] * np.sin(1.6 * x[1:]) + x[1:] * np.cos(2.1 * x[:-1]) + 0.12 * x[:-1] * x[1:])
        
        # Improved high-frequency oscillation with variable amplitude modulation
        high_freq_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * (1.0 + 0.22 * np.sin(3.0 * x)) * np.exp(-0.11 * x**2))
        
        # Combined function with optimized weights for better fitness performance
        return 0.26 * poly_term + 0.21 * sin_term + 0.19 * fractal_term + 0.13 * geo_term + 0.11 * chaotic_term + 0.09 * cross_term + 0.08 * high_freq_term