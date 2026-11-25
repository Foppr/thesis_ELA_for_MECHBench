import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute periodic parameters for each dimension
        self.freqs = 2.0 + 3.0 * np.random.rand(dim)
        self.amps = 1.0 + 2.0 * np.random.rand(dim)
        self.phase_shifts = np.pi * np.random.rand(dim)
        self.radial_coeffs = 0.5 + 1.5 * np.random.rand(dim)
        self.cross_coupling = 0.3 + 0.7 * np.random.rand(dim, dim)
        # Set some coupling weights to zero to create sparse interactions
        mask = np.random.rand(dim, dim) > 0.7
        self.cross_coupling[mask] = 0.0
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial term with varying coefficients
        radial_dist = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * np.sum(self.radial_coeffs * x**2) + 0.1 * radial_dist**3
        
        # Periodic sinusoidal terms
        periodic_term = 0.0
        for i in range(self.dim):
            # Sinusoidal component with frequency, amplitude, and phase
            periodic_term += self.amps[i] * np.sin(self.freqs[i] * x[i] + self.phase_shifts[i])**2
            
        # Cross-dimensional coupling terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.cross_coupling[i, j] * np.sin(x[i] - x[j])**2
        
        # Add a global periodic modulation
        global_mod = np.sin(0.5 * radial_dist)
        
        # Combine all terms with different weights
        return 0.8 * radial_term + 1.2 * periodic_term + 0.6 * coupling_term + 0.3 * global_mod