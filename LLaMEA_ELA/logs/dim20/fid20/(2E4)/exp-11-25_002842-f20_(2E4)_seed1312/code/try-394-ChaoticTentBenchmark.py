import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for each dimension (tent map)
        self.eta = np.random.uniform(1.0, 2.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning factors
        self.conditioning = np.random.uniform(0.5, 3.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial degree for each dimension
        self.poly_degree = np.random.randint(2, 6, dim)
        # Amplitude scaling for each dimension
        self.amp_scaling = np.random.uniform(0.5, 3.0, dim)
        # Coefficients for chaotic dynamics
        self.chaotic_coeffs = np.random.uniform(0.1, 0.9, (dim, 3))
        # Local optima positions for each dimension
        self.local_optima = np.random.uniform(-5.0, 5.0, (dim, 4))
        # Interaction coefficients between dimensions
        self.interaction_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic tent map dynamics with parameter transitions
        for i in range(self.dim):
            # Tent map: x_{n+1} = eta * min(x_n, 1-x_n)
            chaotic_val = self.eta[i] * min(x[i], 1 - x[i])
            result += self.amp_scaling[i] * np.sin(chaotic_val * x[i] + self.phase_shifts[i]) ** 2
            
        # Trigonometric-polynomial coupling between dimensions
        trig_poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_energy += self.trig_poly_coupling[i, j] * np.sin(x[i]) * (x[j] ** self.poly_degree[i])
                    
        # Adaptive conditioning with enhanced nonlinearity
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * np.tan(x[i]) * np.cos(x[i])
            
        # Local optima attraction
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_optima[i, :]))
            local_energy += min_dist ** 2
            
        # Additional interaction terms between dimensions
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.cos(x[i] - x[j])
                
        # Combine components with weighted sum
        total = 0.3 * result + 0.25 * trig_poly_energy + 0.2 * conditioning_energy + 0.15 * local_energy + 0.15 * interaction_energy
        
        return total