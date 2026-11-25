import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with higher degree terms and increased coefficients
        poly_term = np.sum(1.5 * x**6 + 2.0 * x**5 - 1.2 * x**4 + 0.6 * x**3 - 0.2 * x**2 + 0.05 * x + 0.02)
        
        # Intensified sinusoidal modulation with higher frequencies and stronger amplitudes
        sin_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * np.sin(4.0 * x) * np.cos(3.0 * x) * np.sin(2.0 * x))
        
        # Augmented fractal-like scaling with additional logarithmic and power components
        fractal_term = np.sum(np.abs(x) ** (1.8 + 0.5 * np.sin(6.0 * x)) + 0.2 * np.log(1.0 + np.abs(x)) + 0.07 * x**2.8)
        
        # Strengthened multi-scale geometric interactions with exponential and trigonometric kernels
        geo_term = np.sum(np.exp(-0.4 * (x[:-1] - x[1:]) ** 2) * np.sin(3.0 * (x[:-1]**2 + x[1:]**2)))
        
        # Intensified chaotic saddle-point component with hyperbolic tangent and cubic scaling
        chaotic_term = np.sum(np.tanh(4.0 * x) * np.exp(-0.6 * x**3) * np.cos(5.0 * x))
        
        # Augmented cross-dimensional coupling with asymmetric, non-linear, and higher-order interactions
        cross_term = np.sum(x[:-1] * np.sin(3.0 * x[1:]) + x[1:] * np.cos(3.5 * x[:-1]) + 0.3 * x[:-1]**2 * x[1:] + 0.25 * x[:-1] * x[1:]**2)
        
        # Enhanced high-frequency oscillation with compound amplitude and phase modulation
        high_freq_term = np.sum(np.sin(9.0 * x) * np.cos(8.0 * x) * (1.0 + 0.4 * np.sin(5.0 * x)) * np.exp(-0.3 * x**2) * np.tanh(1.5 * x))
        
        # Additional cubic coupling terms to increase saddle-point density
        cubic_coupling = np.sum(0.15 * x[:-1]**3 * x[1:] + 0.12 * x[:-1] * x[1:]**3)
        
        # Combined function with new optimized weights for increased challenge
        return 0.35 * poly_term + 0.3 * sin_term + 0.25 * fractal_term + 0.15 * geo_term + 0.12 * chaotic_term + 0.1 * cross_term + 0.08 * high_freq_term + 0.05 * cubic_coupling