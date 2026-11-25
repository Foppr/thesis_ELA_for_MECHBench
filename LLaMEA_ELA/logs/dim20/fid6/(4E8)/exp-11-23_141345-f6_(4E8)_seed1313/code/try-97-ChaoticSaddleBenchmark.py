import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees for each dimension
        poly_term = np.sum((x**3 + 0.6 * x**2 - 0.4 * x + 0.15) ** 2)
        
        # Sinusoidal modulation with multi-scale frequencies
        sin_term = np.sum(np.sin(2.7 * x) * np.cos(1.9 * x) * np.sin(0.9 * x))
        
        # Fractal-like scaling with recursive structure (enhanced)
        fractal_term = np.sum(np.abs(x) ** (1.4 + 0.3 * np.sin(3.2 * x)))
        
        # Multi-scale geometric interactions
        geo_term = np.sum((x[:-1] ** 2 + x[1:] ** 2) * np.exp(-0.12 * (x[:-1] - x[1:]) ** 2))
        
        # Chaotic saddle-point component with exponential decay
        chaotic_term = np.sum(np.exp(-0.6 * (x - np.sin(x))**2) * np.cos(2.2 * x))
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_term = np.sum(x[:-1] * np.sin(x[1:]) + x[1:] * np.cos(x[:-1]))
        
        # High-frequency oscillation with amplitude modulation
        high_freq_term = np.sum(np.sin(5.2 * x) * np.cos(4.2 * x) * (1.0 + 0.12 * np.sin(2.1 * x)))
        
        # Combined function with carefully balanced weights
        return 0.35 * poly_term + 0.18 * sin_term + 0.18 * fractal_term + 0.12 * geo_term + 0.09 * chaotic_term + 0.07 * cross_term + 0.06 * high_freq_term