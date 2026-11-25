import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute centers for radial basis functions
        self.centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.amplitudes = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            amplitude = self.amplitudes[i]
            distance = np.sum((x_norm - center)**2)
            rbf_sum += amplitude * np.exp(-distance / (2 * 0.5**2))
        
        # Quadratic basin term to guide optimization towards origin
        quadratic_term = 0.1 * np.sum(x_norm**2)
        
        # Add sinusoidal modulation to create additional complexity
        sinusoidal_modulation = np.sin(3 * np.pi * np.sum(x_norm**2))
        
        # Combine all terms
        result = rbf_sum + quadratic_term * (1 + 0.5 * sinusoidal_modulation)
        
        return result