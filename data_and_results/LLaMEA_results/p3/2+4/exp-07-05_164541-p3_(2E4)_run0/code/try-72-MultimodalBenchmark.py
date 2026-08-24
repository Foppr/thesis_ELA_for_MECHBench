import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) + 
                          np.sin(4 * np.pi * x) * np.cos(5 * np.pi * x) + 
                          np.sin(6 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Polynomial chaos expansion with mixed monomials and nonlinear interactions
        poly_term = np.sum(0.5 * x**8 - 3.2 * x**6 + 5.8 * x**4 - 4.1 * x**2 + 1.9 * x)
        
        # Cross-dimensional interaction with chaotic phase shifts and nonlinear coupling
        coupling_term = np.sum((x[:-1] * x[1:] + np.sin(2 * np.pi * x[:-1]) * np.cos(2 * np.pi * x[1:]))**2)
        
        # Multi-scale chaotic oscillations with varying decay rates and amplitude modulation
        chaos_term = np.sum(np.exp(-0.1 * x**2) * np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x) * np.sin(6 * np.pi * x))
        
        # Additional high-frequency noise-like components for increased complexity
        noise_term = np.sum(np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) + 
                            np.sin(9 * np.pi * x) * np.cos(11 * np.pi * x))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.25 * sin_term + 0.15 * poly_term + 0.12 * coupling_term + 0.18 * chaos_term + 0.08 * noise_term + 2.1