import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(10 * np.pi * x) * np.cos(7 * np.pi * x) * np.sin(5 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Polynomial chaos with mixed odd and even powers and nonlinear coupling
        poly_chaos = np.sum(0.3 * x**8 - 4 * x**6 + 7 * x**4 - 6 * x**2 + 2 * x * np.sin(x))
        
        # Cross-dimensional dependency with asymmetric scaling and nonlinear correlation
        cross_term = np.sum((x[:-1] ** 2.5) * np.sin(4 * np.pi * x[1:]) + (x[1:] ** 1.7) * np.cos(6 * np.pi * x[:-1]))
        
        # Non-smooth features with sharp transitions and plateau regions
        smooth_term = np.sum(np.abs(x) ** 1.3 + np.sin(2 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Asymmetric exponential decay with phase modulation
        asym_exp = np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Combine all terms with carefully tuned weights
        return 0.22 * chaotic_term + 0.15 * poly_chaos + 0.18 * cross_term + 0.25 * smooth_term + 0.12 * asym_exp + 2.1