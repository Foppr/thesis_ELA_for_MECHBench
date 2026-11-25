import numpy as np

class SpiralRadialBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Spiral parameters for each dimension
        self.spiral_amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        self.spiral_frequencies = np.random.uniform(1.0, 8.0, size=dim)
        self.spiral_phases = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        # Adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequencies = np.random.uniform(0.5, 5.0, size=dim)
        # Condition number variation
        self.condition_numbers = np.random.uniform(1.0, 100.0, size=dim)
        # Basin depth and location parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=(8, dim))
        self.basin_depths = np.random.uniform(1.0, 10.0, size=8)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spiral component
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 1e-8)  # Avoid division by zero
            theta = np.arctan2(x[i], 1.0)  # Simplified angle calculation
            spiral_val = self.spiral_amplitudes[i] * np.sin(self.spiral_frequencies[i] * theta + self.spiral_phases[i]) * np.exp(-r / (2 * self.condition_numbers[i]))
            spiral += spiral_val
            
        # Radial basis function component
        rbf = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i])**2)
            rbf_val = np.exp(-dist / (2 * self.rbf_widths[i]**2))
            rbf += rbf_val
            
        # Basin component with varying depths
        basin = 0.0
        for i in range(8):
            dist = np.sum((x - self.basin_centers[i])**2)
            basin_val = self.basin_depths[i] * (1.0 / (1.0 + dist))
            basin += basin_val
            
        # Adaptive noise component
        noise = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x[i])
            noise += noise_val
            
        # Combine all components with varying weights
        return (1.5 * spiral + 
                1.2 * rbf + 
                1.3 * basin + 
                0.8 * noise)