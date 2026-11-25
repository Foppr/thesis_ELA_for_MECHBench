import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 3.9 * np.pi * (1 + np.arange(dim) * 0.5)
        self.decay_rates = 0.40 + 0.15 * np.sin(np.arange(dim) * np.pi / (dim + 3))
        # Add chaotic logistic map parameter
        self.r = 3.9 + 0.12 * np.sin(np.arange(dim) * np.pi / (dim + 4))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial radial component with chaotic frequency modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = (np.sin(self.omega[0] * r) + 0.3 * np.cos(2 * self.omega[0] * r)) * np.exp(-self.decay_rates[0] * r**2.5)
        
        # Multi-dimensional chaotic oscillatory component
        oscillatory_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add logistic map modulation to each dimension
            logistic_mod = 1.0 / (1.0 + np.exp(-self.r[i] * (xi - 0.3)))
            oscillatory_sum += np.sin(self.omega[i] * xi) * np.cos(2 * self.omega[i] * xi) * logistic_mod
        
        # Enhanced cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Angular component with chaotic modulation
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                chaotic_factor = np.sin(self.r[i] * angle) * np.cos(self.r[j] * angle)
                cross_term += chaotic_factor * np.exp(-0.40 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Adaptive polynomial decay with fractal-like behavior
        decay_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add fractal-like scaling to decay rates
            fractal_scale = np.sin(xi * np.pi) ** 3 + 0.35
            decay_sum += np.exp(-self.decay_rates[i] * xi**3 * fractal_scale)
        
        # Add a chaotic noise component for additional complexity
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += np.sin(6 * x_scaled[i]) * np.cos(7 * x_scaled[i])
        
        # Combine all components with modified weights
        return 0.32 * radial_term + 0.30 * oscillatory_sum + 0.20 * cross_term - 0.15 * decay_sum - 0.08 * noise_component