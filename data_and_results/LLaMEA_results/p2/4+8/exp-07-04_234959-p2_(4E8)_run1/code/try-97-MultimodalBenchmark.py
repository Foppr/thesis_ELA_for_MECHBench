import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Time-varying global minimum with chaotic perturbations
        np.random.seed(42)
        self.global_min = np.random.uniform(-2.5, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial interaction terms with adaptive weights
        f1 = np.sum((x - self.global_min)**4 + 0.5 * (x - self.global_min)**3)
        
        # Trigonometric interference with dynamic frequency modulation
        f2 = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic barrier terms with exponential scaling
        f3 = np.sum(np.log(1 + np.abs(x)) * np.exp(-0.5 * x**2))
        
        # Coupled sinusoidal components with chaotic phase shifts
        f4 = np.sum(np.sin(x + np.sin(2 * x)) * np.cos(x + np.cos(2 * x)))
        
        # Adaptive noise component with dynamic amplitude
        noise = np.random.normal(0, 0.1, self.dim)
        f5 = np.sum((x - self.global_min + noise)**2 * np.sin(x))
        
        # Cross-dimensional coupling with exponential decay
        f6 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Combine all components with chaotic scaling factors
        weights = [0.15 + 0.05 * np.sin(i) for i in range(6)]
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5 + weights[5] * f6