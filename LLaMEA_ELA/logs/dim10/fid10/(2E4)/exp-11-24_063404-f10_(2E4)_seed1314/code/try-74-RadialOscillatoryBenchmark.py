import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for radial oscillations
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.5)
        self.decay_rates = 0.1 + 0.4 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with oscillating frequency
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(self.omega[0] * r) * np.exp(-self.decay_rates[0] * r**2)
        
        # Multi-dimensional oscillatory component
        oscillatory_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            oscillatory_sum += np.sin(self.omega[i] * xi) * np.cos(self.omega[i] * xi)
        
        # Cross-dimensional interaction with radial coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Angular component
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                cross_term += np.sin(3 * angle) * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Exponential decay with varying rates
        decay_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            decay_sum += np.exp(-self.decay_rates[i] * xi**2)
        
        # Combine all components
        return 0.5 * radial_term + 0.3 * oscillatory_sum + 0.2 * cross_term - 0.1 * decay_sum