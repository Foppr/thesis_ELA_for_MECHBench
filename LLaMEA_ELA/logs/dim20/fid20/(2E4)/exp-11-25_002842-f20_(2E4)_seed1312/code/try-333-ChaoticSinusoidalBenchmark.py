import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial coefficients with higher degree terms and chaotic modulation
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 8))
        # Chaotic frequency modulation with dynamic coupling and fractal-like behavior
        self.freqs = np.random.uniform(0.5, 6.0, dim)
        self.phase_modulators = np.random.uniform(0.05, 3.0, dim)
        # Fractal-like radial basis functions with multiple centers and chaotic widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 9))
        self.rbf_widths = np.random.uniform(0.1, 2.0, (dim, 9))
        # Adaptive conditioning with chaotic scaling and fractal dimensionality
        self.conditioning = np.random.uniform(0.1, 20.0, dim)
        # Dynamic correlation matrix with fractal coupling and chaotic interaction
        self.correlation_matrix = np.random.uniform(-0.9, 0.9, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Global shift parameters with fractal variation and chaotic perturbations
        self.global_shift = np.random.uniform(-4.0, 4.0, dim)
        # Chaotic penalty structure with multi-scale adaptive weights
        self.penalty_weights = np.random.uniform(0.2, 3.0, dim)
        # Fractal dimensionality modifier for enhanced complexity
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced polynomial component with chaotic conditioning and fractal dimensionality
        for i in range(self.dim):
            poly_val = 0.0
            for d in range(8):
                poly_val += self.poly_coeffs[i, d] * (x[i] ** d)
            # Apply fractal conditioning factor with chaotic modulation
            chaos_factor = np.sin(x[i] * self.freqs[i]) + np.cos(x[i] * self.freqs[i] * 0.7) + 2.0
            result += self.conditioning[i] * poly_val ** 2 * chaos_factor
            
        # Trigonometric component with dynamic phase modulation and fractal structure
        trig_energy = 0.0
        for i in range(self.dim):
            # Dynamic frequency modulation based on other dimensions with fractal coupling
            mod_freq = self.freqs[i] * (1.0 + 0.4 * np.sin(x[(i+1) % self.dim]) * np.cos(x[(i+2) % self.dim]))
            trig_term = np.sin(mod_freq * x[i] + self.phase_modulators[i])
            trig_energy += trig_term ** 2
            
        # Fractal-like radial basis function component with chaotic widths
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(9):
                distance = np.abs(x[i] - self.rbf_centers[i, j])
                # Apply fractal width scaling
                width = self.rbf_widths[i, j] * (1.0 + 0.2 * np.sin(i * x[j]))
                rbf_sum += np.exp(-distance ** 2 / (2 * width ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Fractal correlation-induced interaction terms with chaotic coupling
        correlation_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add fractal coupling to correlation
                    coupling_factor = np.cos(x[i] * x[j]) + np.sin(x[i] * x[j] * 0.5) + 1.0
                    correlation_energy += self.correlation_matrix[i, j] * x[i] * x[j] * coupling_factor
                    
        # Global shift effect with adaptive penalty and fractal perturbation
        shift_energy = 0.0
        for i in range(self.dim):
            distance_from_shift = np.abs(x[i] - self.global_shift[i])
            # Apply multi-scale adaptive penalty based on distance and chaotic factors
            penalty = self.penalty_weights[i] * (1.0 + 0.6 * np.sin(x[i]) * np.cos(x[i] * 0.3))
            shift_energy += penalty * distance_from_shift ** 2
            
        # Combine all components with modified weights for better balance and fractal complexity
        total = 0.15 * result + 0.18 * trig_energy + 0.22 * rbf_energy + 0.18 * correlation_energy + 0.27 * shift_energy
        
        return total