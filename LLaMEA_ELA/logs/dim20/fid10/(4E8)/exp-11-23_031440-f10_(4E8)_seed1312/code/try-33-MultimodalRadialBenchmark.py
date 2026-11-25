import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Compute radial distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        
        # Create multiple nested basins with varying depths
        basin_depths = np.array([0.1, 0.3, 0.6, 1.0])
        basin_radii = np.array([0.2, 0.4, 0.6, 0.8])
        
        # Calculate basin contribution for each basin
        basin_contributions = np.zeros_like(basin_radii)
        for i, (depth, radius) in enumerate(zip(basin_depths, basin_radii)):
            # Gaussian-like contribution centered at radius
            basin_contributions[i] = depth * np.exp(-0.5 * ((r - radius) / 0.1)**2)
        
        # Sum all basin contributions
        basin_term = np.sum(basin_contributions)
        
        # Add sinusoidal perturbations with varying frequencies and amplitudes
        sine_term = 0.5 * np.sum(np.sin(10 * np.pi * r) * np.sin(20 * np.pi * r) + 
                                0.3 * np.sin(5 * np.pi * r)**2)
        
        # Add conditioning term that increases with distance from origin
        conditioning_term = 0.2 * r**2
        
        # Add interaction between dimensions to increase complexity
        interaction_term = 0.1 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Combine all terms
        result = basin_term + sine_term + conditioning_term + interaction_term
        
        return result