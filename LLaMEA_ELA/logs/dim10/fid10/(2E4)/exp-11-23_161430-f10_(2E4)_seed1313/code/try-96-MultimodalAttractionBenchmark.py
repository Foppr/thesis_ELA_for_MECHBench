import numpy as np

class MultimodalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize attraction centers and strengths
        self.centers = 3.0 * np.random.rand(dim, 5) - 1.5
        self.strengths = 2.0 + np.random.rand(5)
        # Radial basis function parameters
        self.rbf_widths = 0.5 + 1.5 * np.random.rand(5)
        # Sinusoidal components for additional complexity
        self.freqs = 1.0 + 2.0 * np.random.rand(dim)
        self.amps = 0.5 + 1.0 * np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(5):
            rbf_sum += self.strengths[i] * np.exp(-np.sum((x - self.centers[:, i])**2) / (2 * self.rbf_widths[i]**2))
        
        # Sinusoidal oscillation component
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x[i]) * np.cos(self.freqs[i] * x[i]**2)
        
        # Gradient-based attraction field
        attr_sum = 0.0
        for i in range(self.dim):
            dist_to_centers = np.sum((x - self.centers[i, :])**2, axis=0)
            attr_sum += np.sum(np.exp(-dist_to_centers / (2 * 0.5**2)) * (x[i] - self.centers[i, :]))
        
        # Quadratic penalty for distance from origin
        origin_penalty = 0.1 * np.sum(x**2)
        
        # Combine all components with varying weights
        result = 0.4 * rbf_sum + 0.3 * sin_sum + 0.2 * attr_sum + 0.1 * origin_penalty
        
        return result