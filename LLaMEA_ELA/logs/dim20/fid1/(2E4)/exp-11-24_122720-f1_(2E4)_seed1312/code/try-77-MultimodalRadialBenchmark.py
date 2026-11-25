import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 2))
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Radial basis function component with adaptive centers and widths
        rbf_component = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 3))
            rbf_component += np.exp(-width * (x[i] - center)**2)
        
        # Adaptive penalty term based on distance from origin
        origin_distance = np.linalg.norm(x)
        penalty_factor = 1.0 + 0.8 * np.sin(origin_distance * np.pi / 10.0)
        penalty_component = penalty_factor * (origin_distance**2) / (1.0 + origin_distance)
        
        # Cross-term interaction with varying coupling strengths
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.4 * np.sin((i + j) * np.pi / (self.dim + 4))
                cross_term += coupling * x[i] * x[j] * np.cos(x[i] + x[j])
        
        # Global scaling and normalization
        scale_factor = 1.0 + 0.2 * np.cos(self.dim * np.pi / 8)
        
        # Combine components with dynamic weights
        weight1 = 0.4 + 0.1 * np.sin(self.dim * np.pi / 5)
        weight2 = 0.3 + 0.15 * np.cos(self.dim * np.pi / 6)
        weight3 = 0.2 + 0.1 * np.sin(self.dim * np.pi / 7)
        weight4 = 0.1 + 0.05 * np.cos(self.dim * np.pi / 9)
        
        return weight1 * sin_component + weight2 * rbf_component + weight3 * penalty_component + weight4 * cross_term * scale_factor