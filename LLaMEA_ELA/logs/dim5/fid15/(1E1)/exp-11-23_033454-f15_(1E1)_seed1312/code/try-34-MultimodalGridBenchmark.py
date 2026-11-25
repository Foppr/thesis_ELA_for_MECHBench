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
        # Ensure input is a numpy array and has correct dimension
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        
        if len(x) != self.dim:
            raise ValueError(f"Input dimension {len(x)} must match function dimension {self.dim}")
        
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
            # For higher dimensions, use a more general approach with multiple peaks
            # Create peaks at regular grid points in each dimension
            peak_positions = np.linspace(-4.0, 4.0, 5)
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    # Add peaks at (peak_pos, peak_pos) and (-peak_pos, -peak_pos)
                    dist1 = np.sqrt((x[i] - peak_positions[1])**2 + (x[i+1] - peak_positions[1])**2)
                    dist2 = np.sqrt((x[i] + peak_positions[1])**2 + (x[i+1] + peak_positions[1])**2)
                    multimodal_term += (np.exp(-dist1**2 / 0.8) + np.exp(-dist2**2 / 0.8)) * 0.4
                else:
                    # Handle odd dimensions by adding a single peak
                    dist = np.sqrt((x[i] - peak_positions[2])**2)
                    multimodal_term += np.exp(-dist**2 / 0.6) * 0.3
        
        # Add controlled noise to make it more challenging but deterministic for same inputs
        np.random.seed(int(sum(x) * 1000) % 1000000)  # Deterministic seed based on input
        noise = 0.02 * np.random.random()
        
        return basin_term - multimodal_term + noise