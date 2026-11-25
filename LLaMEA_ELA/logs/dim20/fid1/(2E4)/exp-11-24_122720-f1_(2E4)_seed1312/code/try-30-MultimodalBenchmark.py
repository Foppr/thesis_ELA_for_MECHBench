import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 2 ** (i % 3)  # Varying frequencies: 1, 2, 4
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i] * np.pi / 4)
        
        # Radial basis function with dynamic centers and adaptive widths
        rbf_component = 0
        for i in range(self.dim):
            center = 3 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1 + 0.2 * np.sin(i))
        
        # Elliptic penalty term with anisotropic scaling
        elliptic_penalty = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            elliptic_penalty += (x[i]**2) / (scale + 0.1) + 0.1 * x[i]**4
        
        # Adaptive dimensionality scaling
        dim_scale = 1.0 + 0.1 * np.sin(self.dim * np.pi / 6)
        
        # Combine components with dynamic weights
        weight1 = 0.5 + 0.2 * np.cos(self.dim * np.pi / 8)
        weight2 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 4)
        weight3 = 0.2 + 0.05 * np.cos(self.dim * np.pi / 12)
        
        return weight1 * sin_component + weight2 * rbf_component + weight3 * elliptic_penalty * dim_scale + self.dim