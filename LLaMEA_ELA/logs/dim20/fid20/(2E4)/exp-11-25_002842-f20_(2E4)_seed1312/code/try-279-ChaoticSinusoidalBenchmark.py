import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for each dimension
        self.chaotic_params = np.random.uniform(0.8, 2.5, dim)
        # Periodic attractor frequencies
        self.freqs = np.random.uniform(1.5, 6.0, dim)
        # Amplitude modulation parameters with enhanced variability
        self.amp_modulation = np.random.uniform(1.0, 3.0, dim)
        # Phase shifts for each dimension
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 7))
        # Dynamic scaling factors
        self.scaling = np.random.uniform(0.9, 1.8, dim)
        # Cross-dimensional coupling strength
        self.coupling_strength = np.random.uniform(0.1, 0.5, (dim, dim))
        # Resonance peak parameters
        self.resonance_centers = np.random.uniform(-5.0, 5.0, dim)
        self.resonance_widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced chaotic sinusoidal component with multiple harmonics
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.6 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.3 * np.sin(3 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.1 * np.sin(5 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Periodic attractor component with enhanced complexity
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.4 * np.cos(1.5 * self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Enhanced amplitude modulation with dynamic coupling
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            # Dynamic amplitude modulation based on neighboring dimensions
            modulation_factor = 1.0
            for j in range(self.dim):
                if i != j:
                    modulation_factor += self.coupling_strength[i, j] * np.sin(x[j])
            amp_mod = 1.0 + self.amp_modulation[i] * modulation_factor * np.sin(x[i])
            amp_modulation_energy += amp_mod ** 2
            
        # Local minima attraction with multiple peaks
        minima_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.minima_positions[i, :])
            min_dist = np.min(distances)
            minima_energy += min_dist ** 2
            
        # Resonance peak component to increase optimization difficulty
        resonance_energy = 0.0
        for i in range(self.dim):
            peak_value = np.exp(-0.5 * ((x[i] - self.resonance_centers[i]) / self.resonance_widths[i]) ** 2)
            resonance_energy += peak_value
            
        # Combine components with dynamic weights
        total = 0.25 * result + 0.25 * periodic_energy + 0.2 * amp_modulation_energy + 0.2 * minima_energy + 0.1 * resonance_energy
        
        # Apply dynamic scaling and cross-dimensional effects
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i])
            # Add cross-dimensional coupling effects
            for j in range(self.dim):
                if i != j:
                    total += 0.05 * self.coupling_strength[i, j] * np.sin(x[i]) * np.sin(x[j])
            
        return total