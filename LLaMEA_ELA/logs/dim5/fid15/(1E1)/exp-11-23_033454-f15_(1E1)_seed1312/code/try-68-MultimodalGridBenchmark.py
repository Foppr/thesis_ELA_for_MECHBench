import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case
        if dim == 2:
            # Create grid of global minima with tighter spacing and varied heights
            grid_points = np.linspace(-4.5, 4.5, 9)
            for i in range(9):
                for j in range(9):
                    self.global_minima.append([grid_points[i], grid_points[j]])
        else:
            # For higher dimensions, create a more complex structure
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
        
        # Quadratic basin term with variable conditioning
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal term with multiple global minima using variable exponential decay
        multimodal_term = 0.0
        
        if self.dim == 2:
            # For 2D, use grid of global minima with varying decay rates and heights
            for i, min_pos in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                # Use variable decay rate based on position
                decay_rate = 0.2 + 0.3 * np.sin(i * 0.5)
                height = 0.5 + 0.5 * np.cos(i * 0.3)
                multimodal_term += height * np.exp(-dist**2 / decay_rate)
        else:
            # For higher dimensions, use complex cross-dimensional interaction terms
            # Add interaction between pairs of dimensions with varying strengths
            for i in range(0, self.dim, 2):
                if i + 1 < self.dim:
                    dist = np.sqrt((x[i] - 2.0)**2 + (x[i+1] - 2.0)**2)
                    strength = 0.7 + 0.3 * np.sin(i * 0.4)
                    multimodal_term += strength * np.exp(-dist**2 / 0.5)
                    dist = np.sqrt((x[i] + 2.0)**2 + (x[i+1] + 2.0)**2)
                    multimodal_term += strength * np.exp(-dist**2 / 0.5)
            
            # Add additional interaction terms between non-adjacent dimensions
            for i in range(min(4, self.dim)):
                if i + 3 < self.dim:
                    dist = np.sqrt((x[i] - 1.0)**2 + (x[i+3] - 1.0)**2)
                    strength = 0.4 + 0.2 * np.cos(i * 0.6)
                    multimodal_term += strength * np.exp(-dist**2 / 0.7)
                    dist = np.sqrt((x[i] + 1.0)**2 + (x[i+3] + 1.0)**2)
                    multimodal_term += strength * np.exp(-dist**2 / 0.7)
            
            # Add a complex interaction term with a sinusoidal pattern
            for i in range(self.dim):
                if i + 1 < self.dim:
                    # Create a sinusoidal modulation to the interaction
                    modulation = 1.0 + 0.3 * np.sin(x[i] * 0.5)
                    dist = np.sqrt((x[i] - 1.5)**2 + (x[i+1] - 1.5)**2)
                    multimodal_term += modulation * np.exp(-dist**2 / 0.6)
        
        # Add a complex conditioning term that varies across dimensions
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (i + 1) * x[i]**4
        
        # Combine all terms with different weights
        return basin_term + condition_term - multimodal_term