import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like sine waves with varying frequencies and amplitudes
        freqs = np.logspace(0, 2, self.dim)
        f2 = np.sum(np.sin(freqs * x_norm * np.sin(freqs * x_norm)) ** 2)
        
        # Dynamic phase shifts that depend on dimension index
        phases = np.linspace(0, np.pi, self.dim)
        f3 = np.sum(np.cos(x_norm * np.cos(phases * x_norm)) ** 3)
        
        # Adaptive polynomial interactions with dimension-dependent exponents
        exponents = np.arange(3, 3 + self.dim)
        f4 = np.sum((x_norm ** exponents) * np.exp(-x_norm**2))
        
        # Cross-dimensional coupling with exponential decay and sinusoidal modulation
        f5 = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * np.sin(x_norm[:-1] * x_norm[1:]))
        
        # Asymmetric chaotic interference with varying coupling strengths
        coupling_strengths = np.linspace(0.5, 2.0, self.dim - 1)
        f6 = np.sum(coupling_strengths * np.sin(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Higher-order polynomial with non-uniform coefficients
        f7 = np.sum(0.5 * x_norm**4 + 0.3 * x_norm**6 + 0.1 * x_norm**8)
        
        # Final term: multi-scale chaotic modulation with varying amplitude
        f8 = np.sum(np.sin(10 * np.pi * x_norm * np.cos(5 * np.pi * x_norm)) ** 4)
        
        return 0.5 * f1 + 0.8 * f2 + 0.6 * f3 + 0.4 * f4 + 0.3 * f5 + 0.7 * f6 + 0.2 * f7 + 0.9 * f8