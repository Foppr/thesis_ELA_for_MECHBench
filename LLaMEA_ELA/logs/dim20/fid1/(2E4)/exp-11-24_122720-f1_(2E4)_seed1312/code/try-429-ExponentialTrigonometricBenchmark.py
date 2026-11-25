import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial growth parameters
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(0.1, 2.0, dim)
        # Chaotic coupling coefficients
        self.coupling_amplitudes = np.random.uniform(0.5, 3.0, (dim, dim))
        self.coupling_frequencies = np.random.randint(2, 8, (dim, dim))
        self.coupling_phase_shifts = np.random.uniform(0, 2*np.pi, (dim, dim))
        # Hessian field parameters
        self.hessian_magnitudes = np.random.uniform(0.5, 4.0, (dim, dim))
        self.hessian_offsets = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Dynamic scaling factor
        self.dynamic_scale = np.random.uniform(0.3, 3.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial growth component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = self.poly_coefficients[i] * (xi ** self.poly_degrees[i])
            poly_sum += poly_term
        
        # Chaotic coupling component
        chaos_sum = 0
        for i in range(self.dim):
            xi = x[i]
            coupling_term = 0
            for j in range(self.dim):
                if i != j:
                    coupling_term += (self.coupling_amplitudes[i][j] * 
                                    np.sin(self.coupling_frequencies[i][j] * xi + self.coupling_phase_shifts[i][j]) *
                                    np.cos(self.coupling_frequencies[i][j] * x[j]))
            chaos_sum += coupling_term
        
        # Hessian field component
        hessian_sum = 0
        for i in range(self.dim):
            xi = x[i]
            hessian_term = 0
            for j in range(self.dim):
                if i != j:
                    hessian_term += self.hessian_magnitudes[i][j] * (xi - x[j]) ** 2 + self.hessian_offsets[i][j]
            hessian_sum += hessian_term
        
        # Combine all components with dynamic scaling
        result = (0.5 * poly_sum + 
                 1.2 * chaos_sum + 
                 0.7 * hessian_sum) * self.dynamic_scale
        
        return result