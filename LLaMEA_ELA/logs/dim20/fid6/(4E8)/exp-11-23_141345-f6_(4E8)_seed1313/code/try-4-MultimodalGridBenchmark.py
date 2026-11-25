import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case (can be extended)
        if dim == 2:
            # Create a 3x3 grid of global minima
            grid_positions = np.linspace(-4.0, 4.0, 3)
            for x in grid_positions:
                for y in grid_positions:
                    self.global_minima.append([x, y])
        else:
            # For higher dimensions, create a simple grid structure
            grid_positions = np.linspace(-4.0, 4.0, int(np.ceil(2**(dim/2))))
            if len(grid_positions) > 0:
                # Create tensor product of grid positions for multiple dimensions
                self.global_minima = []
                for i in range(min(100, len(grid_positions)**min(dim, 3))):
                    coords = []
                    temp = i
                    for j in range(min(dim, 3)):
                        coords.append(grid_positions[temp % len(grid_positions)])
                        temp //= len(grid_positions)
                    if len(coords) < dim:
                        coords.extend([0.0] * (dim - len(coords)))
                    self.global_minima.append(coords)

    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base parabolic term that creates a deceptive basin
        parabola_term = np.sum((x - 0.5)**2) * 0.1
        
        # Multimodal term with multiple global minima
        multimodal_term = 0.0
        if len(self.global_minima) > 0:
            for min_pos in self.global_minima[:min(10, len(self.global_minima))]:
                dist = np.sum((x - np.array(min_pos))**2)
                # Use a Gaussian-like function centered at each minimum
                multimodal_term += np.exp(-dist / 2.0) * 0.5
        
        # Add a small noise term to make it more challenging
        noise = 0.01 * np.sum(np.sin(x * 2.0))
        
        return parabola_term + multimodal_term + noise