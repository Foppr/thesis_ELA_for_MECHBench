import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map parameters for each dimension
        self.a_params = np.random.uniform(1.5, 2.0, dim)
        # Time-varying chaotic phase transitions for each dimension
        self.transition_times = np.random.uniform(0.1, 3.0, dim)
        # Hybrid trigonometric-polynomial coupling coefficients
        self.hybrid_coupling = np.random.uniform(-1.2, 1.2, (dim, dim))
        # Adaptive conditioning factors with dynamic scaling
        self.conditioning = np.random.uniform(0.3, 5.0, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 12, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.2, 4.0, dim)
        # Local optima positions for each dimension
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 7))
        # Time-varying parameter modulation
        self.modulation_freq = np.random.uniform(0.02, 2.0, dim)
        # Tent map specific parameters
        self.tent_shift = np.random.uniform(-0.2, 0.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic tent map oscillation with time-varying parameters
        for i in range(self.dim):
            a = self.a_params[i] * (1 + 0.3 * np.sin(self.modulation_freq[i] * x[i]))
            tent_val = a * np.min([x[i], 1 - x[i]])
            result += self.amp_scaling[i] * np.cos(tent_val) ** 2
            
        # Hybrid trigonometric-polynomial coupling between dimensions
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    hybrid_energy += self.hybrid_coupling[i, j] * np.cos(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with dynamic scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning[i] * (1 + 0.4 * np.sin(x[i]))
            conditioning_energy += cond_factor * (x[i] ** 4) * np.cos(x[i])
            
        # Local optima attraction with dynamic distance metrics
        local_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.local_optima[i, :])
            min_dist = np.min(distances)
            local_energy += min_dist ** 3
            
        # Combine components with weighted sum
        total = 0.25 * result + 0.4 * hybrid_energy + 0.2 * conditioning_energy + 0.15 * local_energy
        
        return total