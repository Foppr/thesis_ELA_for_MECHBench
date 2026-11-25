import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial coefficients with higher degree terms and chaotic modulation
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 8))
        # Chaotic frequency modulation with dynamic coupling and fractal-like behavior
        self.freqs = np.random.uniform(0.5, 8.0, dim)
        self.phase_modulators = np.random.uniform(0.1, 3.0, dim)
        # Enhanced radial basis functions with multiple centers and dynamic widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 9))
        self.rbf_widths = np.random.uniform(0.2, 2.0, (dim, 9))
        # Adaptive conditioning with chaotic scaling and fractal-like structures
        self.conditioning = np.random.uniform(0.3, 20.0, dim)
        # Dynamic correlation matrix with chaotic coupling and fractal-induced interactions
        self.correlation_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Global shift parameters with chaotic variation and multi-scale effects
        self.global_shift = np.random.uniform(-4.0, 4.0, dim)
        # Chaotic penalty structure with fractal-like complexity
        self.penalty_weights = np.random.uniform(0.3, 2.5, dim)
        # Fractal-like chaotic parameters for enhanced complexity
        self.fractal_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced polynomial component with chaotic conditioning and fractal modulation
        for i in range(self.dim):
            poly_val = 0.0
            for d in range(8):
                poly_val += self.poly_coeffs[i, d] * (x[i] ** d)
            # Apply fractal chaotic conditioning factor
            chaos_factor = np.sin(x[i] * self.freqs[i]) + np.cos(x[i] * self.fractal_params[i]) + 2.0
            result += self.conditioning[i] * poly_val ** 2 * chaos_factor
            
        # Trigonometric component with dynamic phase modulation and fractal-like structures
        trig_energy = 0.0
        for i in range(self.dim):
            # Dynamic frequency modulation based on other dimensions with fractal influence
            mod_freq = self.freqs[i] * (1.0 + 0.5 * np.sin(x[(i+1) % self.dim]) * self.fractal_params[i])
            trig_term = np.sin(mod_freq * x[i] + self.phase_modulators[i]) + np.cos(x[i] * self.fractal_params[i])
            trig_energy += trig_term ** 2
            
        # Enhanced radial basis function component with fractal-like interaction
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(9):
                distance = np.abs(x[i] - self.rbf_centers[i, j])
                # Fractal-like width modulation
                width_mod = self.rbf_widths[i, j] * (1.0 + 0.3 * np.sin(x[i] * self.fractal_params[i]))
                rbf_sum += np.exp(-distance ** 2 / (2 * width_mod ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Dynamic correlation-induced interaction terms with fractal coupling
        correlation_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add fractal coupling to correlation
                    coupling_factor = np.cos(x[i] * x[j]) + np.sin(x[i] * self.fractal_params[i]) + np.cos(x[j] * self.fractal_params[j])
                    correlation_energy += self.correlation_matrix[i, j] * x[i] * x[j] * coupling_factor
                    
        # Global shift effect with adaptive penalty and fractal complexity
        shift_energy = 0.0
        for i in range(self.dim):
            distance_from_shift = np.abs(x[i] - self.global_shift[i])
            # Apply fractal-adaptive penalty based on distance and chaotic factors
            penalty = self.penalty_weights[i] * (1.0 + 0.7 * np.sin(x[i]) * self.fractal_params[i])
            shift_energy += penalty * distance_from_shift ** 2
            
        # Combine all components with modified weights for better balance and fractal complexity
        total = 0.3 * result + 0.25 * trig_energy + 0.25 * rbf_energy + 0.1 * correlation_energy + 0.1 * shift_energy
        
        return total