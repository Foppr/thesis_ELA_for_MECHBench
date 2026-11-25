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
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(1.0, 10.0, dim)
        # Correlation structure between dimensions
        self.correlation_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.correlation_matrix, 1.0)
        # Global shift parameters
        self.global_shift = np.random.uniform(-2.0, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Polynomial component with adaptive conditioning
        for i in range(self.dim):
            poly_val = 0.0
            for d in range(4):
                poly_val += self.poly_coeffs[i, d] * (x[i] ** d)
            result += self.conditioning[i] * poly_val ** 2
            
        # Trigonometric component with phase shifts
        trig_energy = 0.0
        for i in range(self.dim):
            trig_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            trig_energy += trig_term ** 2
            
        # Radial basis function component
        rbf_energy = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(5):
                distance = np.abs(x[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-distance ** 2 / (2 * self.rbf_widths[i, j] ** 2))
            rbf_energy += rbf_sum ** 2
            
        # Correlation-induced interaction terms
        correlation_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    correlation_energy += self.correlation_matrix[i, j] * x[i] * x[j]
                    
        # Global shift effect
        shift_energy = 0.0
        for i in range(self.dim):
            shift_energy += (x[i] - self.global_shift[i]) ** 2
            
        # Combine all components with varying weights
        total = 0.3 * result + 0.25 * trig_energy + 0.2 * rbf_energy + 0.15 * correlation_energy + 0.1 * shift_energy
        
        return total