import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create a grid of global minima
            grid_points = np.linspace(-4.5, 4.5, 9)
            for i in range(9):
                for j in range(9):
                    self.global_minima.append([grid_points[i], grid_points[j]])
        else:
            # For higher dimensions, create a representative set of global minima
            n_minima = 100
            for _ in range(n_minima):
                self.global_minima.append(np.random.uniform(-4.5, 4.5, dim).tolist())
    
    def f(self, x):
        # Ensure x is a numpy array
        x = np.array(x)
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Quadratic basin term (central attraction)
        basin_term = np.sum(x_norm**2) * 0.1
        
        # Multimodal term with multiple global minima
        multimodal_term = 0
        for min_point in self.global_minima:
            # Ensure min_point is a numpy array with correct shape
            min_point = np.array(min_point)
            if len(min_point) != len(x_norm):
                continue  # Skip if dimension mismatch
            dist = np.sum((x_norm - min_point)**2)
            # Use a Gaussian-like function centered at each minimum
            multimodal_term += np.exp(-dist * 2.0) * 0.5
        
        # Add a small noise term to make it more interesting
        noise = np.random.normal(0, 0.01) if len(x) == 2 else 0
        
        return basin_term + multimodal_term + noise