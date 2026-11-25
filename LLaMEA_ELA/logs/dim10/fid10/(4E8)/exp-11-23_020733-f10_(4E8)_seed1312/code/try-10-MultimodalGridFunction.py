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
        
        # Calculate distance to nearest grid point in each dimension using a modified metric
        distances = []
        for i in range(self.dim):
            dist = np.abs(x[i] - grid_points[np.argmin(np.abs(x[i] - grid_points))])
            # Apply a nonlinear transformation to increase complexity
            distances.append(dist ** 1.5)
        
        # Base function with grid minima using sum of transformed distances
        base_value = np.sum(np.array(distances))
        
        # Add multiple sinusoidal oscillation terms with different frequencies and amplitudes
        oscillation = (
            0.8 * np.sin(0.3 * np.sum(x)) + 
            0.5 * np.cos(0.7 * np.sum(x**2)) +
            0.3 * np.sin(0.9 * np.sum(x**3)) +
            0.2 * np.cos(0.4 * np.sum(np.abs(x)))
        )
        
        # Add a radial component to increase complexity near the global minima
        radial_term = 0.1 * np.exp(-0.1 * np.sum((x - grid_points[np.argmin(np.abs(x - grid_points))])**2))
        
        # Add noise term for additional complexity
        noise = 0.05 * np.random.random()
        
        return base_value + oscillation + radial_term + noise