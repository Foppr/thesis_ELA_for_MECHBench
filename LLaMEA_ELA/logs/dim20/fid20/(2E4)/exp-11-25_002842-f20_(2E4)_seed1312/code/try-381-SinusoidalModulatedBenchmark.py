import numpy as np

class SinusoidalModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic frequency modulation using logistic map
        self.freq_mod = np.random.uniform(1.0, 5.0, dim)
        # Polynomial coupling coefficients between dimensions with memory effects
        self.poly_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Dynamic conditioning factors that depend on previous evaluations
        self.conditioning = np.random.uniform(0.5, 2.0, dim)
        # Phase shifts with memory dependence
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 6, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.5, 2.0, dim)
        # Local minima positions for each dimension
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Memory factors for phase shifts
        self.memory_factors = np.random.uniform(0.1, 0.9, dim)
        # Chaotic parameter for phase modulation
        self.chaotic_param = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal oscillation with memory effects
        for i in range(self.dim):
            # Dynamic phase shift based on chaotic map
            phase_shift = self.phase_shifts[i] + self.memory_factors[i] * np.sin(self.chaotic_param[i] * x[i])
            freq = self.freq_mod[i] * (1 + 0.5 * np.sin(x[i]))
            result += self.amp_scaling[i] * np.sin(freq * x[i] + phase_shift) ** 3
            
        # Higher-order polynomial coupling between dimensions
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Include cubic and quartic terms for complexity
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** self.poly_degree[i]) * (x[j] ** 2)
                    
        # Dynamic conditioning with oscillatory behavior
        conditioning_energy = 0.0
        for i in range(self.dim):
            # Add oscillatory conditioning factor
            cond_factor = self.conditioning[i] * (1 + 0.3 * np.sin(x[i]))
            conditioning_energy += cond_factor * (x[i] ** 2) * np.cos(x[i])
            
        # Local minima attraction with variable weights
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            # Add a nonlinear weighting to the distance
            local_energy += min_dist ** 3
            
        # Combine components with weighted sum
        total = 0.3 * result + 0.3 * poly_coupling_energy + 0.25 * conditioning_energy + 0.15 * local_energy
        
        return total