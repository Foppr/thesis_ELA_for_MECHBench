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
        f2 = 0.8 * np.sum(np.sin(25 * np.pi * x_normalized) ** 2)
        f3 = 0.6 * np.sum(np.sin(35 * np.pi * x_normalized) ** 2)
        
        # Higher-order polynomial terms with alternating signs for complexity
        f4 = 0.2 * np.sum(x_normalized**4)
        f5 = 0.15 * np.sum(x_normalized**6)
        
        # Complex cross-dimensional coupling with exponential interaction
        f6 = 0.25 * np.sum(np.exp(2 * np.abs(x_normalized[:-1])) * x_normalized[1:] ** 2)
        
        # Chaotic trigonometric cross-terms with phase shifts
        f7 = 0.2 * np.sum(np.sin(15 * np.pi * x_normalized[:-1]) * np.cos(10 * np.pi * x_normalized[1:]))
        
        # Dynamic conditioning factor that heavily penalizes higher dimensions
        adaptive_scale = 1.0 + 0.5 * np.exp(0.1 * self.dim)
        
        # Add a small noise term to increase robustness to local optima
        noise = 0.01 * np.sum(np.random.rand(self.dim) * x_normalized**2)
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7) + noise