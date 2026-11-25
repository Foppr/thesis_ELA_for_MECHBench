import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create grid of global minima with tighter spacing
            grid_points = np.linspace(-4.0, 4.0, 7)
            for i in range(7):
                for j in range(7):
                    self.global_minima.append([grid_points[i], grid_points[j]])
        else:
            # For higher dimensions, create a simpler structure
            self.global_minima = [[0.0] * dim]
    
    def f(self, x):
        if len(x) != self.dim:
            # If dimension doesn't match, adjust x to fit
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term - pulls towards origin with stronger conditioning
        basin_term = 0.2 * np.sum(x**2)
        
        # Multimodal term with multiple global minima using modified exponential decay
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use grid of global minima with tighter spacing and stronger peaks
            for min_pos in self.global_minima:
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                multimodal_term += np.exp(-dist**2 / 0.3) * 0.8
        else:
            # For higher dimensions, use cross-dimensional interaction terms
            # Add interaction between pairs of dimensions to increase complexity
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 1.5)**2 + (x[i+1] - 1.5)**2)
                    multimodal_term += np.exp(-dist**2 / 0.4) * 0.6
                    dist = np.sqrt((x[i] + 1.5)**2 + (x[i+1] + 1.5)**2)
                    multimodal_term += np.exp(-dist**2 / 0.4) * 0.6
            
            # Add additional interaction terms between non-adjacent dimensions
            for i in range(min(3, self.dim)):
                if i + 2 < self.dim:
                    dist = np.sqrt((x[i] - 2.0)**2 + (x[i+2] - 2.0)**2)
                    multimodal_term += np.exp(-dist**2 / 0.6) * 0.3
                    dist = np.sqrt((x[i] + 2.0)**2 + (x[i+2] + 2.0)**2)
                    multimodal_term += np.exp(-dist**2 / 0.6) * 0.3
        
        # Remove noise for deterministic evaluation
        return basin_term - multimodal_term