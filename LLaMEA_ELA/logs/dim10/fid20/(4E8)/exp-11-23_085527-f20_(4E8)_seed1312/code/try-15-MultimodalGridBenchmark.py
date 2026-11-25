import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        # Create all combinations properly
        grids = [minima_positions] * dim
        meshgrid = np.meshgrid(*grids, indexing='ij')
        for i in range(len(meshgrid[0].flat)):
            point = [meshgrid[d].flat[i] for d in range(dim)]
            self.global_minima.append(point)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal term with multiple global minima
        multimodal = 0
        for i, center in enumerate(self.global_minima):
            distance = np.sum((x - np.array(center))**2)
            # Add a Gaussian-like contribution for each minimum
            multimodal += np.exp(-distance / 2.0) * (1.0 + 0.5 * np.sin(i))
        
        return basin - multimodal