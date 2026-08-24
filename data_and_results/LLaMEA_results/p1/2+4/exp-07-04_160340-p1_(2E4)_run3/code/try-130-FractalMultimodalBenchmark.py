import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add fractal-like periodic components with increasing frequency and amplitude
        for i in range(1, min(8, self.dim + 1)):
            freq = 3**i
            amplitude = 0.15 / (i**1.5)
            term = amplitude * np.sin(freq * np.pi * x) * np.cos(freq * np.pi * x)
            result += np.sum(term**2)
        
        # Enhanced recursive fractal structure using a modified logistic map
        fractal_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            scale = 0.4
            for depth in range(1, 7):
                # Apply logistic-like transformation that creates high sensitivity
                xi = scale * xi * (1 - xi)
                # Add penalty at each level with varying weights
                fractal_penalty += np.sin(15 * xi) * np.cos(12 * xi) * np.exp(-depth / 4.0)
        
        # Add hyper-chaotic component using coupled sine-Gordon-like terms
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+3)):
                chaotic_term += np.sin(25 * x[i]) * np.cos(20 * x[j]) * np.exp(-(i+j) / (self.dim * 2.0))
        
        # Add multiple nested minima with varying scales and correlation structures
        nested_penalty = 0.0
        for k in range(1, 10):
            # Create k-th level minima with correlated positions
            level_scale = 1.0 / (3**k)
            loc = np.full(self.dim, level_scale)
            for i in range(self.dim):
                # Correlated perturbation pattern
                loc[i] = level_scale * np.sin(k * i * np.pi / self.dim) * np.cos(k * i * np.pi / (self.dim * 2))
            # Distance with custom metric
            distance = np.sum(((x - loc) / (1 + 0.1 * k))**2)
            nested_penalty += np.exp(-distance / (2.0 * (k**1.8)))
        
        # Add a global scaling factor to increase function complexity
        result += 0.8 * fractal_penalty + 0.6 * chaotic_term + 0.7 * nested_penalty
        
        return result