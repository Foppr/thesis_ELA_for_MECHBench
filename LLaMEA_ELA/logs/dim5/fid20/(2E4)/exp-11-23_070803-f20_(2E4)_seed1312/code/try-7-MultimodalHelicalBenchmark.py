import numpy as np

class MultimodalHelicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.n_minima = 12
        self.minima_positions = []
        # Precompute global minima positions in a helical pattern for 2D case
        if dim == 2:
            radius = 4.0
            for i in range(self.n_minima):
                angle = 2 * np.pi * i / self.n_minima
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                self.minima_positions.append([x, y])
        else:
            # For higher dimensions, create a helical pattern in a subspace
            for i in range(self.n_minima):
                angle = 2 * np.pi * i / self.n_minima
                pos = np.zeros(dim)
                if dim >= 2:
                    pos[0] = 4.0 * np.cos(angle)
                    pos[1] = 4.0 * np.sin(angle)
                self.minima_positions.append(pos.tolist())
    
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Quadratic basin term (central attraction)
        basin_term = np.sum(x_norm**2) * 0.1
        
        # Multimodal term with helical global minima
        multimodal_term = 0
        for min_point in self.minima_positions:
            dist = np.sum((x_norm - np.array(min_point))**2)
            # Use a Gaussian-like function centered at each minimum
            multimodal_term += np.exp(-dist * 3.0) * 0.8
        
        # Add a periodic component to increase complexity
        periodic_term = 0
        for i in range(self.dim):
            periodic_term += np.sin(3 * x[i]) * 0.2
        
        return basin_term + multimodal_term + periodic_term