import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with dynamic frequency modulation
        chaotic_wave = np.sum(np.sin(2 * np.pi * x * (1 + 0.5 * np.sin(0.3 * x))) * 
                             np.cos(3 * np.pi * x * (1 + 0.3 * np.cos(0.4 * x))))
        
        # Polynomial chaos with mixed monomials and nonlinear transformations
        poly_chaos = np.sum(0.5 * x**8 - 3.2 * x**6 + 5.8 * x**4 - 4.1 * x**2 + 0.9 * x)
        
        # Cross-dimensional interference with adaptive coupling strength
        interference = 0
        for i in range(self.dim - 1):
            coupling_strength = 0.5 + 0.5 * np.sin(0.5 * np.pi * x[i])
            interference += coupling_strength * (x[i] - x[i+1])**2 * np.sin(4 * np.pi * (x[i] + x[i+1]))
        
        # Multi-scale oscillation with varying amplitudes and phases
        multi_scale = np.sum(np.sin(6 * np.pi * x) * np.cos(8 * np.pi * x) * 
                           (1 + 0.2 * np.sin(2 * np.pi * x)) * 
                           (1 + 0.3 * np.cos(3 * np.pi * x)))
        
        # Adaptive noise-like component with dimension-dependent scaling
        adaptive_noise = np.sum(0.1 * x * np.sin(10 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Combine all components with optimized weights
        return 0.3 * chaotic_wave + 0.25 * poly_chaos + 0.2 * interference + 0.15 * multi_scale + 0.1 * adaptive_noise + 2.1