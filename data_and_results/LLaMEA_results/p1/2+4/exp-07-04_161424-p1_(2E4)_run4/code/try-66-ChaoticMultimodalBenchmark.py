import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 15):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients for interaction terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.3
            rbfs[i] = weight * np.exp(-dist / (2 * 0.03**2))
        
        # Chaotic interaction using logistic map with sine modulation
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm) * np.cos(4 * self.logistic_seq))
        
        # Asymmetric noise with dynamic scaling based on input magnitude
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.05, 1.8, self.dim))
        
        # Higher-order polynomial interactions with chaotic coefficients
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**4 + 0.4 * x_norm**6 + 0.03 * x_norm**8))
        
        # Add sharp transition zones using step functions
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > 0.7)
        
        # Combine all components with dynamic weights
        total = 0.3 * np.sum(rbfs) + 0.3 * chaotic + 0.18 * noise + 0.12 * poly_interaction + 0.05 * transitions
        
        # Add a global scaling factor to increase conditioning
        return total * (1 + 0.6 * np.sin(np.sum(x_norm**2)))