import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute random projections for cross-dimension interactions
        self.projection_matrix = np.random.randn(dim, dim)
        self.projection_matrix, _ = np.linalg.qr(self.projection_matrix)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply random projection to induce cross-dimension coupling
        x_projected = self.projection_matrix @ x
        
        # Radial basis function component with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            # Gaussian RBF with sinusoidal modulation on center and width
            center = 2.5 * np.sin(0.6 * i) + 0.6 * np.cos(0.4 * i)
            width = 1.2 + 0.6 * np.sin(0.5 * i)
            rbf = np.exp(-0.5 * ((x_projected[i] - center) / width)**2)
            result += rbf * (1.0 + 0.4 * np.sin(2.5 * x_projected[i]))
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 0.6 + 0.6 * np.sin(0.4 * i)
            amp = 1.2 + 0.3 * np.cos(0.5 * i)
            result += amp * np.sin(freq * x_projected[i]) * np.cos(freq * x_projected[i]**2)
        
        # Dynamic conditioning based on distance from origin
        norm = np.linalg.norm(x_projected)
        condition_factor = 1.0 + 0.6 * np.sin(0.25 * norm) * np.cos(0.15 * norm)
        result *= condition_factor
        
        # Add a multi-scale periodic component with varying periods
        for i in range(self.dim):
            period = 2.5 + 1.5 * np.sin(0.4 * i)
            result += 2.5 * np.sin(2.0 * np.pi * x_projected[i] / period) * np.cos(3.5 * x_projected[i])
        
        # Add boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                boundary_penalty += 12.0 * np.exp(-dist_from_bound**2)
        result += boundary_penalty
        
        # Add a global scaling factor that varies with problem dimension
        global_scale = 1.0 + 0.15 * np.sin(0.15 * self.dim)
        result *= global_scale
        
        return result