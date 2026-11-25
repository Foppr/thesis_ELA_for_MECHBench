import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize condition numbers and saddle point locations
        self.condition_numbers = np.random.uniform(1.0, 100.0, dim)
        self.saddle_points = np.random.uniform(-3.0, 3.0, (dim, dim))
        self.noise_amplitude = 0.05 + 0.05 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with variable conditioning
        quadratic_term = 0.0
        for i in range(self.dim):
            quadratic_term += self.condition_numbers[i] * (x_norm[i] ** 2)
        
        # Saddle point interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                distance = (x_norm[i] - self.saddle_points[i, j]) ** 2
                saddle_term += np.exp(-distance / (2.0 * (0.5 + 0.5 * np.sin(i + j))))
        
        # Adaptive noise modulation based on position
        noise_modulation = np.sum(np.sin(x_norm) * np.cos(x_norm))
        adaptive_noise = self.noise_amplitude * noise_modulation * np.random.normal(0, 1)
        
        # Multi-scale sinusoidal modulations to create complex landscape
        modulation_term = 0.0
        for i in range(self.dim):
            modulation_term += (1.0 + 0.3 * np.sin(2 * np.pi * x_norm[i])) * \
                              np.cos(3 * np.pi * x_norm[i]) * \
                              np.exp(-0.1 * np.abs(x_norm[i]))
        
        # Combined fitness function
        combined = quadratic_term + saddle_term + modulation_term + adaptive_noise
        
        return combined