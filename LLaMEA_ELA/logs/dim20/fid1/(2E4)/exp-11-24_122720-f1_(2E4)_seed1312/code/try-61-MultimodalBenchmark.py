import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) / self.dim
            amp = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            sin_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Radial basis function with dynamic centers and widths
        rbf_component = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.5 + 0.5 * np.cos(i * np.pi / (self.dim + 2))
            rbf_component += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Conditioning penalty with exponential scaling
        cond_penalty = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            cond_penalty += scale * (x[i]**4 + x[i]**2) + 0.1 * x[i]**6
        
        # Cross-dimensional interaction term
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) / (1 + abs(x[i] - x[j]))
        
        # Global scaling factor
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * np.pi / 4)
        
        # Combine components with dynamic weights
        weight1 = 0.3 + 0.2 * np.cos(self.dim * np.pi / 6)
        weight2 = 0.4 + 0.1 * np.sin(self.dim * np.pi / 7)
        weight3 = 0.3 + 0.15 * np.cos(self.dim * np.pi / 8)
        
        return weight1 * sin_component + weight2 * rbf_component + weight3 * cond_penalty * scale_factor + cross_term