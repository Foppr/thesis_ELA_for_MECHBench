import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute periodic parameters for each dimension
        self.freqs = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.8)
        self.amps = 1.0 + 0.5 * np.cos(np.arange(dim) * 0.6)
        self.phase_shifts = np.pi * np.random.rand(dim)
        # Radial conditioning parameters
        self.radial_scale = 1.0 + 0.3 * np.sin(np.arange(dim) * 0.4)
        self.radial_power = 2.0 + 0.8 * np.cos(np.arange(dim) * 0.5)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial term with adaptive scaling and power
        radial_dist = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * np.sum(self.radial_scale * (radial_dist**self.radial_power))
        
        # Periodic sinusoidal components
        periodic_term = 0.0
        for i in range(self.dim):
            # Sinusoidal function with adaptive frequency, amplitude, and phase
            periodic_component = self.amps[i] * np.sin(self.freqs[i] * x[i] + self.phase_shifts[i])
            # Add coupling between dimensions with varying strength
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 0.3 + 0.2 * np.sin(i * 0.3 + j * 0.25 + x[i] * 0.1)
                    coupling += coupling_strength * np.cos(x[i] - x[j])
            periodic_term += (periodic_component + coupling)**2
        
        # Adaptive conditioning term with dimension-wise scaling
        cond_term = 0.0
        for i in range(self.dim):
            # Variable conditioning based on position and precomputed parameters
            cond_factor = 1.0 + 0.5 * np.sin(x[i] * 0.4 + i * 0.3)
            cond_term += cond_factor * (x[i]**2) / (1.0 + np.abs(x[i]))
        
        # Multi-modal structure with nested optima
        modal_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima using cosine functions
            local_minima = 3.0 * np.cos(2.0 * x[i] + i * 0.5)
            modal_term += local_minima**2
        
        # Combined function with weighted components
        return 0.7 * radial_term + 1.2 * periodic_term + 0.8 * cond_term + 0.6 * modal_term