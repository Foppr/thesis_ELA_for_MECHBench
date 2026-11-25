import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for radial oscillations with improved conditioning
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.3)
        self.decay_rates = 0.05 + 0.6 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with oscillating frequency and enhanced decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(self.omega[0] * r) * np.exp(-self.decay_rates[0] * r**3)
        
        # Multi-dimensional oscillatory component with modified interaction
        oscillatory_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            oscillatory_sum += np.sin(self.omega[i] * xi) * np.cos(self.omega[i] * xi) * (1 + 0.1 * np.sin(xi))
        
        # Enhanced cross-dimensional interaction with angular and radial coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Angular component with frequency modulation
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                cross_term += np.sin(4 * angle) * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2)) * (1 + 0.05 * r)
        
        # Exponential decay with varying rates and additional sinusoidal modulation
        decay_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            decay_sum += np.exp(-self.decay_rates[i] * xi**2) * (1 + 0.2 * np.cos(xi))
        
        # Additional high-frequency oscillation component for increased multimodality
        high_freq_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            high_freq_term += np.sin(10 * xi) * np.cos(5 * xi)
        
        # Combine all components with adjusted weights
        return 0.4 * radial_term + 0.25 * oscillatory_sum + 0.2 * cross_term - 0.15 * decay_sum + 0.05 * high_freq_term