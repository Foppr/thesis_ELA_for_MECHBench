import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Time-varying global minimum with chaotic perturbation
        self.global_min = np.array([2.5 * np.sin(i * 0.7) + 0.5 * np.cos(i * 0.3) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial coupling with adaptive weights
        f1 = np.sum((x - self.global_min)**4 + 0.5 * (x - self.global_min)**3)
        
        # Trigonometric interference with dynamic phase modulation
        f2 = np.sum(np.sin(2.0 * x + np.cos(0.5 * x)) * np.cos(1.5 * x + np.sin(0.3 * x)))
        
        # Logarithmic barrier terms with exponential scaling
        f3 = np.sum(np.log(1 + 0.1 * np.abs(x)) * np.exp(0.2 * x**2))
        
        # Adaptive chaotic component with nested sinusoids
        f4 = np.sum(np.sin(np.pi * x * np.cos(x)) + np.cos(np.pi * x * np.sin(x)))
        
        # Cross-dimensional coupling with exponential interaction
        f5 = np.sum(np.exp(np.abs(x) * np.sin(x)) - 1)
        
        # Dynamic scaling with time-varying coefficients
        scale = 1.0 + 0.2 * np.sin(np.sum(x) * 0.1)
        
        # Combine all components with varying weights
        return scale * (0.2 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.2 * f5)