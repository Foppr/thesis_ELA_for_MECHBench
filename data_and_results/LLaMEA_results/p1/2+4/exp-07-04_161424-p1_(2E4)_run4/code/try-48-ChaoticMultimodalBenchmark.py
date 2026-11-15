import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients for interaction terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        
        # Add more chaotic modulation for better conditioning
        self.chaotic_mod = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.03**2))
        
        # Chaotic interaction using logistic map with sine modulation and additional chaos
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm * self.chaotic_mod) * np.cos(3 * self.logistic_seq))
        
        # Asymmetric noise with dynamic scaling based on input magnitude and chaotic modulation
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.05, 1.5, self.dim) * self.chaotic_mod)
        
        # Higher-order polynomial interactions with chaotic coefficients and increased degree
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**4 + 0.4 * x_norm**6 + 0.1 * x_norm**8))
        
        # Add sharp transition zones using step functions with chaotic thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * self.chaotic_mod)) > 0.7)
        
        # Combine all components with dynamic weights
        total = 0.3 * np.sum(rbfs) + 0.3 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.05 * transitions
        
        # Add a global scaling factor to increase conditioning and introduce more irregularity
        return total * (1 + 0.7 * np.sin(np.sum(x_norm**3)))