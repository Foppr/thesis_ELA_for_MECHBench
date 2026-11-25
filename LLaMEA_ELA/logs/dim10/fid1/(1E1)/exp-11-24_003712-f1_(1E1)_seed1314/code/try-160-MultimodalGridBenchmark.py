import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with different spacing
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.5, 4.5, num_minima_per_dim)
        for point in np.nditer(np.array(np.meshgrid(*[minima_positions] * dim, indexing='ij'))):
            self.global_minima.append(point)
        
        # Add central minimum with different characteristics
        self.global_minima.append(np.zeros(dim))
        self.global_minima = np.array(self.global_minima)

    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Quadratic basin term with modified coefficient
        basin_term = 0.05 * np.sum(x**2, axis=1)
        
        # Multimodal term with multiple global minima and modified sinusoidal modulation
        multimodal_term = np.zeros(x.shape[0])
        
        for i in range(len(self.global_minima)):
            center = self.global_minima[i]
            dist = np.sum((x - center)**2, axis=1)
            # Add a Gaussian-like attraction with frequency modulation and phase shift
            freq_mod = 1.0 + 0.3 * np.sin(i * 0.785)  # Phase shift for each minimum
            multimodal_term += np.exp(-dist / (2.0 * freq_mod)) * (1.0 + 0.4 * np.sin(i * 1.57 + 0.5))
        
        # Combine terms with different weights
        return basin_term + 0.6 * multimodal_term