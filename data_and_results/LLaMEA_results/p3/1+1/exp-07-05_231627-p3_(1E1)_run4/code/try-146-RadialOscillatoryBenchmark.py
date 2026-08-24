import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for consistent scaling
        x_norm = x / 5.0
        
        # Radial component with exponential decay and polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1 + 0.5 * r**4)
        
        # Multi-frequency trigonometric oscillation in radial direction
        oscillation = np.sum(np.sin(10 * r) * np.cos(15 * r) * np.sin(20 * r))
        
        # Angular component with multiple peaks and valleys
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1:], x_norm[0])
            angular = np.sum(np.sin(8 * angles) * np.cos(12 * angles) * np.exp(-0.5 * r**2))
        
        # Cross-dimensional interaction with Gaussian-like correlations
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(5 * (x_norm[i] + x_norm[j]))
        
        # Polynomial ridge structure with varying curvature
        ridge = np.sum((x_norm**3 - 3 * x_norm)**2)
        
        # Add a global sinusoidal modulation
        modulation = np.sin(0.5 * np.sum(x_norm))
        
        # Combine all components with adaptive weights
        result = 0.4 * radial + 0.3 * oscillation + 0.15 * angular + 0.1 * interaction + 0.05 * ridge + 0.05 * modulation
        
        # Add small random noise for robustness
        noise = 0.001 * np.random.random()
        
        return result + noise