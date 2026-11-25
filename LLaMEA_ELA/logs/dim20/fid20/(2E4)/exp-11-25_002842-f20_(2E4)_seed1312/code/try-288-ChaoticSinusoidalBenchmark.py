import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for each dimension
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        # Periodic attractor frequencies
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        # Amplitude modulation parameters with higher variation
        self.amp_modulation = np.random.uniform(1.0, 3.0, dim)
        # Phase shifts for each dimension
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Dynamic scaling factors
        self.scaling = np.random.uniform(0.8, 1.5, dim)
        # Cubic interaction terms for increased complexity
        self.cubic_coeffs = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.5 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.3 * np.sin(3 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Periodic attractor component
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Modified amplitude modulation with cubic term
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i]) + self.cubic_coeffs[i] * (x[i] ** 3)
            amp_modulation_energy += amp_mod ** 2
            
        # Local minima attraction
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Combine components with dynamic weights
        total = 0.3 * result + 0.3 * periodic_energy + 0.2 * amp_modulation_energy + 0.2 * minima_energy
        
        # Apply dynamic scaling with cubic interaction
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i]) + self.cubic_coeffs[i] * (x[i] ** 3)
            
        return total