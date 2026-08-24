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
            center = 2.0 * np.sin(0.7 * i) + 0.5 * np.cos(0.4 * i)
            width = 1.5 + 0.3 * np.sin(0.5 * i)  # Increased base width and modulation
            rbf = np.exp(-0.5 * ((x_projected[i] - center) / width)**2)
            result += rbf * (1.0 + 0.4 * np.sin(3.0 * x_projected[i]))  # Increased sinusoidal modulation
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 0.7 + 0.3 * np.sin(0.4 * i)  # Slightly increased frequency range
            amp = 1.2 + 0.1 * np.cos(0.5 * i)   # Increased amplitude
            result += amp * np.sin(freq * x_projected[i]) * np.cos(freq * x_projected[i]**2)
        
        # Dynamic conditioning based on distance from origin
        norm = np.linalg.norm(x_projected)
        condition_factor = 1.0 + 0.7 * np.sin(0.3 * norm) * np.cos(0.15 * norm)  # Increased conditioning
        result *= condition_factor
        
        # Add a multi-scale periodic component with varying periods
        for i in range(self.dim):
            period = 2.5 + 0.8 * np.sin(0.4 * i)  # Increased period variation
            result += 2.5 * np.sin(2.0 * np.pi * x_projected[i] / period) * np.cos(3.5 * x_projected[i])
        
        # Add boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                boundary_penalty += 15.0 * np.exp(-dist_from_bound**2)  # Increased penalty
        result += boundary_penalty
        
        # Add a global scaling factor that varies with problem dimension
        global_scale = 1.0 + 0.15 * np.sin(0.12 * self.dim)  # Slight increase in scaling
        result *= global_scale
        
        return result