import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed global minimum with chaotic offset
        self.global_min = np.array([(-1)**i * 2.5 + 0.5 * np.sin(i * np.pi / 4) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive quadratic term with chaotic scaling
        f1 = np.sum((x - self.global_min)**2 * (1 + 0.2 * np.sin(2 * x)))
        
        # Chaotic sine-cosine coupling with dynamic frequency
        f2 = np.sum(np.sin(3.0 * x + np.cos(2.0 * x)) * np.cos(2.0 * x + np.sin(3.0 * x)))
        
        # Higher-order polynomial with cross-terms and chaotic coefficients
        f3 = np.sum(x**6 - 20 * x**4 + 150 * x**2 - 500)
        
        # Logarithmic barrier with exponential scaling
        f4 = np.sum(np.log(1 + 0.1 * np.abs(x)) * np.exp(0.2 * np.abs(x)))
        
        # Nested chaotic trigonometric interactions
        f5 = np.sum(np.sin(np.cos(np.sin(x))) + np.cos(np.sin(np.cos(x))))
        
        # Adaptive coupling with chaotic phase shifts
        f6 = np.sum(np.sin(x * np.cos(x) + np.sin(x)) * np.cos(x * np.sin(x) + np.cos(x)))
        
        # Combine all components with optimized weights and chaotic scaling
        return 0.2 * f1 + 0.2 * f2 + 0.15 * f3 + 0.2 * f4 + 0.15 * f5 + 0.1 * f6