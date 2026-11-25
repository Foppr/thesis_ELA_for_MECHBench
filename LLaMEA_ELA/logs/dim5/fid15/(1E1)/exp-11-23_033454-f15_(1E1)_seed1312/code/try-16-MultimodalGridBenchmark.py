import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create grid of global minima
            grid_points = np.linspace(-4.5, 4.5, 9)
            for i in range(9):
                for j in range(9):
                    self.global_minima.append([grid_points[i], grid_points[j]])
        else:
            # For higher dimensions, create a simpler structure
            self.global_minima = [[0.0] * dim]
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - pulls towards origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal term with multiple global minima
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use grid of global minima
            for min_pos in self.global_minima:
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                multimodal_term += np.exp(-dist**2 / 0.3) * 0.8
        else:
            # For higher dimensions, use a more general approach with cross-terms
            # Create multiple peaks around the grid points with interaction terms
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 1.5)**2 + (x[i+1] - 1.5)**2)
                    multimodal_term += np.exp(-dist**2 / 0.8) * 0.4
                    dist = np.sqrt((x[i] + 1.5)**2 + (x[i+1] + 1.5)**2)
                    multimodal_term += np.exp(-dist**2 / 0.8) * 0.4
            
            # Add cross-terms between dimensions for increased complexity
            cross_term = 0.0
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    cross_term += np.sin(x[i]) * np.cos(x[j])
            multimodal_term += 0.1 * cross_term
        
        # Add some noise to make it more challenging
        noise = 0.03 * np.random.random()
        
        return basin_term - multimodal_term + noise