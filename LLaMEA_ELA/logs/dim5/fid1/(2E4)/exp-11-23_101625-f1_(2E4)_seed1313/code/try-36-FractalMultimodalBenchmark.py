import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Fractal-like multimodal components with self-similarity
        for i in range(self.dim):
            # Logarithmic scaling of frequencies
            freq = 2 ** (i % 4 + 1)
            # Multi-resolution interference patterns
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.log(1 + abs(x[i]))
            
        # Nested fractal valleys with varying depths
        for i in range(self.dim):
            # Create nested structures using polynomial transformations
            val = x[i]**2 + 0.1
            result += 0.4 * np.sin(10 * np.log(val)) * np.cos(5 * np.log(val))
            
        # Multi-scale ridge patterns with logarithmic spacing
        for i in range(self.dim):
            # Logarithmic scale ridge structure
            ridge_scale = 2 ** (i % 3 + 1)
            result += 0.25 * np.sin(ridge_scale * x[i]) * np.cos(ridge_scale * x[i] * 0.7) * np.exp(-0.1 * abs(x[i]))
            
        # Interference terms between dimensions with fractal coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal coupling strength based on dimension indices
                coupling = 0.15 * (i + j + 1) ** -0.8
                # Logarithmic interference pattern
                result += coupling * np.sin(2**i * x[i]) * np.cos(2**j * x[j]) * np.log(1 + abs(x[i] - x[j]))
                
        # Asymmetric fractal valleys with irregular depth
        for i in range(self.dim):
            # Irregular valley structure using asymmetric polynomial
            asym_valley = (x[i]**3 + 0.5 * x[i]**2) * np.exp(-0.2 * abs(x[i]))
            result += 0.3 * asym_valley
            
        # High-frequency fractal oscillations with diminishing amplitude
        for i in range(self.dim):
            # Fractal frequency progression
            freq = 10 * (i + 1)
            result += 0.1 * np.sin(freq * x[i]) * np.exp(-0.05 * freq)
            
        return result