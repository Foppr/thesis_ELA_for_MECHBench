import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component for non-linearity and sensitivity
        logistic = np.sum(4 * x_norm * (1 - x_norm))
        
        # Radial basis function with multiple centers for multimodality
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbf = np.sum(np.exp(-5 * np.sum((x_norm[:, np.newaxis] - centers)**2, axis=0)))
        
        # Saddle-point structure with mixed quadratic and quartic terms
        saddle = np.sum(x_norm**2 * x_norm**4) - 0.5 * np.sum(x_norm**6)
        
        # Cross-terms creating complex interactions between dimensions
        cross_terms = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Add periodic modulation to increase complexity
        periodic = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Combine all components with adaptive weights
        result = logistic + 0.3 * rbf + 0.4 * saddle + 0.2 * cross_terms + 0.1 * periodic
        
        # Add small random noise for robustness
        result += 0.005 * np.random.random()
        
        return result