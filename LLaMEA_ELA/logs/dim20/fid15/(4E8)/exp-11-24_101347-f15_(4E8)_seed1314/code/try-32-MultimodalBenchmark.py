import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with sinusoidal modulation
        chaotic_grad = np.sum(np.sin(x * np.pi) * np.cos(2.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Polynomial modulation with mixed exponents
        poly_mod = np.sum((x**4 + 0.5 * x**3 - 0.3 * x**2 + 0.1 * x) / (1.0 + np.abs(x)))
        
        # Exponentially decaying harmonic terms
        exp_harmonic = np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Saddle-point inducing cross-dimensional interaction
        saddle_term = np.prod(np.tanh(x)) * np.sum(x**2)
        
        # Add a global minimum at origin with perturbation
        return chaotic_grad + poly_mod + exp_harmonic + saddle_term + 0.01 * np.sum(x**8)