import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractal-like recursive component with self-similarity
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            if i < self.dim:
                fractal += np.sum(np.sin(2**i * x[:-i]) * np.cos(2**(i+1) * x[i:]))
        
        # Trigonometric chaos with varying frequencies
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(10 * x[i] + np.sin(5 * x[i])) * np.cos(7 * x[i] + np.cos(3 * x[i]))
        
        # Adaptive penalty landscape based on dimensionality
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i] ** 4) * np.sin(1 / (x[i]**2 + 0.01)) * np.exp(-0.1 * np.abs(x[i]))
        
        # Nested multimodal structure with varying scales
        nested = 0.0
        for i in range(self.dim):
            nested += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Interaction terms with varying strength
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**2 * np.sin(10 * (x[i] + x[i+1]))
        
        # Combine all components
        result += 0.3 * fractal + 0.2 * chaos + 0.1 * penalty + 0.15 * nested + 0.05 * interaction
        
        # Add small random noise for additional challenge
        result += 0.001 * np.random.random()
        
        return result