import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term
        polynomial = 0.1 * np.sum(x**4) + 0.05 * np.sum(x**2)
        
        # Trigonometric oscillations with varying frequencies and phases
        trigonometric = 0.0
        for i in range(self.dim):
            trigonometric += np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            trigonometric += 0.5 * np.cos(4 * x[i]) * np.sin(5 * x[(i + 2) % self.dim])
            trigonometric += 0.3 * np.sin(6 * x[i]) * np.cos(7 * x[(i + 3) % self.dim])
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf += np.exp(-0.5 * ((x[i] - center) / 1.5)**2)
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            cross_interaction += np.exp(-0.1 * (x[i] - x[(i + 1) % self.dim])**2)
            cross_interaction += 0.2 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 2) % self.dim])
        
        # High-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(50 * x[i]) * np.cos(40 * x[(i + 1) % self.dim])
        
        # Combine all components with different weights
        return 0.7 * polynomial + 1.3 * trigonometric + 0.8 * rbf + 1.1 * cross_interaction + 0.5 * noise