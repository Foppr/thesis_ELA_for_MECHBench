import numpy as np

class MultimodalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial coefficients for different degrees
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Trigonometric frequencies and phases
        self.freqs = np.random.uniform(0.5, 3.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 5))
        # Adaptive conditioning parameters with chaotic scaling
        self.conditioning = np.random.uniform(1.0, 10.0, dim)
        # Correlation structure between dimensions with chaotic perturbations
        self.correlation_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Global shift parameters with chaotic component
        self.global_shift = np.random.uniform(-2.0, 2.0, dim)
        # Chaotic scaling factors for enhanced multimodality
        self.chaotic_factors = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial component with chaotic conditioning
        for i in range(self.dim):
            poly_val = 0.0
            for d in range(4):
                poly_val += self.poly_coeffs[i, d] * (x[i] ** d)
            result += self.conditioning[i] * self.chaotic_factors[i] * poly_val ** 2
            
        # Trigonometric component with chaotic phase modulation
        trig_energy = 0.0
        for i in range(self.dim):
            # Add chaotic modulation to frequencies and phases
            freq_mod = self.freqs[i] * (1.0 + 0.1 * np.sin(i * 2.0 * np.pi / self.dim))
            phase_mod = self.phases[i] + 0.2 * np.cos(i * 3.0 * np.pi / self.dim)
            trig_term = np.sin(freq_mod * x[i] + phase_mod)
            trig_energy += trig_term ** 2
            
        # Radial basis function component with chaotic width scaling
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(5):
                distance = np.abs(x[i] - self.rbf_centers[i, j])
                # Apply chaotic scaling to widths
                width_scaled = self.rbf_widths[i, j] * (1.0 + 0.1 * np.sin(j * 1.5 * np.pi / self.dim))
                rbf_sum += np.exp(-distance ** 2 / (2 * width_scaled ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Correlation-induced interaction terms with chaotic perturbations
        correlation_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add chaotic perturbation to correlation coefficients
                    corr_pert = self.correlation_matrix[i, j] * (1.0 + 0.05 * np.sin(i * j * np.pi / self.dim))
                    correlation_energy += corr_pert * x[i] * x[j]
                    
        # Global shift effect with chaotic modulation
        shift_energy = 0.0
        for i in range(self.dim):
            # Add chaotic component to shift
            shift_mod = self.global_shift[i] * (1.0 + 0.1 * np.cos(i * np.pi / self.dim))
            shift_energy += (x[i] - shift_mod) ** 2
            
        # Combine all components with varying weights and chaotic scaling
        total = 0.3 * result + 0.25 * trig_energy + 0.2 * rbf_energy + 0.15 * correlation_energy + 0.1 * shift_energy
        
        return total