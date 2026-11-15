import numpy as np

class FractalSineBenchmark:
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
        
        # Polynomial chaos expansion component with fractal sine-wave interactions
        result = 0.0
        for i in range(self.dim):
            # Fractal-like sine-wave with varying frequencies and amplitudes
            freq = 1.0 + 0.5 * np.sin(0.3 * i) + 0.2 * np.cos(0.4 * i)
            amp = 1.0 + 0.3 * np.sin(0.5 * i) + 0.1 * np.cos(0.6 * i)
            phase = 0.1 * np.sin(0.4 * i) + 0.05 * np.cos(0.3 * i)
            result += amp * np.sin(freq * x_projected[i] + phase) * np.cos(freq * x_projected[i]**2 + phase)
        
        # Add adaptive conditioning based on dimensionality
        adaptive_factor = 1.0 + 0.2 * np.sin(0.1 * self.dim) + 0.1 * np.cos(0.05 * self.dim)
        result *= adaptive_factor
        
        # Add multi-scale periodic component with chaotic modulation
        for i in range(self.dim):
            period = 2.0 + 1.0 * np.sin(0.3 * i) + 0.3 * np.cos(0.5 * i)
            result += 1.5 * np.sin(2.0 * np.pi * x_projected[i] / period) * np.cos(3.0 * x_projected[i])
        
        # Add boundary penalty with fractal-like behavior
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                fractal_factor = 1.0 + 0.2 * np.sin(0.5 * i) + 0.1 * np.cos(0.3 * i)
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2) * fractal_factor
        result += boundary_penalty
        
        # Add a global scaling factor that varies with problem dimension and fractal modulation
        global_scale = 1.0 + 0.1 * np.sin(0.1 * self.dim) + 0.05 * np.cos(0.05 * self.dim)
        result *= global_scale
        
        # Add fractal noise component to increase landscape irregularity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(3.0 * x_projected[i] + 0.2 * i) * np.cos(1.5 * x_projected[i]**3 + 0.1 * i)
        result += noise
        
        # Add a new component: enhanced cross-dimension coupling with fractal structure
        cross_dim_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_coupling += 0.2 * np.sin(x_projected[i] * x_projected[j]) * np.cos(0.3 * x_projected[i]**2 + 0.2 * x_projected[j]**2)
        result += cross_dim_coupling
        
        # Add a new component: polynomial chaos expansion with adaptive weights
        chaos_component = 0.0
        for i in range(self.dim):
            chaos_component += 0.1 * np.sin(0.8 * x_projected[i]) * np.cos(0.6 * x_projected[i]**3 + 0.1 * x_projected[i]**2)
        result += chaos_component
        
        return result