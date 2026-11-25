import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential decay and sinusoidal components
        self.exponential_rates = np.random.uniform(0.1, 2.0, size=dim)
        self.sinusoidal_frequencies = np.random.uniform(1.0, 10.0, size=dim)
        self.amplitudes = np.random.uniform(1.0, 5.0, size=dim)
        # Radial symmetry parameters
        self.radial_centers = np.random.uniform(-2.0, 2.0, size=dim)
        self.radial_weights = np.random.uniform(0.5, 2.0, size=dim)
        # Cross-dimensional interaction weights
        self.interaction_matrix = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with adaptive rates
        exponential_decay = 0.0
        for i in range(self.dim):
            exponential_decay += self.amplitudes[i] * np.exp(-self.exponential_rates[i] * np.abs(x[i])) * np.sin(self.sinusoidal_frequencies[i] * x[i])
            
        # Radial symmetry component with weighted distances
        radial_component = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i] - self.radial_centers[i])
            radial_component += self.radial_weights[i] * np.exp(-0.5 * (distance / self.conditioning_factors[i])**2)
            
        # Cross-dimensional interaction with adaptive coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_matrix[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Sinusoidal oscillation with varying frequencies and amplitudes
        sinusoidal_oscillation = 0.0
        for i in range(self.dim):
            sinusoidal_oscillation += self.amplitudes[i] * np.sin(self.sinusoidal_frequencies[i] * x[i]) * np.cos(self.sinusoidal_frequencies[i] * x[i])
            
        # Adaptive conditioning component with exponential scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += self.conditioning_factors[i] * np.exp(-0.1 * x[i]**2) * np.sin(2 * x[i])
            
        # Combined landscape with tunable weights optimized for ruggedness and structure
        return (1.3 * exponential_decay + 
                1.1 * radial_component + 
                1.4 * interaction + 
                1.2 * sinusoidal_oscillation + 
                0.9 * conditioning)