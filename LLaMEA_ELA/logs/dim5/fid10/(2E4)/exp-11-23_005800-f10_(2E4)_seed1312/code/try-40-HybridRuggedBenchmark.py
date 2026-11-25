import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay attraction fields centered at regular grid points
        attraction = 0.0
        grid_points = np.linspace(-1, 1, 5)
        for i in range(len(grid_points)):
            for j in range(len(grid_points)):
                if self.dim >= 2:
                    xi = grid_points[i]
                    xj = grid_points[j]
                    dist = np.sqrt((x_norm[0] - xi)**2 + (x_norm[1] - xj)**2)
                    attraction += np.exp(-dist * 5) * np.cos(dist * np.pi)
        
        # Sinusoidal modulation based on angular position in higher dimensions
        sin_modulation = 0.0
        if self.dim > 1:
            for i in range(0, self.dim - 1):
                angle = np.arctan2(x_norm[i+1], x_norm[i])
                sin_modulation += np.sin(angle * 7) * np.cos(angle * 3)
        
        # Radial symmetry with polynomial scaling
        r = np.linalg.norm(x_norm)
        radial_term = r**4 + 0.5 * r**2
        
        # Cross-dimensional interaction via multivariate Gaussian
        gaussian_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                gaussian_interaction += np.exp(-((x_norm[i] - x_norm[j])**2) / 0.5)
        
        # Combined function value
        f_val = radial_term + 2.0 * attraction + 0.3 * sin_modulation + 0.5 * gaussian_interaction
        
        return f_val