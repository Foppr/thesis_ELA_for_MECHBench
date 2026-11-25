import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic parameter for tent map with fractional dimensionality
        self.chebyshev_params = np.random.uniform(2.5, 4.0, dim)
        # Fractional polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Adaptive conditioning factors with extreme variability
        self.conditioning = np.random.uniform(0.01, 5.0, dim)
        # Phase shifts for trigonometric components with fractional frequencies
        self.phase_shifts = np.random.uniform(0, 8*np.pi, dim)
        # Fractional polynomial degree for each dimension with higher variability
        self.poly_degree = np.random.randint(2, 15, dim)
        # Amplitude scaling with greater variation and fractional exponents
        self.amp_scaling = np.random.uniform(0.2, 4.0, dim)
        # Local minima positions with more diversity and clustered structure
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 12))
        # Additional interaction terms with hyperchaotic behavior
        self.interaction_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Dynamic parameter transitions with time-varying chaos
        self.transition_params = np.random.uniform(0.005, 0.3, dim)
        # Fractional chaotic modulation parameters
        self.fractional_modulation = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Hyperchaotic tent map oscillation with fractional parameter transitions
        for i in range(self.dim):
            # Tent map with dynamic parameter and fractional modulation
            param = self.chebyshev_params[i] * (1 + 0.5 * np.sin(x[i] * self.fractional_modulation[i]))
            tent_value = 1 - 2 * np.abs(x[i] - 0.5)
            chaotic_term = param * tent_value
            result += self.amp_scaling[i] * np.sin(chaotic_term + self.phase_shifts[i]) ** (self.poly_degree[i] / 2.0)
            
        # Fractional trigonometric-polynomial coupling between dimensions
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.sin(x[i] ** (self.poly_degree[i] / 3.0)) * x[j]
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 5) * np.sin(x[i] ** 2)
            
        # Local minima attraction with multiple candidates and clustered structure
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** (self.poly_degree[i] / 2.0)
            
        # Additional interaction terms between dimensions with hyperchaotic coupling
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.cos(x[i] * x[j] * self.fractional_modulation[i])
                
        # Combine components with weighted sum and chaotic weighting
        total = 0.20 * result + 0.35 * trig_poly_coupling_energy + 0.15 * conditioning_energy + 0.20 * local_energy + 0.10 * interaction_energy
        
        return total