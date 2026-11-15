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
        
        # Additional chaotic sequence for enhanced complexity
        self.secondary_seq = np.random.rand(dim) * 2 - 1
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.3
            rbfs[i] = weight * np.exp(-dist / (2 * 0.03**2))
        
        # Chaotic interaction using logistic map with sine modulation and secondary chaos
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm) * np.cos(3 * self.logistic_seq) * 
                        (1 + 0.2 * np.sin(self.secondary_seq * x_norm)))
        
        # Asymmetric noise with dynamic scaling based on input magnitude and chaotic sequence
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.05, 1.5, self.dim) * 
                      (1 + 0.1 * np.sin(self.logistic_seq)))
        
        # Higher-order polynomial interactions with chaotic coefficients and additional terms
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**3 + 0.4 * x_norm**5 + 0.08 * x_norm**7 + 
                                                     0.02 * x_norm**9))
        
        # Add sharp transition zones using step functions with chaotic thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * (1 + 0.1 * self.logistic_seq))) > 0.7)
        
        # Combine all components with dynamic weights
        total = 0.3 * np.sum(rbfs) + 0.3 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.05 * transitions
        
        # Add a global scaling factor to increase conditioning and introduce more irregularity
        return total * (1 + 0.6 * np.sin(np.sum(x_norm**2) * (1 + 0.1 * np.sum(self.logistic_seq))))