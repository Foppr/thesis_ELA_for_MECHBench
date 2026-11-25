import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map parameters for each dimension
        self.mu_params = np.random.uniform(1.5, 2.0, dim)
        # Chaotic phase transitions for each dimension
        self.transition_probs = np.random.uniform(0.05, 0.95, dim)
        # Trigonometric-polynomial coupling coefficients
        self.trig_poly_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Adaptive conditioning factors with dynamic scaling
        self.conditioning = np.random.uniform(0.2, 4.0, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(3, 10, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.3, 3.0, dim)
        # Local optima positions for each dimension
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 9))
        # Dynamic parameter modulation
        self.modulation_freq = np.random.uniform(0.2, 1.5, dim)
        # Nonlinearity exponents for tent map
        self.nonlin_exponent = np.random.uniform(1.2, 3.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic tent map oscillation with dynamic parameter transitions
        for i in range(self.dim):
            mu = self.mu_params[i] * (1 + 0.4 * np.cos(self.modulation_freq[i] * x[i]))
            tent_val = mu * np.abs(x[i]) if x[i] < 0.5 else mu * (1 - np.abs(x[i]))
            result += self.amp_scaling[i] * np.tan(tent_val) ** 2
            
        # Trigonometric-polynomial coupling between dimensions
        trig_poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_energy += self.trig_poly_coupling[i, j] * np.cos(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with dynamic scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning[i] * (1 + 0.3 * np.sin(x[i]))
            conditioning_energy += cond_factor * (x[i] ** self.nonlin_exponent[i]) * np.cos(x[i])
            
        # Local optima attraction with dynamic distance metrics
        local_energy = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.local_optima[i, :])
            min_dist = np.min(distances)
            local_energy += min_dist ** 3
            
        # Combine components with weighted sum
        total = 0.3 * result + 0.35 * trig_poly_energy + 0.25 * conditioning_energy + 0.15 * local_energy
        
        return total