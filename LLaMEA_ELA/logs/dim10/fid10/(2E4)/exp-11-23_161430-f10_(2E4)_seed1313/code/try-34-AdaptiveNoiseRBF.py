import numpy as np

class AdaptiveNoiseRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute RBF centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        # Directional steering parameters
        self.directions = np.random.randn(10, dim)
        self.directions = self.directions / np.linalg.norm(self.directions, axis=1, keepdims=True)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.widths[i])**2)) * (i + 1)
        
        # Adaptive noise injection based on position
        noise_level = 0.1 * (1.0 + 0.5 * np.sin(np.sum(x**2) / 10.0))
        noise = np.random.normal(0.0, noise_level, self.dim)
        
        # Directional steering component
        steer_sum = 0.0
        for i in range(10):
            proj = np.dot(x - self.centers[i], self.directions[i])
            steer_sum += proj * np.exp(-0.1 * np.sum((x - self.centers[i])**2))
        
        # Cross-dimensional interaction with cosine modulation
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.cos(0.5 * x[i]) * np.sin(0.3 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Combine all terms with dynamic weighting
        result = 0.6 * rbf_sum + 0.2 * steer_sum + 0.1 * cross_term + 0.1 * np.sum(noise**2)
        
        return result