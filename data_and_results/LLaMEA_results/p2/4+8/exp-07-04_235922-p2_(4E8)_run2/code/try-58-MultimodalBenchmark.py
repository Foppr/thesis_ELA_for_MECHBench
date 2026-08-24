import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar components
        term1 = np.sum(np.abs(x) ** 1.7)
        term2 = 0.5 * np.sum(np.sin(10 * np.log(np.abs(x) + 1e-8)) * np.cos(5 * np.log(np.abs(x) + 1e-8)))
        
        # Trigonometric chaos with varying frequencies
        term3 = 0.3 * np.sum(np.sin(2 * x) * np.cos(3 * x) * np.sin(5 * x))
        term4 = 0.2 * np.sum(np.cos(4 * x) * np.sin(7 * x) * np.cos(9 * x))
        
        # Adaptive gradient modulation based on local curvature
        grad_mod = np.zeros_like(x)
        for i in range(len(x)):
            if i > 0:
                grad_mod[i] += 0.1 * (x[i] - x[i-1]) ** 2
            if i < len(x) - 1:
                grad_mod[i] += 0.1 * (x[i+1] - x[i]) ** 2
        term5 = np.sum(grad_mod)
        
        # Multi-scale geometric interference
        interference = 0.4 * np.sum(np.sin(x) * np.cos(x**0.5) * np.sin(x**0.3))
        interference += 0.3 * np.sum(np.cos(x) * np.sin(x**0.7) * np.cos(x**0.2))
        
        # Asymmetric exponential barriers
        barrier = 0.6 * np.sum(np.exp(-0.5 * (x - np.mean(x))**2) * np.sin(10 * x) * np.cos(3 * x))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + term5 + interference + barrier
        
        # Add small perturbation to increase complexity
        result += 0.001 * np.random.random()
        
        return result