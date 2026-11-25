import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base = 0.1 * np.sum(x**2)
        
        # Fractal-like self-similar structure using recursive sine-cosine patterns
        fractal = 0
        for i in range(self.dim):
            # Multi-scale oscillations with decreasing amplitude
            scale = 1.0
            for k in range(1, 6):  # 5 levels of recursion
                fractal += scale * np.sin(k * np.pi * x[i]) * np.cos(k * np.pi * x[i])
                scale *= 0.5
        
        # Logarithmic barrier terms to create non-smooth regions
        barrier = 0
        for i in range(self.dim):
            if np.abs(x[i]) < 0.1:
                barrier += 100 * (1 / (np.abs(x[i]) + 1e-8) - 1)
            else:
                barrier += np.log(1 + np.abs(x[i]))
        
        # Multi-scale periodic components with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(10 * x[i]) * np.cos(5 * x[i])
            periodic += 0.3 * np.sin(20 * x[i]) * np.cos(10 * x[i])
        
        # Interaction terms between dimensions with varying strength
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all components
        return base + fractal + barrier + periodic + interaction + 0.001 * np.sum(np.abs(x)**3)