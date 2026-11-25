import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for logistic map with higher variability
        self.logistic_params = np.random.uniform(3.5, 4.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Adaptive conditioning factors with increased variability
        self.conditioning = np.random.uniform(0.05, 4.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 6*np.pi, dim)
        # Polynomial degree for each dimension with higher values
        self.poly_degree = np.random.randint(4, 12, dim)
        # Amplitude scaling with greater variation
        self.amp_scaling = np.random.uniform(0.3, 4.0, dim)
        # Local minima positions with more diversity
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 12))
        # Additional interaction terms with chaotic behavior
        self.interaction_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Dynamic parameter transitions with higher frequency
        self.transition_params = np.random.uniform(0.05, 0.3, dim)
        # Chaos-induced frequency modulation
        self.frequency_modulation = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic logistic map oscillation with dynamic parameter transitions
        for i in range(self.dim):
            # Logistic map with dynamic parameter
            param = self.logistic_params[i] * (1 + 0.4 * np.sin(x[i] * self.frequency_modulation[i]))
            logistic_value = param * x[i] * (1 - x[i])
            chaotic_term = np.log(1 + np.abs(logistic_value))
            result += self.amp_scaling[i] * np.cos(chaotic_term + self.phase_shifts[i]) ** 4
            
        # Trigonometric-polynomial coupling between dimensions
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.cos(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 5) * np.cos(x[i])
            
        # Local minima attraction with multiple candidates
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 4
            
        # Additional interaction terms between dimensions with chaotic coupling
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.sin(x[i] * x[j])
                
        # Combine components with weighted sum and chaotic weighting
        total = 0.30 * result + 0.25 * trig_poly_coupling_energy + 0.20 * conditioning_energy + 0.15 * local_energy + 0.10 * interaction_energy
        
        return total