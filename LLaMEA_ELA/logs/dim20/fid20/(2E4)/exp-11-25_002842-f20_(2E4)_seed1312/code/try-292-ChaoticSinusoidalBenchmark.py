import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher variability
        self.chaotic_params = np.random.uniform(1.0, 4.0, dim)
        # Multi-frequency periodic components
        self.freqs = np.random.uniform(0.5, 8.0, dim)
        self.harmonics = np.random.randint(2, 6, dim)
        # Dynamic amplitude modulation with varying strength
        self.amp_modulation = np.random.uniform(1.0, 3.0, dim)
        # Phase shifts with higher randomness
        self.phases = np.random.uniform(0, 4*np.pi, dim)
        # Multiple local minima per dimension
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 8))
        # Dynamic scaling factors with larger variation
        self.scaling = np.random.uniform(0.5, 2.0, dim)
        # Fractional Brownian motion parameters with extreme Hurst values
        self.hurst = np.random.uniform(0.05, 0.95, dim)
        # Cross-dimensional interaction terms
        self.cross_interaction = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Memory effect coefficients
        self.memory_coeff = np.random.uniform(0.05, 0.3, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced chaotic sinusoidal component with multiple harmonics
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            for h in range(2, self.harmonics[i] + 1):
                chaotic_term += (1.0/h) * np.sin(h * self.chaotic_params[i] * x[i])
            
            # Add fractional Brownian motion component
            fbm = np.random.normal(0, 1) * (np.abs(x[i]) ** self.hurst[i])
            chaotic_term += fbm
            
            result += chaotic_term ** 2
            
        # Multi-frequency periodic attractor component
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            for h in range(2, 4):
                freq_term += (1.0/h) * np.sin(h * self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Enhanced amplitude modulation
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i])
            amp_modulation_energy += amp_mod ** 3  # Cubic modulation for stronger effect
            
        # Multi-minima attraction with weighted distances
        minima_energy = 0.0
        for i in range(self.dim):
            dists = np.abs(x[i] - self.minima_positions[i, :])
            min_dist = np.min(dists)
            # Weighted sum of multiple distances
            weights = np.exp(-dists / (np.std(dists) + 1e-8))
            weighted_sum = np.sum(weights * dists)
            minima_energy += weighted_sum ** 2
            
        # Cross-dimensional interaction terms
        cross_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_energy += self.cross_interaction[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Memory-dependent energy terms with stronger influence
        memory_energy = 0.0
        for i in range(self.dim):
            memory_energy += self.memory_coeff[i] * np.sin(x[i]) * np.cos(x[i-1] if i > 0 else x[-1])
            
        # Combine all components with new weights
        total = 0.25 * result + 0.25 * periodic_energy + 0.2 * amp_modulation_energy + 0.2 * minima_energy + 0.1 * cross_energy + 0.05 * memory_energy
        
        # Add strong conditioning through exponential scaling
        for i in range(self.dim):
            total += self.scaling[i] * np.exp(0.1 * np.abs(x[i])) * np.sin(x[i])
            
        return total