import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal oscillations with exponential growth and cross-dimensional interaction
        f2 = np.sum(np.sin(20.0 * np.exp(0.8 * np.abs(x)) * x) * np.cos(0.5 * np.sum(x, axis=0, keepdims=True)))
        
        # Polynomial corruption with varying degrees and asymmetric distortion
        f3 = 0.02 * np.sum((x**7 + 0.7 * x**6 + 0.4 * x**5 + 0.2 * x**4) * (1 + 0.1 * np.sin(x)))
        
        # Add saddle point structure with stronger interaction and directional bias
        f4 = 0.2 * np.sum(np.cos(4.0 * x) * np.sin(0.8 * x) * np.exp(-0.15 * np.abs(x)) * (1 + 0.05 * np.cos(x)))
        
        # Introduce additional chaotic component with asymmetric exponential and logarithmic terms
        f5 = 0.07 * np.sum(np.sin(np.exp(1.2 * x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.tanh(x))
        
        # Cross-dimensional interaction term to increase complexity
        f6 = 0.1 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6