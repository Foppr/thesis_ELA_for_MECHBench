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
        
        # Enhanced radial basis function component with chaotic modulation and exponential decay
        result = 0.0
        for i in range(self.dim):
            # Gaussian RBF with sinusoidal modulation on center, width, and amplitude
            center = 2.0 * np.sin(0.5 * i) + 0.5 * np.cos(0.3 * i) + 0.1 * np.sin(0.7 * i)
            width = 1.0 + 0.5 * np.sin(0.4 * i) + 0.2 * np.cos(0.6 * i)
            amplitude = 1.0 + 0.3 * np.sin(0.8 * i) + 0.1 * np.cos(0.5 * i)
            rbf = amplitude * np.exp(-0.5 * ((x_projected[i] - center) / width)**2)
            result += rbf * (1.0 + 0.3 * np.sin(2.0 * x_projected[i]) + 0.2 * np.cos(3.0 * x_projected[i]))
        
        # Add chaotic sinusoidal components with varying frequencies, amplitudes, and phases
        for i in range(self.dim):
            freq = 0.5 + 0.5 * np.sin(0.3 * i) + 0.1 * np.cos(0.4 * i)
            amp = 1.0 + 0.2 * np.cos(0.4 * i) + 0.1 * np.sin(0.6 * i)
            phase = 0.1 * np.sin(0.5 * i) + 0.05 * np.cos(0.3 * i)
            result += amp * np.sin(freq * x_projected[i] + phase) * np.cos(freq * x_projected[i]**2 + phase)
        
        # Dynamic conditioning based on distance from origin with exponential factor
        norm = np.linalg.norm(x_projected)
        condition_factor = 1.0 + 0.5 * np.sin(0.2 * norm) * np.cos(0.1 * norm) + 0.1 * np.exp(-0.1 * norm)
        result *= condition_factor
        
        # Add a multi-scale periodic component with varying periods and chaotic modulation
        for i in range(self.dim):
            period = 2.0 + 1.0 * np.sin(0.3 * i) + 0.3 * np.cos(0.5 * i)
            result += 2.0 * np.sin(2.0 * np.pi * x_projected[i] / period) * np.cos(3.0 * x_projected[i]) * (1.0 + 0.2 * np.sin(0.4 * x_projected[i]))
        
        # Add boundary penalty with exponential decay and chaotic perturbations
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                chaotic_factor = 1.0 + 0.2 * np.sin(0.5 * i) + 0.1 * np.cos(0.3 * i)
                boundary_penalty += 10.0 * np.exp(-dist_from_bound**2) * chaotic_factor
        result += boundary_penalty
        
        # Add a global scaling factor that varies with problem dimension and chaotic modulation
        global_scale = 1.0 + 0.1 * np.sin(0.1 * self.dim) + 0.05 * np.cos(0.05 * self.dim)
        result *= global_scale
        
        # Add a chaotic noise component to increase landscape irregularity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(5.0 * x_projected[i] + 0.3 * i) * np.cos(2.0 * x_projected[i]**3 + 0.2 * i)
        result += noise
        
        # Add a new component to improve performance metrics: enhanced cross-dimension coupling
        cross_dim_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_coupling += 0.3 * np.sin(x_projected[i] * x_projected[j]) * np.cos(0.5 * x_projected[i]**2 + 0.3 * x_projected[j]**2)
        result += cross_dim_coupling
        
        # Add a new component: fractional Brownian motion inspired chaotic modulation
        fbm_component = 0.0
        for i in range(self.dim):
            fbm_component += 0.2 * np.sin(0.7 * x_projected[i]) * np.cos(0.4 * x_projected[i]**3 + 0.1 * x_projected[i]**2)
        result += fbm_component
        
        # Mutation: Introduce a new chaotic interaction term with modified scaling and phase
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_interaction += 0.15 * np.sin(1.5 * x_projected[i] + 0.3 * x_projected[j]) * np.cos(0.8 * x_projected[i]**2 - 0.4 * x_projected[j]**2)
        result += chaotic_interaction
        
        # New mutation: Add a modified cross-dimension interaction with enhanced chaotic behavior
        enhanced_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                enhanced_coupling += 0.25 * np.sin(2.0 * x_projected[i] + 0.4 * x_projected[j]) * np.cos(0.6 * x_projected[i]**3 + 0.3 * x_projected[j]**3)
        result += enhanced_coupling
        
        # New mutation: Introduce a modified boundary penalty with additional chaotic modulation
        modified_boundary = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                chaotic_factor = 1.0 + 0.15 * np.sin(0.6 * i) + 0.08 * np.cos(0.4 * i)
                modified_boundary += 8.0 * np.exp(-dist_from_bound**2) * chaotic_factor
        result += modified_boundary
        
        # New mutation: Add a new chaotic component with polynomial interaction terms
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += 0.1 * np.sin(x_projected[i]**2 + 0.3 * x_projected[i]) * np.cos(0.5 * x_projected[i]**4 + 0.2 * x_projected[i]**2)
        result += poly_chaos
        
        return result