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
        
        # Trigonometric interference with dynamic frequency modulation
        f2 = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic barrier terms with exponential scaling
        f3 = np.sum(np.log(1 + np.abs(x)) * np.exp(-0.2 * x**2))
        
        # Cross-dimensional coupling with chaotic phase shifts
        f4 = np.sum(np.sin(x * np.pi / 4 + np.sin(x * 0.5)) * np.cos(x * np.pi / 3 + np.cos(x * 0.3)))
        
        # Adaptive noise component with time-varying amplitude
        noise = np.random.normal(0, 0.1 * (1 + np.sin(np.sum(x) * 0.1)))
        
        # Combine all components with dynamic scaling
        return 0.25 * f1 + 0.30 * f2 + 0.20 * f3 + 0.25 * f4 + noise