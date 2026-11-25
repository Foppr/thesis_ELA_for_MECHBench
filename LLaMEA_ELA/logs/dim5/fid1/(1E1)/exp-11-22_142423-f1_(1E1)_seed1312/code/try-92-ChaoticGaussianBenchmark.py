import numpy as np

class ChaoticGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for chaotic mixing
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation for chaotic mixing
        x_rot = self.rotation_matrix @ x
        
        # Base quadratic term
        f = np.sum(x_rot**2)
        
        # Add multiple Gaussian peaks with varying positions and heights
        peak_positions = np.random.uniform(-3, 3, (5, self.dim))
        peak_heights = np.random.uniform(0.5, 2.0, 5)
        
        for i in range(5):
            peak_dist = np.sum((x_rot - peak_positions[i])**2)
            f += peak_heights[i] * np.exp(-peak_dist / 4.0)
            
        # Add sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(3 * x_rot[i]) * np.cos(2 * x_rot[(i + 1) % self.dim])
            
        # Add chaotic cross-dimensional coupling terms
        for i in range(self.dim):
            f += 0.3 * np.sin(5 * x_rot[i]) * np.cos(4 * x_rot[(i + 2) % self.dim]) * np.sin(6 * x_rot[(i + 3) % self.dim])
            
        # Add irregular penalty terms
        f += 0.2 * np.sum(np.abs(x_rot)**1.5) + 0.1 * np.sum(x_rot**4)
        
        # Add higher-order polynomial interactions
        for i in range(self.dim):
            f += 0.05 * x_rot[i]**6 + 0.08 * x_rot[i]**5
            
        return f