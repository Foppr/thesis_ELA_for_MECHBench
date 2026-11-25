import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 3.0 * np.pi * (1 + np.arange(dim) * 0.7)
        self.decay_rates = 0.2 + 0.6 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        # Add chaotic logistic map parameter
        self.r = 3.9 + 0.1 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with chaotic frequency modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(self.omega[0] * r) * np.exp(-self.decay_rates[0] * r**3)
        
        # Multi-dimensional chaotic oscillatory component
        oscillatory_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add logistic map modulation to each dimension
            logistic_mod = 1.0 / (1.0 + np.exp(-self.r[i] * (xi - 0.5)))
            oscillatory_sum += np.sin(self.omega[i] * xi) * np.cos(self.omega[i] * xi) * logistic_mod
        
        # Enhanced cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Angular component with chaotic modulation
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                chaotic_factor = np.sin(self.r[i] * angle) * np.cos(self.r[j] * angle)
                cross_term += chaotic_factor * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Adaptive exponential decay with fractal-like behavior
        decay_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add fractal-like scaling to decay rates
            fractal_scale = np.sin(xi * np.pi) ** 2 + 0.5
            decay_sum += np.exp(-self.decay_rates[i] * xi**2 * fractal_scale)
        
        # Add a chaotic noise component for additional complexity
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += np.sin(10 * x_scaled[i]) * np.cos(7 * x_scaled[i])
        
        # Combine all components with modified weights
        return 0.4 * radial_term + 0.3 * oscillatory_sum + 0.2 * cross_term - 0.15 * decay_sum - 0.05 * noise_component