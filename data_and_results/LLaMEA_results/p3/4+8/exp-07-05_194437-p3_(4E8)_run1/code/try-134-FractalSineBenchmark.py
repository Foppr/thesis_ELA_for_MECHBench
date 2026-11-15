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
            # Base polynomial chaos term with sine modulation
            poly_term = x_projected[i]**2 + 0.5 * np.sin(3.0 * x_projected[i])
            # Fractal-like sine-wave interaction
            fractal_interaction = 0.3 * np.sin(2.0 * np.pi * x_projected[i]) * np.cos(0.5 * np.pi * x_projected[i]**2)
            result += poly_term * fractal_interaction
        
        # Add adaptive conditioning based on dimensionality and chaotic modulation
        adaptive_factor = 1.0 + 0.2 * np.sin(0.1 * self.dim) + 0.1 * np.cos(0.05 * self.dim)
        result *= adaptive_factor
        
        # Add complex fitness valleys with multi-scale periodic components
        for i in range(self.dim):
            # Multi-scale periodic components with varying periods and amplitudes
            period1 = 1.0 + 0.5 * np.sin(0.2 * i)
            period2 = 2.0 + 0.3 * np.cos(0.3 * i)
            result += 1.5 * np.sin(2.0 * np.pi * x_projected[i] / period1) * np.cos(2.0 * np.pi * x_projected[i] / period2)
        
        # Add boundary penalty with exponential decay and fractal perturbations
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                fractal_factor = 1.0 + 0.1 * np.sin(0.3 * i) + 0.05 * np.cos(0.2 * i)
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2) * fractal_factor
        result += boundary_penalty
        
        # Add a chaotic noise component to increase landscape irregularity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(4.0 * x_projected[i] + 0.2 * i) * np.cos(1.5 * x_projected[i]**3 + 0.1 * i)
        result += noise
        
        # Add a novel component: enhanced cross-dimension coupling with fractal modulation
        cross_dim_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_coupling = 0.2 * np.sin(0.5 * x_projected[i]) * np.cos(0.3 * x_projected[j]) * np.sin(0.4 * x_projected[i] * x_projected[j])
                cross_dim_coupling += fractal_coupling
        result += cross_dim_coupling
        
        # Add a global scaling factor that varies with problem dimension and fractal modulation
        global_scale = 1.0 + 0.15 * np.sin(0.1 * self.dim) + 0.08 * np.cos(0.08 * self.dim)
        result *= global_scale
        
        return result