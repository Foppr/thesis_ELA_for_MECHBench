import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at the center
        self.global_min = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum((x - self.global_min)**2)
        
        # Fractal-like structure using recursive trigonometric terms
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Nested trigonometric functions creating fractal behavior
            term = np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.25 * np.sin(4 * xi)
            f2 += term**2
        
        # Multi-scale sinusoidal interference
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f3 += np.sin(10 * xi) * np.cos(5 * xi) * np.sin(2 * xi)
        
        # Adaptive noise component with varying intensity
        noise = np.random.normal(0, 0.1, self.dim)
        f4 = np.sum((x + noise)**4)
        
        # Exponential barrier terms
        f5 = np.sum(np.exp(0.5 * np.abs(x)) * np.sin(x)**2)
        
        # Coupled polynomial interactions
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += (x[i] * x[j])**2 * np.sin(x[i] + x[j])
        
        # Combine all components with dynamic weights
        return 0.2 * f1 + 0.3 * f2 + 0.15 * f3 + 0.15 * f4 + 0.1 * f5 + 0.1 * f6