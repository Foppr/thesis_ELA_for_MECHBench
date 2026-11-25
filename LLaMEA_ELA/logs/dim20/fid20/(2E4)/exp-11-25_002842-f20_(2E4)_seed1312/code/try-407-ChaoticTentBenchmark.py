import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for logistic map with enhanced variability
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Adaptive conditioning factors with higher variability and nonlinearity
        self.conditioning = np.random.uniform(0.5, 4.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension with higher values and randomness
        self.poly_degree = np.random.randint(2, 12, dim)
        # Amplitude scaling with greater variation and chaotic modulation
        self.amp_scaling = np.random.uniform(0.3, 4.0, dim)
        # Local minima positions with more diversity and clustering
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 10))
        # Additional interaction terms with chaotic behavior and coupling strength
        self.interaction_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Dynamic parameter transitions with more complex modulation
        self.transition_params = np.random.uniform(0.02, 0.15, dim)
        # Chaos modulation factors for enhanced landscape complexity
        self.chaos_modulation = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic logistic map oscillation with dynamic parameter transitions
        for i in range(self.dim):
            # Logistic map with dynamic parameter and chaos modulation
            param = self.logistic_params[i] * (1 + 0.2 * np.sin(x[i]))
            logistic_value = param * x[i] * (1 - x[i])
            chaotic_term = self.chaos_modulation[i] * logistic_value
            result += self.amp_scaling[i] * np.cos(chaotic_term + self.phase_shifts[i]) ** 2
            
        # Trigonometric-polynomial coupling between dimensions with enhanced nonlinearity
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.cos(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 3) * np.cos(x[i])
            
        # Local minima attraction with multiple candidates and variable influence
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 2.5
            
        # Additional interaction terms between dimensions with chaotic coupling
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j]) * (x[i] + x[j])
                
        # Combine components with weighted sum and chaotic weighting
        total = 0.30 * result + 0.25 * trig_poly_coupling_energy + 0.20 * conditioning_energy + 0.15 * local_energy + 0.10 * interaction_energy
        
        return total