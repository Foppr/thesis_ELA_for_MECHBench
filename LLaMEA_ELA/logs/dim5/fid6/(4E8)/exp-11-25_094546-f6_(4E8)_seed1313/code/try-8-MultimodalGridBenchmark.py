import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already scaled
        x = np.clip(x, -5.0, 5.0)
        
        # Create a grid of global minima at positions with small perturbations
        # Each dimension has minima at positions: -4, -2, 0, 2, 4
        grid_positions = np.array([-4, -2, 0, 2, 4])
        
        # Calculate distance to nearest grid point for each dimension
        distances = np.abs(x[:, None] - grid_positions[None, :])
        min_distances = np.min(distances, axis=1)
        
        # Base multimodal contribution: sum of squared distances to grid points
        multimodal = np.sum(min_distances**2)
        
        # Add a quadratic basin term that pulls towards the origin
        basin = 0.1 * np.sum(x**2)
        
        # Add sine-based interactions between dimensions to increase complexity
        interaction = 0.05 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        # Add noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(5 * x)**2)
        
        return multimodal + basin + interaction + noise