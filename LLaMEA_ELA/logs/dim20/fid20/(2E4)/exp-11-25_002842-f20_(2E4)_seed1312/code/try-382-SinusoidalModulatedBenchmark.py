import numpy as np

class SinusoidalModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Frequency modulation parameters for each dimension
        self.freq_mod = np.random.uniform(1.0, 5.0, dim)
        # Polynomial coupling coefficients between dimensions
        self.poly_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning factors
        self.conditioning = np.random.uniform(0.5, 2.0, dim)
        # Phase shifts for sinusoidal components with chaotic modification
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 6, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.5, 2.0, dim)
        # Local minima positions for each dimension
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Chaotic phase modulation factor
        self.chaotic_factor = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation with frequency modulation and chaotic phase shifts
        for i in range(self.dim):
            freq = self.freq_mod[i] * (1 + 0.5 * np.sin(x[i]))
            # Add chaotic modulation to phase shift
            chaotic_phase = self.phase_shifts[i] + self.chaotic_factor[i] * np.sin(x[i])
            result += self.amp_scaling[i] * np.sin(freq * x[i] + chaotic_phase) ** 2
            
        # Polynomial coupling between dimensions with higher-order interactions
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add cubic interaction term for increased complexity
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** self.poly_degree[i]) * (x[j] ** 2)
                    
        # Adaptive conditioning with additional nonlinear term
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 2) * np.cos(x[i]) + 0.1 * x[i] ** 4
            
        # Local minima attraction with distance weighting
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            # Add inverse distance weighting for more complex landscape
            local_energy += 1.0 / (min_dist + 0.1) ** 2
            
        # Combine components with weighted sum
        total = 0.35 * result + 0.3 * poly_coupling_energy + 0.25 * conditioning_energy + 0.1 * local_energy
        
        return total