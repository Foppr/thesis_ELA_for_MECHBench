import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like chaotic components with self-similarity
        term1 = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic barrier regions
        term2 = 0.5 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(5 * x))
        
        # Multi-scale harmonic modulations
        term3 = 0.3 * np.sum(np.sin(2 * x) * np.cos(3 * x) * np.sin(7 * x))
        
        # Self-similar fractal structure using recursive-like terms
        term4 = 0.2 * np.sum(np.sin(10 * np.sin(5 * x)) * np.cos(10 * np.cos(3 * x)))
        
        # Non-smooth irregularities
        term5 = 0.1 * np.sum(np.abs(x - np.round(x / 0.5)) ** 1.5)
        
        # Interaction terms with fractal-like scaling
        interaction = 0.05 * np.sum(np.sin(15 * (x[:-1] - x[1:])) * np.cos(10 * (x[:-1] + x[1:])))
        
        # Adaptive exponential decay with fractal scaling
        barrier = 0.4 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(25 * x) * np.cos(12 * x))
        
        result = term1 + term2 + term3 + term4 + term5 + interaction + barrier
        
        # Add small perturbation to increase difficulty
        result += 0.001 * np.random.random()
        
        return result