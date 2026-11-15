import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with slight noise
        f = np.sum(x**2) * (1 + 0.1 * np.random.random())
        
        # Add chaotic sinusoidal grid pattern with multiple global minima
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i]**2)
            
        # Add nested interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.1 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(5 * x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add fractal-like self-similar structure
        for i in range(self.dim):
            f += 0.05 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i]) * np.cos(4 * x[i])
            
        # Add multiple local minima with varying depths
        for i in range(self.dim):
            f += 0.15 * np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(9 * x[i]) * np.cos(6 * x[i])
            
        # Add global minimum at origin with complex noise
        f += 0.02 * np.sum(np.sin(x)**3) + 0.01 * np.sum(np.cos(x)**4)
        
        # Add a small random perturbation to make it non-deterministic
        f += 0.005 * np.random.random()
        
        return f