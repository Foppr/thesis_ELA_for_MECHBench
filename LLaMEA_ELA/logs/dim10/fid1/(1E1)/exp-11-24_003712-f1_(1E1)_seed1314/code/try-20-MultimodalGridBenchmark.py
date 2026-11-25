import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with shifted positions
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.5, 4.5, num_minima_per_dim)
        # Add some shift to make the landscape more complex
        shifts = np.random.uniform(-0.2, 0.2, size=(num_minima_per_dim**dim, dim))
        for i, point in enumerate(np.nditer(np.array(np.meshgrid(*[minima_positions] * dim, indexing='ij')))):
            shifted_point = point + shifts[i]
            self.global_minima.append(shifted_point)
        
        # Add central minimum with different characteristics
        self.global_minima.append(np.zeros(dim) + np.random.uniform(-0.1, 0.1, dim))
        self.global_minima = np.array(self.global_minima)

    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Quadratic basin term with modified coefficient
        basin_term = 0.05 * np.sum(x**2, axis=1)
        
        # Multimodal term with multiple global minima and different interaction strengths
        multimodal_term = np.zeros(x.shape[0])
        
        for i in range(len(self.global_minima)):
            center = self.global_minima[i]
            dist = np.sum((x - center)**2, axis=1)
            # Add a modified Gaussian-like attraction with frequency modulation
            freq_factor = 1.0 + 0.3 * np.sin(i * 0.5)
            multimodal_term += np.exp(-dist / (2.0 * freq_factor)) * (1.0 + 0.4 * np.cos(i * 0.7))
        
        # Combine terms with different weights
        return basin_term + 0.3 * multimodal_term