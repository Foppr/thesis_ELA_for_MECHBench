import numpy as np

class ChaoticPolynomialMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.center_offsets = np.random.uniform(-2.0, 2.0, dim)
        self.amplitude_factors = np.random.uniform(0.3, 2.5, dim)
        self.frequency_modulators = np.random.uniform(1.0, 2.0, dim)
        self.polynomial_coeffs = np.random.uniform(-0.5, 0.5, (dim, 4))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with dynamic conditioning
        base_condition = 1.0 + 0.5 * np.sin(np.sum(x**2) / self.dim)
        result += 0.1 * base_condition * np.sum(x**2)
        
        # Multi-modal sinusoidal components with chaotic modulation
        for i in range(self.dim):
            center = 3.0 * np.sin(self.center_offsets[i] * x[i] + 0.5 * np.cos(x[i]))
            amplitude = self.amplitude_factors[i]
            frequency = 3.0 + self.frequency_modulators[i] * np.sin(1.5 * x[i])
            
            # Polynomial chaos expansion with chaotic coefficients
            poly_term = (self.polynomial_coeffs[i, 0] + 
                        self.polynomial_coeffs[i, 1] * x[i] +
                        self.polynomial_coeffs[i, 2] * x[i]**2 +
                        self.polynomial_coeffs[i, 3] * x[i]**3)
            
            # Combined chaotic sinusoidal and polynomial contribution
            term = amplitude * (np.sin(frequency * x[i] + center)**4 + 
                               0.3 * np.cos(4 * frequency * x[i] + center)**4 +
                               0.7 * poly_term)
            result += term
            
        # Enhanced radial basis functions with dynamic chaotic centers
        for i in range(self.dim):
            # Chaotic dynamic center with multiple sinusoidal components
            dynamic_center = (2.0 * np.sin(x[i]) + 
                             0.8 * np.cos(2 * x[i]) + 
                             0.4 * np.sin(3 * x[i]) + 
                             0.2 * np.cos(5 * x[i]))
            
            # Position-dependent sigma with chaotic modulation
            sigma = 0.3 + 0.5 * (1.0 + np.sin(x[i])) * np.abs(np.cos(x[i]))
            
            rbf = np.exp(-0.5 * ((x[i] - dynamic_center) / sigma)**2)
            result += 1.5 * rbf
            
        # Enhanced cross-dimensional coupling with polynomial chaos interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Polynomial chaos based coupling strength
                coupling_strength = (1.0 + 
                                   0.5 * np.sin(x[i]) * np.cos(x[j]) +
                                   0.3 * np.sin(2 * x[i] + x[j]) *
                                   np.cos(1.5 * x[i] - x[j]))
                
                # Chaotic interaction with polynomial terms
                interaction = coupling_strength * (np.sin(x[i] + x[j])**3 + 
                                                  np.cos(x[i] - x[j])**3 +
                                                  0.5 * (x[i]**2 - x[j]**2))
                result += 0.6 * interaction
                
        # Dynamic conditioning with polynomial chaos modulation
        condition_factor = 1.0 + 0.8 * np.sin(np.sum(x**3) / self.dim + 
                                             0.4 * np.cos(np.sum(x**2)))
        result *= condition_factor
        
        # Add chaotic noise with polynomial chaos amplitude
        noise_amplitude = 0.12 * (1.0 + 0.4 * np.abs(np.sin(np.sum(x**3)) + 
                                                    0.3 * np.cos(np.sum(x**4))))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        # Add higher-order polynomial chaos terms
        for i in range(self.dim):
            result += 0.2 * (x[i]**5 - 2*x[i]**3 + x[i])
            
        return result