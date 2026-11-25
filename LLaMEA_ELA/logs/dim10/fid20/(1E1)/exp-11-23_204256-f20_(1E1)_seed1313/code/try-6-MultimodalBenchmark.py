import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Add exponentially scaled sinusoidal perturbations to create multiple local minima
        f2 = 0.3 * np.sum(np.exp(3 * np.abs(x_normalized)) * np.sin(5 * np.pi * x_normalized) ** 2)
        
        # Add a global scaling factor to control the function landscape
        f3 = 0.05 * np.sum(x_normalized**4)
        
        # Add higher-order nonlinear terms for increased complexity
        f4 = 0.1 * np.sum(np.cos(4 * np.pi * x_normalized) ** 3)
        
        # Add cross-terms to increase interaction between dimensions
        f5 = 0.08 * np.sum((x_normalized[:-1] + x_normalized[1:]) ** 2)
        
        # Introduce chaotic behavior through a logistic map-like component
        f6 = 0.03 * np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(10 * np.pi * x_normalized))
        
        return f1 + f2 + f3 + f4 + f5 + f6