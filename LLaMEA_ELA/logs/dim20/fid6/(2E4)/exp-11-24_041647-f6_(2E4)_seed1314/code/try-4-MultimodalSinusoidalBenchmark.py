import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define centers for radial basis functions
        self.centers = []
        grid_size = 5
        positions = np.linspace(-4.0, 4.0, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if i == 2 and j == 2:  # Skip center to avoid trivial solution
                    continue
                self.centers.append([positions[i], positions[j]])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Global quadratic basin term
        basin = 0.05 * np.sum(x**2)
        
        # Radial basis function terms
        rbf_sum = 0
        for center in self.centers:
            dist_sq = np.sum((x - np.array(center))**2)
            rbf_sum += 3.0 * np.exp(-dist_sq / 8.0)
        
        # Sinusoidal perturbation term
        sin_term = 2.0 * np.sin(0.5 * x[0]) * np.cos(0.5 * x[1])
        if self.dim > 2:
            for i in range(2, self.dim):
                sin_term *= np.sin(0.3 * x[i])
        
        return basin + rbf_sum + sin_term