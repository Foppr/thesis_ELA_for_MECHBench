import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 3.0 * np.pi * (1 + np.arange(dim) * 0.7)
        self.decay_rates = 0.2 + 0.6 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        # Add chaotic logistic map parameter for dynamic behavior
        self.chaos_params = 3.8 + 0.3 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced radial component with chaotic frequency modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(self.omega[0] * r * (1 + 0.3 * np.sin(r * 2))) * np.exp(-self.decay_rates[0] * r**2.5)
        
        # Multi-dimensional chaotic oscillatory component
        oscillatory_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add chaotic modulation to each dimension's oscillation
            chaotic_mod = 1 + 0.2 * np.sin(self.chaos_params[i] * xi)
            oscillatory_sum += np.sin(self.omega[i] * xi * chaotic_mod) * np.cos(self.omega[i] * xi * chaotic_mod)
        
        # Enhanced cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic angular component
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                chaotic_angle = angle * (1 + 0.25 * np.sin(self.chaos_params[i] * angle))
                cross_term += np.sin(4 * chaotic_angle) * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Adaptive exponential decay with chaotic rates
        decay_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply chaotic modulation to decay rate
            adaptive_decay = self.decay_rates[i] * (1 + 0.15 * np.sin(self.chaos_params[i] * xi))
            decay_sum += np.exp(-adaptive_decay * xi**2.2)
        
        # Add a chaotic polynomial term for additional complexity
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_term += xi**4 * np.sin(5 * xi) * np.cos(2 * xi)
        
        # Combine all components with dynamic weights
        return 0.4 * radial_term + 0.25 * oscillatory_sum + 0.2 * cross_term - 0.15 * decay_sum + 0.05 * poly_term