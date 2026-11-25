import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for sinusoidal components
        self.freqs = np.random.uniform(1.0, 6.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Radial structure with multiple peaks
        self.radial_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.radial_weights = np.random.dirichlet(np.ones(3), dim).T
        
        # Cross-dimensional coupling matrix
        self.coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling, 0.0)
        
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
        # Add noise parameters
        self.noise_level = np.random.uniform(0.01, 0.2, dim)
        
    def f(self, x):
        # Ensure bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1]
        norm_x = x / 5.0
        
        # Compute sinusoidal components
        sin_components = np.zeros(self.dim)
        for i in range(self.dim):
            sin_components[i] = self.amps[i] * np.sin(self.freqs[i] * norm_x[i] + self.phases[i])
        
        # Radial multimodal structure
        radial_values = np.zeros(self.dim)
        for i in range(self.dim):
            radial_sum = 0.0
            for j in range(3):
                dist = np.abs(norm_x[i] - self.radial_centers[i, j])
                radial_sum += self.radial_weights[j, i] * np.exp(-dist**2 / 0.1)
            radial_values[i] = radial_sum
        
        # Combine components with adaptive conditioning
        fitness = 0.0
        for i in range(self.dim):
            component = sin_components[i] + radial_values[i]
            fitness += self.conditioning_factors[i] * (component**2 + 0.3 * component**3)
        
        # Add coupling terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling[i, j] * sin_components[i] * sin_components[j]
        
        # Add radial interaction
        r = np.sqrt(np.sum(norm_x**2))
        radial_interaction = np.sum([np.sin(2 * r + i) for i in range(self.dim)])
        
        # Final fitness with noise and scaling
        return fitness + 0.5 * coupling_term + 0.1 * radial_interaction + np.sum(self.noise_level * np.random.randn(self.dim))