import numpy as np

class MultimodalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial coefficients with higher degree terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 6))
        # Chaotic frequency modulation with dynamic coupling
        self.freqs = np.random.uniform(1.0, 5.0, dim)
        self.phase_modulators = np.random.uniform(0.1, 2.0, dim)
        # Enhanced radial basis functions with multiple centers
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 7))
        self.rbf_widths = np.random.uniform(0.3, 1.5, (dim, 7))
        # Adaptive conditioning with chaotic scaling
        self.conditioning = np.random.uniform(0.5, 15.0, dim)
        # Dynamic correlation matrix with chaotic coupling
        self.correlation_matrix = np.random.uniform(-0.7, 0.7, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Global shift parameters with chaotic variation
        self.global_shift = np.random.uniform(-3.0, 3.0, dim)
        # Chaotic penalty structure
        self.penalty_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced polynomial component with chaotic conditioning
        for i in range(self.dim):
            poly_val = 0.0
            for d in range(6):
                poly_val += self.poly_coeffs[i, d] * (x[i] ** d)
            # Apply chaotic conditioning factor
            chaos_factor = np.sin(x[i] * self.freqs[i]) + 1.5
            result += self.conditioning[i] * poly_val ** 2 * chaos_factor
            
        # Trigonometric component with dynamic phase modulation
        trig_energy = 0.0
        for i in range(self.dim):
            # Dynamic frequency modulation based on other dimensions
            mod_freq = self.freqs[i] * (1.0 + 0.3 * np.sin(x[(i+1) % self.dim]))
            trig_term = np.sin(mod_freq * x[i] + self.phase_modulators[i])
            trig_energy += trig_term ** 2
            
        # Enhanced radial basis function component
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(7):
                distance = np.abs(x[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-distance ** 2 / (2 * self.rbf_widths[i, j] ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Dynamic correlation-induced interaction terms
        correlation_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add chaotic coupling to correlation
                    coupling_factor = np.cos(x[i] * x[j]) + 1.0
                    correlation_energy += self.correlation_matrix[i, j] * x[i] * x[j] * coupling_factor
                    
        # Global shift effect with adaptive penalty
        shift_energy = 0.0
        for i in range(self.dim):
            distance_from_shift = np.abs(x[i] - self.global_shift[i])
            # Apply adaptive penalty based on distance and chaotic factors
            penalty = self.penalty_weights[i] * (1.0 + 0.5 * np.sin(x[i]))
            shift_energy += penalty * distance_from_shift ** 2
            
        # Combine all components with modified weights for better balance
        total = 0.25 * result + 0.2 * trig_energy + 0.25 * rbf_energy + 0.15 * correlation_energy + 0.15 * shift_energy
        
        return total