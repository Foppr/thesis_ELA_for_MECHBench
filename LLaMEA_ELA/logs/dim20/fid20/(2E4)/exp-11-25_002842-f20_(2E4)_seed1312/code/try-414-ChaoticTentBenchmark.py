import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for sine map
        self.sine_params = np.random.uniform(1.5, 3.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Adaptive conditioning factors with higher variability
        self.conditioning = np.random.uniform(0.1, 3.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 4*np.pi, dim)
        # Polynomial degree for each dimension with higher values
        self.poly_degree = np.random.randint(3, 10, dim)
        # Amplitude scaling with greater variation
        self.amp_scaling = np.random.uniform(0.5, 3.5, dim)
        # Local minima positions with more diversity
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 8))
        # Additional interaction terms with chaotic behavior
        self.interaction_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Dynamic parameter transitions
        self.transition_params = np.random.uniform(0.01, 0.2, dim)
        # Enhanced polynomial coupling coefficients
        self.poly_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Modified interaction frequency
        self.freq_modifier = np.random.uniform(0.5, 2.0, dim)
        # Sine map chaotic dynamics with higher sensitivity
        self.sine_sensitivity = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sine map oscillation with dynamic parameter transitions
        for i in range(self.dim):
            # Sine map with dynamic parameter
            param = self.sine_params[i] * (1 + 0.3 * np.sin(x[i]))
            sine_value = np.sin(param * x[i])
            chaotic_term = self.sine_sensitivity[i] * sine_value
            result += self.amp_scaling[i] * np.cos(chaotic_term + self.phase_shifts[i]) ** 3
            
        # Trigonometric-polynomial coupling between dimensions
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.cos(x[i] ** self.poly_degree[i]) * x[j]
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 3) * np.cos(x[i])
            
        # Local minima attraction with multiple candidates
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 2
            
        # Additional interaction terms between dimensions with chaotic coupling
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Enhanced polynomial coupling between dimensions
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** (self.poly_degree[i] + 2)) * (x[j] ** 3)
                    
        # Modified interaction with frequency scaling
        freq_interaction = 0.0
        for i in range(self.dim):
            freq_interaction += self.freq_modifier[i] * np.cos(x[i]) * np.sin(x[i])
            
        # Combine components with weighted sum and chaotic weighting
        total = 0.15 * result + 0.20 * trig_poly_coupling_energy + 0.20 * conditioning_energy + 0.15 * local_energy + 0.15 * interaction_energy + 0.10 * poly_coupling_energy + 0.05 * freq_interaction
        
        return total