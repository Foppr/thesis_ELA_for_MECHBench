import numpy as np

class PolynomialRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced polynomial chaos expansion with chaotic scaling
        self.poly_degrees = np.random.randint(4, 10, dim)
        self.poly_coefficients = np.random.uniform(0.5, 4.0, dim)
        self.poly_exponents = np.random.uniform(0.5, 6.0, dim)
        # Chaotic radial basis function parameters
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 4.0, (dim, dim))
        self.rbf_weights = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Enhanced cross-dimensional interference with chaotic coupling
        self.interference_amplitudes = np.random.uniform(1.0, 6.0, (dim, dim))
        self.interference_frequencies = np.random.randint(2, 10, (dim, dim))
        self.interference_phase_shifts = np.random.uniform(0, 4*np.pi, (dim, dim))
        # Chaotic conditioning factors
        self.conditioning_factors = np.random.uniform(0.05, 8.0, dim)
        # Additional chaotic cosine modulation with dynamic frequency
        self.cosine_amplitudes = np.random.uniform(0.2, 1.5, dim)
        self.cosine_frequencies = np.random.randint(3, 12, dim)
        # Novel chaotic interaction terms
        self.chaotic_coupling_strength = np.random.uniform(0.5, 3.0, (dim, dim))
        self.chaotic_phase_shifts = np.random.uniform(0, 3*np.pi, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with chaotic scaling
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = self.poly_coefficients[i] * (xi ** self.poly_degrees[i]) * np.exp(-self.poly_exponents[i] * abs(xi))
            # Add chaotic modulation to polynomial coefficients
            chaotic_mod = 1.0 + 0.3 * np.sin(self.poly_exponents[i] * xi)
            poly_sum += poly_term * chaotic_mod
        
        # Enhanced radial basis function with chaotic weights
        rbf_sum = 0
        for i in range(self.dim):
            xi = x[i]
            rbf_term = 0
            for j in range(self.dim):
                distance = abs(xi - self.rbf_centers[i][j])
                # Add chaotic scaling to RBF widths
                chaotic_width = self.rbf_widths[i][j] * (1.0 + 0.2 * np.cos(xi * self.rbf_weights[i][j]))
                rbf_term += self.rbf_weights[i][j] * np.exp(-0.5 * (distance / chaotic_width) ** 2)
            rbf_sum += rbf_term
        
        # Enhanced cross-dimensional interference with chaotic coupling
        interference_sum = 0
        for i in range(self.dim):
            xi = x[i]
            interference_term = 0
            for j in range(self.dim):
                if i != j:
                    # Add chaotic coupling strength modulation
                    coupling_mod = 1.0 + 0.4 * np.sin(xi * self.chaotic_coupling_strength[i][j])
                    interference_term += (self.interference_amplitudes[i][j] * 
                                       np.sin(self.interference_frequencies[i][j] * xi + self.interference_phase_shifts[i][j]) *
                                       np.cos(self.interference_frequencies[i][j] * x[j]) * 
                                       coupling_mod)
            interference_sum += interference_term
        
        # Additional chaotic cosine modulation
        cosine_sum = 0
        for i in range(self.dim):
            # Add dynamic frequency modulation based on position
            dynamic_freq = self.cosine_frequencies[i] * (1.0 + 0.3 * np.sin(x[i]))
            cosine_sum += self.cosine_amplitudes[i] * np.cos(dynamic_freq * x[i])
        
        # Novel chaotic interaction component
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_interaction += (self.chaotic_coupling_strength[i][j] * 
                                         np.sin(x[i] * x[j] + self.chaotic_phase_shifts[i][j]) *
                                         np.exp(-0.1 * abs(x[i] - x[j])))
        
        # Combine all components with chaotic conditioning
        result = (0.9 * poly_sum + 
                 1.8 * rbf_sum + 
                 1.5 * interference_sum + 
                 0.7 * cosine_sum + 
                 0.6 * chaotic_interaction) * self.conditioning_factors[np.random.randint(0, self.dim)]
        
        return result