import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for sinusoidal components
        self.sin_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Generate random parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        self.rbf_heights = np.random.uniform(1.0, 5.0, size=10)
        
        # Generate adaptive noise parameters
        self.noise_amp = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_freq = np.random.uniform(0.5, 4.0, size=dim)
        self.noise_decay = np.random.uniform(0.1, 0.8, size=dim)
        
        # Generate scaling and rotation parameters
        self.scaling = np.random.uniform(0.5, 2.0, size=dim)
        self.rotation_angles = np.random.uniform(-np.pi/4, np.pi/4, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply scaling and rotation
        x_scaled = x * self.scaling
        x_rotated = np.dot(x_scaled, self.rotation_angles)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.sin_amp[i] * np.sin(self.sin_freq[i] * x_rotated[i] + self.sin_phase[i])
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            dist = np.sum((x_rotated - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_heights[i] * np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amp[i] * np.sin(self.noise_freq[i] * x_rotated[i]) * np.exp(-self.noise_decay[i] * np.abs(x_rotated[i]))
            noise_component += noise_val
            
        # Combine components with appropriate weights
        return 0.8 * sin_component + 1.2 * rbf_component + 0.5 * noise_component