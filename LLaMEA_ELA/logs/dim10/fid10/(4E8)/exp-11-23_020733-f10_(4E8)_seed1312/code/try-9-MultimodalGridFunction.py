import numpy as np

class MultimodalGridFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, self.bounds.lb, self.bounds.ub)
        
        # Grid of global minima at regular intervals
        grid_points = np.arange(-4.0, 5.0, 2.0)
        if len(grid_points) < 2:
            grid_points = np.array([-4.0, 0.0, 4.0])
        
        # Calculate distance to nearest grid point in each dimension
        distances = []
        for i in range(self.dim):
            dist = np.abs(x[i] - grid_points[np.argmin(np.abs(x[i] - grid_points))])
            distances.append(dist)
        
        # Base function with grid minima
        base_value = np.sum(np.array(distances) ** 2)
        
        # Add sinusoidal oscillation to create complex landscape
        oscillation = 0.5 * np.sin(0.5 * np.sum(x)) + 0.3 * np.cos(0.3 * np.sum(x**2))
        
        # Add chaotic logistic map term for additional complexity
        logistic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(min(self.dim, 5)):  # Limit to first 5 dimensions for chaos
            logistic_term += np.sin(r * x[i] * (1 - x[i]))
        
        # Add noise term for additional complexity
        noise = 0.1 * np.random.random()
        
        return base_value + oscillation + logistic_term + noise