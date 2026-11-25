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
            # Generate a set of representative points for higher dimensions
            self.global_minima = []
            if dim >= 2:
                # Create a simple pattern that works in any dimension
                base_points = np.linspace(-4.0, 4.0, 5)
                if dim == 3:
                    for x in base_points:
                        for y in base_points:
                            for z in base_points:
                                self.global_minima.append([x, y, z])
                else:
                    # For higher dimensions, use a reduced grid
                    for i in range(3):
                        point = [base_points[(i*3) % len(base_points)]] * dim
                        self.global_minima.append(point)
    
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
                multimodal_term += np.exp(-dist**2 / 0.5) * 0.5
        else:
            # For higher dimensions, use a more consistent approach
            # Use a subset of global minima for higher dimensions
            num_minima = min(len(self.global_minima), 10)
            for i in range(num_minima):
                min_pos = self.global_minima[i]
                dist = np.sqrt(np.sum((x - np.array(min_pos))**2))
                multimodal_term += np.exp(-dist**2 / 1.0) * 0.3
        
        # Add some noise to make it more challenging
        noise = 0.05 * np.random.random()
        
        return basin_term - multimodal_term + noise