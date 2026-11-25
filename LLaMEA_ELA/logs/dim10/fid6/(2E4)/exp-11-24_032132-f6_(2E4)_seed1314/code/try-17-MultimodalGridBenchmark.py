import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with shifted positions
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i != 0 or j != 0:  # Exclude the center point which is also a minimum
                    self.global_minima.append([i * 1.5 + 0.1 * i, j * 1.5 + 0.1 * j])
        
        # Add center point as global minimum with slight shift
        self.global_minima.append([0.05, -0.05])
        self.global_minima = np.array(self.global_minima)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # For 2D case (most common for benchmarking)
        if self.dim == 2:
            # Quadratic basin term with modified coefficient
            basin_term = 0.2 * (x[0]**2 + x[1]**2)
            
            # Multimodal terms - sum of Gaussian peaks at global minima with modified variance
            multimodal_term = 0.0
            for center in self.global_minima:
                dist = np.sqrt((x[0] - center[0])**2 + (x[1] - center[1])**2)
                multimodal_term += np.exp(-dist**2 / 0.3) * 0.8
            
            # Add a small noise term to make it non-trivial
            return basin_term + multimodal_term + np.random.normal(0, 0.01)
        
        else:
            # For higher dimensions, use a similar principle but with reduced complexity
            # Quadratic basin in first two dimensions with modified coefficient
            basin_term = 0.2 * (x[0]**2 + x[1]**2)
            
            # Multimodal term based on distance to some key points with interaction terms
            multimodal_term = 0.0
            key_points = [[i, j] for i in range(-2, 3) for j in range(-2, 3)]
            
            for point in key_points:
                dist = np.sqrt(sum((x[i] - point[i%2])**2 for i in range(self.dim)))
                multimodal_term += np.exp(-dist**2 / 0.3) * 0.8
            
            return basin_term + multimodal_term + np.random.normal(0, 0.01)