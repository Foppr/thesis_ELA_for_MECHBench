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
        
        # Add fractal-like periodic components with increasing frequency
        for i in range(1, min(6, self.dim + 1)):
            freq = 2**i
            term = np.sin(freq * np.pi * x) * np.cos(freq * np.pi * x)
            result += 0.1 * np.sum(term**2)
        
        # Recursive fractal structure using a modified Barnsley-like construction
        fractal_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create nested structure with scaling factor
            scale = 0.5
            for depth in range(1, 5):
                # Apply transformation that creates self-similarity
                xi = scale * (xi - 0.5) + 0.5
                # Add penalty at each level
                fractal_penalty += np.sin(10 * xi) * np.exp(-depth / 3.0)
        
        # Add chaotic component using sine-Gordon-like terms
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-i / self.dim)
        
        # Add multiple nested minima with exponentially decaying depths
        nested_penalty = 0.0
        for k in range(1, 8):
            # Create k-th level minima
            level_scale = 1.0 / (2**k)
            loc = np.full(self.dim, level_scale)
            # Random perturbation to create complex structure
            for i in range(self.dim):
                loc[i] = level_scale * np.sin(k * i * np.pi / self.dim)
            distance = np.sum((x - loc)**2)
            nested_penalty += np.exp(-distance / (2.0 * (k**2)))
        
        result += fractal_penalty + chaotic_term + 0.5 * nested_penalty
        
        return result