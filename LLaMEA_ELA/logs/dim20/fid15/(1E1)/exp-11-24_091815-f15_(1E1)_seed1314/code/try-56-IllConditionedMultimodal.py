import numpy as np

class IllConditionedMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with mixed degrees to induce multimodality
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric component with varying frequencies and phase shifts
        trig_term = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Exponential interaction term to create conditioning difficulties
        exp_term = np.exp(-np.sum(x_norm**2) / (2 * 0.5**2)) * np.sum(np.exp(x_norm**2))
        
        # Cross-dimensional interaction with a conditioning matrix
        conditioning_matrix = np.eye(self.dim) + 0.1 * np.ones((self.dim, self.dim))
        cross_term = np.dot(x_norm.T, np.dot(conditioning_matrix, x_norm))
        
        # Add a global minimum at the origin with additional penalty
        global_min = -np.exp(-np.sum(x_norm**2) / (2 * 0.1**2))
        
        return poly_term + trig_term + exp_term + cross_term + global_min