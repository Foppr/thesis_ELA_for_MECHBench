import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with sinusoidal shift
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        for point in np.nditer(np.array(np.meshgrid(*[minima_positions] * dim, indexing='ij'))):
            # Apply sinusoidal shift to create more complex landscape
            shifted_point = point + 0.5 * np.sin(point)
            self.global_minima.append(shifted_point)
        
        # Add central minimum with different characteristics
        self.global_minima.append(np.zeros(dim))
        self.global_minima = np.array(self.global_minima)

    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Quadratic basin term
        basin_term = 0.1 * np.sum(x**2, axis=1)
        
        # Multimodal term with multiple global minima
        multimodal_term = np.zeros(x.shape[0])
        
        for i in range(len(self.global_minima)):
            center = self.global_minima[i]
            dist = np.sum((x - center)**2, axis=1)
            # Add a Gaussian-like attraction to each minimum with sinusoidal modulation
            multimodal_term += np.exp(-dist / 3.0) * (1.0 + 0.3 * np.sin(i * 0.5 + np.sum(x, axis=1) * 0.1))
        
        # Combine terms with different weights
        return basin_term + 0.6 * multimodal_term