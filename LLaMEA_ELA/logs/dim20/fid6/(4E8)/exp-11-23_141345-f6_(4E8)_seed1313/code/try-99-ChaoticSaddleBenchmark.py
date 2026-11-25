import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with varying degrees and cross-terms
        poly_term = np.sum((x**4 + 0.3 * x**3 - 0.4 * x**2 + 0.2 * x - 0.1) ** 2)
        
        # Modified sinusoidal modulation with increased frequency and amplitude
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(1.5 * x) * np.cos(0.5 * x))
        
        # Enhanced fractal-like scaling with non-integer exponents and chaotic modulation
        fractal_term = np.sum(np.abs(x) ** (1.5 + 0.3 * np.sin(4.0 * x) + 0.1 * np.cos(2.0 * x)))
        
        # Improved multi-scale geometric interactions with exponential weighting
        geo_term = np.sum(np.exp(-0.05 * (x[:-1]**2 + x[1:]**2)) * (x[:-1] - x[1:])**2)
        
        # Enhanced chaotic saddle-point component with double exponential decay
        chaotic_term = np.sum(np.exp(-0.3 * (x - np.sin(x))**2) * np.exp(-0.2 * (x - np.cos(x))**2) * np.cos(3.0 * x))
        
        # Advanced cross-dimensional coupling with asymmetric and non-linear interaction
        cross_term = np.sum(np.sin(x[:-1]) * np.cos(x[1:]) + np.cos(x[:-1]) * np.sin(x[1:]) + 0.1 * x[:-1] * x[1:])
        
        # High-frequency oscillation with variable amplitude and phase modulation
        high_freq_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * (1.0 + 0.2 * np.sin(3.0 * x) * np.cos(2.0 * x)))
        
        # Additional chaotic component with nested trigonometric structure
        nested_term = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.exp(-0.1 * x**2))
        
        # Combined function with optimized weights for improved landscape complexity
        return 0.25 * poly_term + 0.2 * sin_term + 0.15 * fractal_term + 0.1 * geo_term + 0.1 * chaotic_term + 0.08 * cross_term + 0.07 * high_freq_term + 0.05 * nested_term