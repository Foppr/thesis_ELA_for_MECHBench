import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(4 * np.pi * x))
        
        # Polynomial chaos expansion with mixed monomials and nonlinear interactions
        poly_term = np.sum(0.5 * x**8 - 3.2 * x**6 + 5.1 * x**4 - 4.3 * x**2 + 1.9 * x)
        
        # Cross-dimensional coupling with chaotic phase shifts and exponential decay
        coupling_term = np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(6 * np.pi * x[:-1]) * np.cos(4 * np.pi * x[1:]))
        
        # Multi-scale oscillatory patterns with varying amplitudes and frequencies
        oscillation_term = np.sum(np.sin(8 * np.pi * x) * np.cos(5 * np.pi * x) * np.sin(2 * np.pi * x))
        
        # Nonlinear correlation terms with polynomial weighting and chaotic modulation
        corr_term = np.sum((x**2 + 0.5 * x**3) * np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.3 * sin_term + 0.15 * poly_term + 0.25 * coupling_term + 0.1 * oscillation_term + 0.2 * corr_term + 2.1