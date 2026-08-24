import numpy as np

class MultimodalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for consistent scaling
        x_normalized = x / 5.0
        
        # Radial component with varying frequency
        r = np.sqrt(np.sum(x_normalized**2))
        radial = np.sin(5 * r) * np.exp(-0.5 * r**2)
        
        # Angular component with multiple interference patterns
        angular = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle_diff = np.arctan2(x_normalized[j], x_normalized[i])
                angular += np.sin(3 * angle_diff + i * 0.5) * np.cos(2 * angle_diff + j * 0.3)
        
        # Sinusoidal interference pattern in each dimension
        interference = 0
        for i in range(self.dim):
            interference += np.sin(2 * np.pi * x_normalized[i] + i * 0.7) * np.cos(1.5 * np.pi * x_normalized[i] + i * 0.4)
        
        # Variable conditioning through dimension-specific scaling
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.sin(i * 0.3)
            conditioning += condition_factor * x_normalized[i]**2
        
        # Add a global minimum at origin with additional noise
        result = 0.5 * radial + 0.3 * angular + 0.2 * interference + 0.1 * conditioning
        
        # Introduce local minima using a sum of Gaussian-like functions
        local_minima = 0
        for i in range(10):  # 10 local minima
            center = np.random.uniform(-1, 1, self.dim)
            sigma = 0.2 + 0.1 * np.random.random()
            exponent = -0.5 * np.sum(((x_normalized - center) / sigma)**2)
            local_minima += np.exp(exponent)
        
        result += 0.1 * local_minima
        
        # Add small random perturbation for increased complexity
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 9))
        result += perturbation
        
        return result