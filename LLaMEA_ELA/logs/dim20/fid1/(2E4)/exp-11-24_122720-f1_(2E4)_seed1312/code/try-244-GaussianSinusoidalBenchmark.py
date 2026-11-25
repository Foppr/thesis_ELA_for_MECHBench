import numpy as np

class GaussianSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for Gaussian components
        self.gaussian_centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.gaussian_weights = np.random.uniform(0.5, 2.0, 10)
        self.gaussian_widths = np.random.uniform(0.5, 2.5, 10)
        # Sinusoidal modulation parameters
        self.sin_amplitudes = np.random.uniform(0.5, 1.5, dim)
        self.sin_frequencies = np.random.uniform(1.0, 3.0, dim)
        # Asymmetric saddle point parameters
        self.saddle_centers = np.random.uniform(-4.0, 4.0, dim)
        self.saddle_strengths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components
        gaussian_sum = 0.0
        for i in range(10):
            center = self.gaussian_centers[i]
            diff = x - center
            exponent = -np.sum((diff**2) / (2 * self.gaussian_widths[i]**2))
            gaussian_sum += self.gaussian_weights[i] * np.exp(exponent)
        
        # Sinusoidal modulation
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x[i])
            
        # Asymmetric saddle points
        saddle_term = 0.0
        for i in range(self.dim):
            diff = x[i] - self.saddle_centers[i]
            if diff >= 0:
                saddle_term += self.saddle_strengths[i] * (diff**3)
            else:
                saddle_term += self.saddle_strengths[i] * (0.5 * diff**3)
        
        # Combine components with dimensionality scaling
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        result = scale_factor * (0.3 * gaussian_sum + 0.4 * sin_modulation + 0.3 * saddle_term)
        
        # Add small random noise
        noise = 0.005 * np.random.normal(0, 1)
        
        return result + noise + 0.1 * self.dim