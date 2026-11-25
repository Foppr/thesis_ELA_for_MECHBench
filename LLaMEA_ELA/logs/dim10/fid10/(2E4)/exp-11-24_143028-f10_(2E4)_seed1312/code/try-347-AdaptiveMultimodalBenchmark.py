import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for sinusoidal components
        self.freqs = np.random.uniform(1.5, 7.0, dim)
        self.amps = np.random.uniform(0.8, 2.5, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Radial structure with multiple peaks
        self.radial_centers = np.random.uniform(-4.0, 4.0, (dim, 4))
        self.radial_weights = np.random.dirichlet(np.ones(4), dim).T
        
        # Cross-dimensional coupling matrix with stronger interactions
        self.coupling = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling, 0.0)
        
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.2, 15.0, dim)
        
        # Add noise parameters
        self.noise_level = np.random.uniform(0.02, 0.3, dim)
        
    def f(self, x):
        # Ensure bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1]
        norm_x = x / 5.0
        
        # Compute sinusoidal components
        sin_components = np.zeros(self.dim)
        for i in range(self.dim):
            sin_components[i] = self.amps[i] * np.sin(self.freqs[i] * norm_x[i] + self.phases[i])
        
        # Radial multimodal structure with more peaks
        radial_values = np.zeros(self.dim)
        for i in range(self.dim):
            radial_sum = 0.0
            for j in range(4):
                dist = np.abs(norm_x[i] - self.radial_centers[i, j])
                radial_sum += self.radial_weights[j, i] * np.exp(-dist**2 / 0.05)
            radial_values[i] = radial_sum
        
        # Combine components with adaptive conditioning and stronger nonlinearities
        fitness = 0.0
        for i in range(self.dim):
            component = sin_components[i] + radial_values[i]
            fitness += self.conditioning_factors[i] * (component**2 + 0.5 * component**3 + 0.1 * component**4)
        
        # Add coupling terms with increased strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling[i, j] * sin_components[i] * sin_components[j]
        
        # Add radial interaction with higher frequency
        r = np.sqrt(np.sum(norm_x**2))
        radial_interaction = np.sum([np.sin(3 * r + i) for i in range(self.dim)])
        
        # Final fitness with noise and scaling
        return fitness + 0.7 * coupling_term + 0.15 * radial_interaction + np.sum(self.noise_level * np.random.randn(self.dim))