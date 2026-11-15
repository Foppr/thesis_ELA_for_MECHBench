import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and longer period
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 25):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients for interaction terms with increased complexity
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.poly_coeffs_2 = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.03**2))
        
        # Chaotic interaction using logistic map with sine modulation and cosine correction
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm) * np.cos(3 * self.logistic_seq) + 
                         np.cos(self.logistic_seq * x_norm) * np.sin(2 * self.logistic_seq))
        
        # Asymmetric noise with dynamic scaling based on input magnitude and chaotic modulation
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.05, 3.0, self.dim) * 
                       (1 + 0.5 * np.sin(self.logistic_seq)))
        
        # Higher-order polynomial interactions with chaotic coefficients and cross-terms
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**3 + 0.3 * x_norm**5 + 0.05 * x_norm**7) + 
                                 self.poly_coeffs_2 * (x_norm**4 + 0.2 * x_norm**6))
        
        # Add sharp transition zones using step functions and chaotic threshold modulation
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > 0.85 + 
                            0.3 * np.sin(self.logistic_seq * np.pi))
        
        # Combine all components with dynamic weights and chaotic modulation
        total = 0.3 * np.sum(rbfs) + 0.3 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.05 * transitions
        
        # Add a global scaling factor to increase conditioning with chaotic modulation
        return total * (1 + 0.7 * np.sin(np.sum(x_norm**2) * self.logistic_seq[0]))