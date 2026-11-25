import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Define grid of global minima
        grid_size = 3
        grid_points = np.linspace(-4.0, 4.0, grid_size)
        minima_positions = np.array(np.meshgrid(*[grid_points] * self.dim, indexing='ij')).T.reshape(-1, self.dim)
        
        # Calculate distance to all minima and find the closest one
        # Use broadcasting to compute all distances at once
        distances = np.sqrt(np.sum((minima_positions[:, np.newaxis] - x) ** 2, axis=2))
        closest_minima_idx = np.argmin(distances)
        closest_minima = minima_positions[closest_minima_idx]
        
        # Base function: quadratic basin around the closest minimum
        base_value = np.sum((x - closest_minima) ** 2) / (2.0 * self.dim)
        
        # Add sinusoidal perturbations to create multimodality - deterministic version
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Add noise term - make it deterministic for reproducibility
        np.random.seed(hash(tuple(x)) % (2**32))
        noise = 0.1 * np.random.random()
        
        return base_value + 0.5 * perturbation + noise