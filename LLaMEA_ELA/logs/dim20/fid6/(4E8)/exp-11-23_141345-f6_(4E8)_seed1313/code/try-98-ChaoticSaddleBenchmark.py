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
        
        # Improved fractal-like scaling with logarithmic components
        fractal_term = np.sum(np.abs(x) ** (1.4 + 0.3 * np.sin(4.0 * x)) + 0.1 * np.log(1.0 + np.abs(x)))
        
        # Enhanced multi-scale geometric interactions with Gaussian kernels
        geo_term = np.sum(np.exp(-0.2 * (x[:-1] - x[1:]) ** 2) * (x[:-1]**2 + x[1:]**2))
        
        # Modified chaotic saddle-point component with hyperbolic tangent scaling
        chaotic_term = np.sum(np.tanh(2.0 * x) * np.exp(-0.3 * x**2) * np.cos(3.0 * x))
        
        # Enhanced cross-dimensional coupling with asymmetric and non-linear interactions
        cross_term = np.sum(x[:-1] * np.sin(1.5 * x[1:]) + x[1:] * np.cos(2.0 * x[:-1]) + 0.1 * x[:-1] * x[1:])
        
        # Improved high-frequency oscillation with variable amplitude modulation
        high_freq_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * (1.0 + 0.2 * np.sin(3.0 * x)) * np.exp(-0.1 * x**2))
        
        # Combined function with optimized weights for better fitness performance
        return 0.25 * poly_term + 0.2 * sin_term + 0.18 * fractal_term + 0.12 * geo_term + 0.1 * chaotic_term + 0.08 * cross_term + 0.07 * high_freq_term