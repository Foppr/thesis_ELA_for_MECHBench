import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and fractional steps
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute fractional polynomial coefficients for complex interactions
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.frac_exponents = np.random.uniform(1.5, 3.5, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with fractional powers and chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * (0.02 + 0.01 * np.sin(self.logistic_seq[i] * 2 * np.pi))**2))
        
        # Chaotic interaction using logistic map with sine modulation and fractional exponents
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm)**self.frac_exponents * np.cos(3 * self.logistic_seq))
        
        # Dynamic noise with adaptive scaling based on input magnitude and chaotic sequence
        noise = np.sum(np.abs(x_norm)**1.5 * np.random.uniform(0.5, 2.5, self.dim) * (1 + 0.3 * np.sin(self.logistic_seq)))
        
        # Fractional polynomial interactions with chaotic coefficients and dynamic exponents
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**self.frac_exponents + 0.3 * x_norm**(2 * self.frac_exponents) + 0.02 * x_norm**(3 * self.frac_exponents)))
        
        # Add sharp transition zones using step functions with chaotic thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > (0.6 + 0.1 * np.sin(self.logistic_seq)))
        
        # Add dynamic sine-based basins for increased multimodality
        basins = np.sum(np.sin(x_norm * np.pi * 2)**2 * np.cos(x_norm * np.pi * 0.5)**2)
        
        # Combine all components with dynamic weights based on chaotic sequence
        total = 0.25 * np.sum(rbfs) + 0.25 * chaotic + 0.15 * noise + 0.1 * poly_interaction + 0.15 * transitions + 0.1 * basins
        
        # Add a global scaling factor to increase conditioning with chaotic modulation
        return total * (1 + 0.8 * np.sin(np.sum(x_norm**2)) * np.cos(self.logistic_seq[0]))