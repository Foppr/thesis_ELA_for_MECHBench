import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Enhanced quadratic basin with varying coefficients
        quadratic_sum = np.sum((x_normalized**2) * (1 + 0.5 * np.sin(2 * np.pi * x_normalized)))
        
        # Multiple interacting sinusoidal components with different frequencies
        sinusoidal_sum = np.sum(np.sin(10 * np.pi * x_normalized) + 
                               0.5 * np.sin(20 * np.pi * x_normalized) + 
                               0.3 * np.sin(30 * np.pi * x_normalized))
        
        # Complex penalty terms with cross-terms
        penalty = 0.2 * np.sum(x_normalized**6) + \
                 0.1 * np.sum((x_normalized[:-1] - x_normalized[1:])**2)
        
        # Add a global minimum attraction term at the origin
        attraction = 0.5 * np.exp(-np.sum(x_normalized**2) / 2)
        
        # Combine all components to create a highly challenging multimodal function
        return quadratic_sum + sinusoidal_sum + penalty - attraction