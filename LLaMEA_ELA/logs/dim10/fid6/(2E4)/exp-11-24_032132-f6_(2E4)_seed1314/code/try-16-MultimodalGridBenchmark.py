import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate grid of global minima
        self.global_minima = []
        if dim == 2:
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if i != 0 or j != 0:  # Exclude the center point which is also a minimum
                        self.global_minima.append([i * 1.5, j * 1.5])
            # Add center point as global minimum
            self.global_minima.append([0.0, 0.0])
            self.global_minima = np.array(self.global_minima)
        else:
            # For higher dimensions, create a reduced grid pattern
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if i != 0 or j != 0:
                        point = [i * 1.5, j * 1.5] + [0.0] * (dim - 2)
                        self.global_minima.append(point)
            # Add center point as global minimum
            self.global_minima.append([0.0] * dim)
            self.global_minima = np.array(self.global_minima)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal terms - sum of Gaussian peaks at global minima
        multimodal_term = 0.0
        for center in self.global_minima:
            dist = np.sqrt(np.sum((x - center)**2))
            multimodal_term += np.exp(-dist**2 / 0.5) * 0.5
        
        # Add a small noise term to make it non-trivial
        return basin_term + multimodal_term + np.random.normal(0, 0.01)