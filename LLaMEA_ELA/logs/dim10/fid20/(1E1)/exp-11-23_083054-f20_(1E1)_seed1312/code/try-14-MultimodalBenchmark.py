import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(np.sin(6 * np.pi * x_norm) ** 2 + 0.8 * np.sin(12 * np.pi * x_norm) ** 2)
        
        # Additional high-frequency sinusoidal term to increase complexity
        f3 = np.sum(np.sin(20 * np.pi * x_norm) ** 2 + 0.5 * np.sin(24 * np.pi * x_norm) ** 2)
        
        # Polynomial interaction terms with modified exponents and weights
        f4 = np.sum(2.0 * x_norm**4 + 0.5 * x_norm**6 + 0.1 * x_norm**8)
        
        # Product term with modified scaling to create more intricate landscape
        f5 = np.prod(0.9 * np.cos(0.5 * np.pi * x_norm) ** 2 + 0.1 * np.sin(1.0 * np.pi * x_norm) ** 2)
        
        # Chaotic component using logistic map for added nonlinearity
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            if i > 0:
                chaotic += (r * x_norm[i-1] * (1 - x_norm[i-1])) - (r * x_norm[i] * (1 - x_norm[i]))
        
        # Combine all terms with carefully tuned weights
        return 0.7 * f1 + 0.2 * f2 + 0.05 * f3 + 0.02 * f4 - 0.05 * f5 + 0.01 * chaotic