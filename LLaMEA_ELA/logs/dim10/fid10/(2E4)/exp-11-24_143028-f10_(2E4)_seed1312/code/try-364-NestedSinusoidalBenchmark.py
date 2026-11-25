import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize nested sinusoidal parameters
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        self.decay_rates = np.random.uniform(0.1, 0.8, dim)
        # Cross-dimensional coupling parameters
        self.coupling_strength = np.random.uniform(0.1, 0.5, dim)
        self.coupling_exponents = np.random.uniform(0.5, 2.0, dim)
        # Adaptive frequency modulation
        self.modulation_freq = np.random.uniform(0.5, 3.0, dim)
        self.modulation_amp = np.random.uniform(0.1, 0.5, dim)
        # Local minima distribution
        self.minima_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.minima_widths = np.random.uniform(0.5, 2.0, 5)

    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1]
        normalized_x = x / 5.0
        
        # Compute nested sinusoidal components
        nested_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Base sinusoidal term with decay
            base_term = self.amplitudes[i] * np.sin(self.frequencies[i] * normalized_x[i] + self.phases[i]) * np.exp(-self.decay_rates[i] * np.abs(normalized_x[i]))
            
            # Adaptive frequency modulation
            modulation = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * normalized_x[i])
            modulated_freq = self.frequencies[i] * (1.0 + modulation)
            
            # Add modulated sinusoidal term
            modulated_term = self.amplitudes[i] * np.sin(modulated_freq * normalized_x[i] + self.phases[i]) * np.exp(-self.decay_rates[i] * np.abs(normalized_x[i]))
            
            # Cross-dimensional coupling
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.abs(normalized_x[i] - normalized_x[j]) ** self.coupling_exponents[i]
                    coupling_term += self.coupling_strength[i] * coupling_factor
            
            nested_sum[i] = base_term + modulated_term + coupling_term
        
        # Multi-local minima landscape
        minima_energy = 0.0
        for k in range(5):
            # Compute distance to each minimum center
            dist = np.sum((normalized_x[:, None] - self.minima_centers[:, k]) ** 2, axis=0)
            # Apply Gaussian-like attraction to local minima
            minima_energy += np.exp(-dist / (2 * self.minima_widths[k] ** 2))
        
        # Combine components with nonlinearity
        fitness = np.sum(nested_sum ** 2) + 0.3 * minima_energy
        
        # Add conditioning effects based on dimensionality
        condition_factor = np.sum(np.abs(normalized_x) ** (1.2 + np.random.rand() * 1.8)) / self.dim
        fitness += 0.2 * condition_factor
        
        # Add noise for complexity
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise