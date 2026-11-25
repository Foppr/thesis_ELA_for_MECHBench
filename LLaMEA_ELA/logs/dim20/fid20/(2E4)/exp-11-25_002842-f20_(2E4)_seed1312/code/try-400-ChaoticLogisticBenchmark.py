import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map parameters for each dimension
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        # Time-varying chaotic phase transitions for each dimension
        self.transition_times = np.random.uniform(0.1, 2.0, dim)
        # Hybrid trigonometric-polynomial coupling coefficients (modified)
        self.hybrid_coupling = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Adaptive conditioning factors with dynamic scaling
        self.conditioning = np.random.uniform(0.5, 4.0, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(3, 10, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.3, 3.0, dim)
        # Local optima positions for each dimension
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 9))
        # Time-varying parameter modulation
        self.modulation_freq = np.random.uniform(0.05, 1.5, dim)
        # Logistic map specific parameters
        self.logistic_shift = np.random.uniform(-0.3, 0.3, dim)
        # Additional cubic nonlinearities for increased complexity
        self.cubic_coeff = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic logistic map oscillation with time-varying parameters
        for i in range(self.dim):
            r = self.r_params[i] * (1 + 0.4 * np.sin(self.modulation_freq[i] * x[i]))
            logistic_val = r * x[i] * (1 - x[i])
            result += self.amp_scaling[i] * np.sin(logistic_val) ** 2
            
        # Hybrid trigonometric-polynomial coupling between dimensions
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    hybrid_energy += self.hybrid_coupling[i, j] * np.sin(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with dynamic scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning[i] * (1 + 0.3 * np.cos(x[i]))
            conditioning_energy += cond_factor * (x[i] ** 5) * np.sin(x[i])
            
        # Local optima attraction with dynamic distance metrics
        local_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.local_optima[i, :])
            min_dist = np.min(distances)
            local_energy += min_dist ** 4
            
        # Add cubic nonlinearities to increase complexity
        cubic_energy = 0.0
        for i in range(self.dim):
            cubic_energy += self.cubic_coeff[i] * (x[i] ** 3)
            
        # Combine components with weighted sum
        total = 0.25 * result + 0.30 * hybrid_energy + 0.20 * conditioning_energy + 0.15 * local_energy + 0.10 * cubic_energy
        
        return total