import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(5 * np.pi * x))
        
        # Polynomial chaos with high-degree terms and mixed nonlinearities
        poly_term = np.sum(0.3 * x**8 - 4 * x**6 + 7 * x**4 - 5 * x**2 + 2 * x)
        
        # Cross-dimensional cubic coupling with chaotic phase shifts
        coupling_term = np.sum((x[:-1] - x[1:])**3 * np.sin(7 * np.pi * x[:-1]) * np.cos(3 * np.pi * x[1:]))
        
        # Chaotic interaction terms with exponential decay and sinusoidal modulation
        chaotic_term = np.sum(np.exp(-0.5 * x**2) * np.sin(9 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Additional multimodal structure with Gaussian-like peaks and valleys
        gaussian_term = np.sum(np.exp(-0.1 * (x - 1)**2) + np.exp(-0.1 * (x + 1)**2) - 0.5 * np.exp(-0.1 * x**2))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.15 * sin_term + 0.1 * poly_term + 0.07 * coupling_term + 0.05 * chaotic_term + 0.03 * gaussian_term + 2.1