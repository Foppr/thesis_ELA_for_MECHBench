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
        # Convert to numpy array and ensure correct dimension
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        
        if len(x) != self.dim:
            raise ValueError(f"Input dimension {len(x)} must match the function dimension {self.dim}")
        
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
            # For higher dimensions, use a more general approach
            # Create multiple peaks around the grid points
            for i in range(0, min(self.dim, 4), 2):  # Only use first 4 dimensions for peak creation
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 2.0)**2 + (x[i+1] - 2.0)**2)
                    multimodal_term += np.exp(-dist**2 / 1.0) * 0.3
                    dist = np.sqrt((x[i] + 2.0)**2 + (x[i+1] + 2.0)**2)
                    multimodal_term += np.exp(-dist**2 / 1.0) * 0.3
        
        # Add deterministic noise to make it more challenging
        noise = 0.05 * np.sin(x[0]) * np.cos(x[1]) if self.dim >= 2 else 0.0
        
        return basin_term - multimodal_term + noise