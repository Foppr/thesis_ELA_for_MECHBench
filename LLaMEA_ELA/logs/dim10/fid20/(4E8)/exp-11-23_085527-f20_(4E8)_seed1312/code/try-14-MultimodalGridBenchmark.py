import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        # Use list comprehension to avoid tuple issues
        minima_list = [list(point) for point in np.nditer(np.meshgrid(*[minima_positions] * dim, indexing='ij'), flags=['multi_index'])]
        self.global_minima = minima_list
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal term with multiple global minima
        multimodal = 0
        for i in range(len(self.global_minima)):
            center = np.array(self.global_minima[i])
            distance = np.sum((x - center)**2)
            # Add a Gaussian-like contribution for each minimum
            multimodal += np.exp(-distance / 2.0) * (1.0 + 0.5 * np.sin(i))
        
        return basin - multimodal