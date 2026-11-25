import numpy as np

class HybridRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (20, dim))
        self.widths = np.random.uniform(0.5, 2.0, 20)
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            width = self.widths[i]
            diff = x_scaled - center
            rbf_sum += np.exp(-0.5 * np.sum(diff**2) / (width**2))
        
        # Evolutionary noise component with temporal correlation
        noise = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Correlated noise with frequency modulation
            freq = 2 * np.pi * (i + 1) * (1 + 0.1 * np.sin(xi))
            noise += np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-0.1 * xi**2)
        
        # Polynomial scaling with variable exponents
        poly_scale = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            exp_factor = 1 + 0.5 * np.sin(i * np.pi / self.dim)
            poly_scale += xi**(2 + exp_factor) + 0.3 * xi**(3 + exp_factor)
        
        # Cross-dimensional interaction with distance-weighted terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interaction += (1 / (1 + dist)) * np.sin(5 * (x_scaled[i] + x_scaled[j]))
        
        # Combine all components with dynamic weighting
        total = 0.7 * rbf_sum + 0.2 * noise + 0.1 * poly_scale + 0.3 * interaction
        
        # Add global scaling and shift to ensure positive fitness
        return np.abs(total) + 0.5 * np.sin(self.dim)