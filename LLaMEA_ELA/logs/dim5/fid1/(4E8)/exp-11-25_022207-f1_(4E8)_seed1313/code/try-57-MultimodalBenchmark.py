import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure using sine-cosine combinations
        fractal_term = np.sum(np.sin(2**np.arange(1, self.dim + 1) * x_norm) * 
                             np.cos(3**np.arange(1, self.dim + 1) * x_norm))
        
        # Dynamic gradient field with position-dependent frequency modulation
        grad_field = np.sum((x_norm**2 + 0.1) * np.sin(10 * x_norm * (1 + 0.2 * np.cos(x_norm))))
        
        # Hybrid oscillatory-polynomial interactions with variable coupling strength
        hybrid_term = np.sum(np.sin(x_norm**3) * np.cos(2 * x_norm**2) * 
                            (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Nested optima structure using recursive polynomial transformations
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (x_norm[i]**6 - 2 * x_norm[i]**4 + x_norm[i]**2) * \
                          np.exp(-0.1 * (x_norm[i] - 1)**2)
        
        # Cross-dimensional coupling with fractal scaling
        cross_coupling = 0.2 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                    np.sin(5 * np.pi * x_norm[:-1]))
        
        # Add noise for robustness and complexity
        noise = 0.02 * np.random.randn()
        
        return fractal_term + grad_field + hybrid_term + nested_term + cross_coupling + noise