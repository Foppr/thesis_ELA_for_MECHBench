import numpy as np

class SinusoidalModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Frequency modulation parameters for each dimension
        self.freq_mod = np.random.uniform(1.0, 6.0, dim)
        # Polynomial coupling coefficients between dimensions
        self.poly_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Adaptive conditioning factors
        self.conditioning = np.random.uniform(0.3, 2.5, dim)
        # Phase shifts for sinusoidal components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 7, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.3, 2.5, dim)
        # Local minima positions for each dimension
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Additional interaction terms
        self.interaction_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation with frequency modulation
        for i in range(self.dim):
            freq = self.freq_mod[i] * (1 + 0.6 * np.sin(x[i]))
            result += self.amp_scaling[i] * np.sin(freq * x[i] + self.phase_shifts[i]) ** 2
            
        # Polynomial coupling between dimensions
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with enhanced nonlinearity
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 3) * np.cos(x[i])
            
        # Local minima attraction
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 2
            
        # Additional interaction terms between dimensions
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Combine components with weighted sum
        total = 0.35 * result + 0.25 * poly_coupling_energy + 0.2 * conditioning_energy + 0.15 * local_energy + 0.05 * interaction_energy
        
        return total