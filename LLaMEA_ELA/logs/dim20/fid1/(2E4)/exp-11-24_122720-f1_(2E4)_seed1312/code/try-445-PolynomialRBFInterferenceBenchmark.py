import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion parameters
        self.poly_degrees = np.random.randint(3, 10, dim)
        self.poly_coefficients = np.random.uniform(0.2, 3.0, dim)
        self.poly_exponents = np.random.uniform(1.0, 4.0, dim)
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, dim))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Cross-dimensional interference patterns
        self.interference_amplitudes = np.random.uniform(0.5, 4.0, (dim, dim))
        self.interference_frequencies = np.random.randint(1, 6, (dim, dim))
        self.interference_phase_shifts = np.random.uniform(0, 2*np.pi, (dim, dim))
        # Dynamic conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 5.0, dim)
        # Coupled sinusoidal modulation for increased complexity
        self.modulation_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.modulation_frequencies = np.random.randint(2, 8, dim)
        # Quaternion-based coupling for enhanced non-separability
        self.quaternion_weights = np.random.uniform(-1.0, 1.0, (dim, 4))
        self.quaternion_angles = np.random.uniform(0, 2*np.pi, (dim, 3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = self.poly_coefficients[i] * (xi ** self.poly_degrees[i]) * np.exp(-self.poly_exponents[i] * abs(xi))
            poly_sum += poly_term
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                distance = abs(xi - self.rbf_centers[i][j])
                rbf_term += self.rbf_weights[i][j] * np.exp(-0.5 * (distance / self.rbf_widths[i][j]) ** 2)
            rbf_sum += rbf_term
        
        # Cross-dimensional interference component
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    interference_term += (self.interference_amplitudes[i][j] * 
                                       np.sin(self.interference_frequencies[i][j] * xi + self.interference_phase_shifts[i][j]) *
                                       np.cos(self.interference_frequencies[i][j] * x[j]))
            interference_sum += interference_term
        
        # Coupled sinusoidal modulation for enhanced complexity
        modulation_sum = 0
        for i in range(self.dim):
            modulation_term = self.modulation_amplitudes[i] * np.sin(self.modulation_frequencies[i] * x[i])
            modulation_sum += modulation_term
        
        # Quaternion-based coupling component for non-separability
        quaternion_sum = 0
        for i in range(self.dim):
            q = self.quaternion_weights[i]
            angles = self.quaternion_angles[i]
            # Quaternion rotation effect on dimension i
            rot_xi = x[i] * (q[0]**2 - q[1]**2 - q[2]**2 - q[3]**2) + \
                     2 * (q[0]*q[1]*x[0] + q[0]*q[2]*x[1] + q[0]*q[3]*x[2]) + \
                     2 * (q[1]*q[2]*x[2] - q[1]*q[3]*x[3])
            quaternion_sum += rot_xi
        
        # Combine all components with dynamic conditioning
        result = (0.8 * poly_sum + 
                 1.5 * rbf_sum + 
                 1.2 * interference_sum + 
                 0.5 * modulation_sum + 
                 0.3 * quaternion_sum) * self.conditioning_factors[np.random.randint(0, self.dim)]
        
        return result