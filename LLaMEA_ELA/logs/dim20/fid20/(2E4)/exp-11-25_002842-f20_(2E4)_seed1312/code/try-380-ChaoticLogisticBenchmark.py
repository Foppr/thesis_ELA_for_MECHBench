import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map parameters for each dimension
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        # Chaotic phase transitions for each dimension
        self.transition_probs = np.random.uniform(0.1, 0.9, dim)
        # Trigonometric-polynomial coupling coefficients
        self.trig_poly_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning factors with dynamic scaling
        self.conditioning = np.random.uniform(0.1, 3.0, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 8, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.5, 2.5, dim)
        # Local optima positions for each dimension
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 7))
        # Dynamic parameter modulation
        self.modulation_freq = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic logistic map oscillation with dynamic parameter transitions
        for i in range(self.dim):
            r = self.r_params[i] * (1 + 0.3 * np.sin(self.modulation_freq[i] * x[i]))
            logistic_val = r * x[i] * (1 - x[i])
            result += self.amp_scaling[i] * np.sin(logistic_val) ** 2
            
        # Trigonometric-polynomial coupling between dimensions
        trig_poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_energy += self.trig_poly_coupling[i, j] * np.sin(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with dynamic scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning[i] * (1 + 0.2 * np.cos(x[i]))
            conditioning_energy += cond_factor * (x[i] ** 3) * np.sin(x[i])
            
        # Local optima attraction with dynamic distance metrics
        local_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.local_optima[i, :])
            min_dist = np.min(distances)
            local_energy += min_dist ** 2
            
        # Combine components with weighted sum
        total = 0.35 * result + 0.3 * trig_poly_energy + 0.25 * conditioning_energy + 0.1 * local_energy
        
        return total