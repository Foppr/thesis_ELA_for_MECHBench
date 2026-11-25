import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for each dimension
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        # Periodic attractor frequencies
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        # Modified amplitude modulation parameters
        self.amp_modulation = np.random.uniform(1.0, 3.0, dim)
        # Phase shifts for each dimension
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Dynamic scaling factors
        self.scaling = np.random.uniform(0.8, 1.5, dim)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, dim)
        # Cross-dimension interaction coefficients
        self.interactions = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Cubic nonlinearity factors
        self.cubic_factors = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component with fractional Brownian motion
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.5 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.3 * np.sin(3 * self.chaotic_params[i] * x[i])
            
            # Add fractional Brownian motion component for roughness
            fbm = np.random.normal(0, 1) * (np.abs(x[i]) ** self.hurst[i])
            chaotic_term += fbm
            
            # Add cubic nonlinearity
            chaotic_term += self.cubic_factors[i] * (x[i] ** 3)
            
            result += chaotic_term ** 2
            
        # Periodic attractor component
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Amplitude modulation
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i])
            amp_modulation_energy += amp_mod ** 2
            
        # Local minima attraction
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Combine components with dynamic weights
        total = 0.25 * result + 0.25 * periodic_energy + 0.2 * amp_modulation_energy + 0.3 * minima_energy
        
        # Apply dynamic scaling and add memory-dependent energy terms
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i])
            # Memory term: previous x value influence
            if i > 0:
                total += 0.1 * np.sin(x[i-1]) * np.cos(x[i])
            
        # Add cross-dimension interactions
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    total += self.interactions[i, j] * x[i] * x[j]
                    
        return total