import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic sine-wave perturbations with varying frequencies and amplitudes
        f2 = 0.7 * np.sum(np.sin(25 * np.pi * x_normalized) ** 2)
        f3 = 0.4 * np.sum(np.sin(35 * np.pi * x_normalized) ** 2)
        
        # Enhanced fifth-order polynomial terms for increased complexity
        f4 = 0.15 * np.sum(x_normalized**5)
        f5 = 0.1 * np.sum(x_normalized**7)
        
        # Additional trigonometric term with chaotic phase and amplitude
        f6 = 0.25 * np.sum(np.cos(15 * np.pi * x_normalized) ** 2)
        
        # Complex cross-terms creating intricate interaction between dimensions
        f7 = 0.2 * np.sum(x_normalized[:-1] ** 4 * x_normalized[1:])
        f8 = 0.18 * np.sum(x_normalized[:-2] * x_normalized[1:-1] ** 3 * x_normalized[2:] ** 4)
        
        # Dynamic exponential conditioning factor with stronger scaling
        adaptive_scale = 1.0 + 0.5 * np.exp(0.1 * self.dim)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)