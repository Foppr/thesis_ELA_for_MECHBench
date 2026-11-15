import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using sine and cosine with varying frequencies
        chaotic = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm) * np.sin(7 * x_norm))
        
        # Asymmetric valley term to create non-symmetric landscape
        valley = np.sum((x_norm - 0.3) ** 4 + (x_norm + 0.5) ** 2)
        
        # Saddle point structure with mixed quadratic and hyperbolic terms
        saddle = np.sum(x_norm ** 2 * np.tanh(x_norm))
        
        # Dynamic conditioning: weights change based on dimension
        weights = np.array([np.exp(-i / self.dim) for i in range(self.dim)])
        conditioning = np.sum(weights * x_norm ** 2)
        
        # Interaction term between dimensions with chaotic coupling
        interaction = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Combine all components with varying importance
        result = 0.2 * chaotic + 0.3 * valley + 0.2 * saddle + 0.2 * conditioning + 0.1 * interaction
        
        # Add small random noise to increase robustness testing
        noise = 0.01 * np.random.rand()
        
        return result + noise