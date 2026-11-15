import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with mixed degrees for varied curvature
        poly_term = np.sum(x_scaled**6 + 0.5 * x_scaled**4 + 0.1 * x_scaled**2)
        
        # Trigonometric components creating oscillatory behavior
        trig_term = np.sum(np.cos(5 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Radial basis function component for multi-modal structure
        rbf = 0
        for i in range(1, 6):
            center = np.random.uniform(-1, 1, self.dim)
            rbf += np.exp(-10 * np.sum((x_scaled - center)**2))
        
        # Cross-term interaction to induce non-separability
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combine all components with different weights
        return 0.3 * poly_term + 1.2 * trig_term + 0.8 * rbf + 0.2 * cross_term