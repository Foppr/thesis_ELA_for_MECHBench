import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for non-linearity and sensitivity
        tent_component = 0
        a = 1.5  # Control parameter for tent map
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent_val = a * xi
            else:
                tent_val = a * (1 - xi)
            tent_component += tent_val * np.sin(xi * np.pi)
        
        # Adaptive quadratic form with varying curvature and rotation
        quad_component = 0
        for i in range(self.dim):
            # Dynamic scaling based on dimension
            scale = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            # Rotational term for conditioning variation
            rot_term = np.cos(0.5 * i * np.pi / self.dim) * x[i]**2
            quad_component += scale * (x[i]**2 + rot_term)
        
        # Saddle-point penalty with hyperbolic tangent shaping
        saddle_penalty = 0
        for i in range(self.dim):
            # Create saddle points via tanh-based penalty
            saddle_val = np.tanh(x[i] * 0.5) * np.cos(x[i] * np.pi / 4)
            saddle_penalty += saddle_val**2
        
        # Dimensionality-dependent modulation
        dim_mod = 1.0 + 0.2 * np.cos(self.dim * np.pi / 6)
        
        # Combine components with dynamic weights
        weight1 = 0.4 + 0.1 * np.sin(self.dim * np.pi / 8)
        weight2 = 0.35 + 0.05 * np.cos(self.dim * np.pi / 4)
        weight3 = 0.25 + 0.05 * np.sin(self.dim * np.pi / 12)
        
        return weight1 * tent_component + weight2 * quad_component + weight3 * saddle_penalty * dim_mod + self.dim