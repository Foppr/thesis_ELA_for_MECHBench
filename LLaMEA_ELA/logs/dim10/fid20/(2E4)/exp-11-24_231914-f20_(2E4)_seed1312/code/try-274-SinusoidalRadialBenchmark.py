import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random frequencies for sinusoidal components
        self.frequencies = np.random.uniform(1.0, 8.0, size=dim)
        # Generate radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        # Generate adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequencies = np.random.uniform(2.0, 10.0, size=dim)
        # Generate rotation matrix for directional complexity
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix = self.rotation_matrix @ self.rotation_matrix.T
        self.rotation_matrix /= np.linalg.norm(self.rotation_matrix, axis=1, keepdims=True)
        
    def f(self, x):
        # Apply rotation to input
        x_rotated = self.rotation_matrix @ x
        
        # Sinusoidal component with multiple frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(self.frequencies[i] * x_rotated[i]) * np.cos(self.frequencies[i] * x_rotated[i])
        
        # Radial basis function component
        rbf = 0.0
        for i in range(15):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.sum((x_rotated - center) ** 2)
            rbf += np.exp(-distance / (2 * width ** 2))
        
        # Adaptive noise component
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_rotated[i])
        
        # Distance-based penalty to keep solution within bounds
        distance_penalty = np.sum(np.maximum(0, np.abs(x) - 5.0) ** 2)
        
        # Combine all components with different weights
        return 2.0 * sinusoidal + 1.5 * rbf + 0.8 * noise + 0.5 * distance_penalty