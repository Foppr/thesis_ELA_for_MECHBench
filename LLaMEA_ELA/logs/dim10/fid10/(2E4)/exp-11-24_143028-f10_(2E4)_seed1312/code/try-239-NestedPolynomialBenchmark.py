import numpy as np

class NestedPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        self.interference_strength = np.random.uniform(0.5, 2.0, dim)
        self.penalty_exponents = np.random.uniform(2.0, 6.0, dim)
        # Generate random coefficients for nested polynomials
        self.poly_coeffs = []
        for i in range(dim):
            # Each dimension has a different degree polynomial
            degree = np.random.randint(3, 7)
            coeffs = np.random.uniform(-1.0, 1.0, degree + 1)
            self.poly_coeffs.append(coeffs)
        # Add harmonic shift components
        self.harmonic_shifts = np.random.uniform(-1.0, 1.0, dim)
        self.frequency_modulators = np.random.uniform(0.5, 3.0, dim)
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested polynomial component
        polynomial_term = 0.0
        for i in range(self.dim):
            # Evaluate nested polynomial of degree 3-6
            poly_val = 0.0
            for j, coeff in enumerate(self.poly_coeffs[i]):
                poly_val += coeff * (x[i] ** j)
            # Apply conditioning factor
            polynomial_term += self.conditioning_factors[i] * poly_val**2
            
        # Cross-dimensional interference term with enhanced frequency
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interference based on distance and conditioning with frequency modulation
                dist = np.abs(x[i] - x[j])
                freq_mod_i = self.frequency_modulators[i]
                freq_mod_j = self.frequency_modulators[j]
                interference_term += (self.interference_strength[i] * 
                                   self.interference_strength[j] * 
                                   np.sin(freq_mod_i * dist) * 
                                   np.exp(-0.1 * freq_mod_j * dist**2))
                
        # Dynamic penalty landscape with multiple scales and harmonic shifts
        penalty_term = 0.0
        for i in range(self.dim):
            # Multiple penalty components with different exponents
            penalty = 0.0
            shift = self.harmonic_shifts[i]
            for scale in [0.5, 1.0, 2.0, 5.0]:
                scaled_x = (x[i] + shift) / scale
                penalty += (np.abs(scaled_x) ** self.penalty_exponents[i]) * np.exp(-0.05 * scaled_x**2)
            penalty_term += penalty
            
        # Adaptive conditioning based on dimensionality
        adaptive_factor = np.log(self.dim + 1) + 1.0
        
        # Combine all components with dynamic weights
        result = adaptive_factor * polynomial_term + 0.7 * interference_term + 0.4 * penalty_term
        
        return result