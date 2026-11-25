import numpy as np

class SinusoidalModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaos-based frequency modulation using logistic map
        self.freq_mod = np.random.uniform(3.5, 4.0, dim)
        # Higher-order polynomial coupling coefficients between dimensions
        self.poly_coupling = np.random.uniform(-2.0, 2.0, (dim, dim, dim))
        # Adaptive conditioning factors with chaotic scaling
        self.conditioning = np.random.uniform(0.1, 3.0, dim)
        # Phase shifts for sinusoidal components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension (higher order)
        self.poly_degree = np.random.randint(3, 8, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.1, 3.0, dim)
        # Local minima positions for each dimension
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 7))
        # Chaotic parameter for logistic map to generate dynamic modulation
        self.chaotic_param = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation with chaotic frequency modulation
        for i in range(self.dim):
            # Dynamic frequency modulation using logistic map
            freq = self.freq_mod[i] * (1 + 0.3 * np.sin(x[i]) * np.cos(self.chaotic_param[i] * x[i]))
            result += self.amp_scaling[i] * np.sin(freq * x[i] + self.phase_shifts[i]) ** 3
            
        # Higher-order polynomial coupling between dimensions
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        poly_coupling_energy += self.poly_coupling[i, j, k] * (x[i] ** self.poly_degree[i]) * x[j] * x[k]
                    
        # Adaptive conditioning with chaotic scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 3) * np.sin(x[i])
            
        # Local minima attraction with multiple local optima
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 3
            
        # Combine components with weighted sum
        total = 0.3 * result + 0.4 * poly_coupling_energy + 0.2 * conditioning_energy + 0.1 * local_energy
        
        return total