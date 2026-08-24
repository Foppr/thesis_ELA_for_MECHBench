import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and periodicity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients for interaction terms with fractal-like distribution
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        # Add fractal-like scaling to coefficients
        for i in range(dim):
            self.poly_coeffs[i] *= (1 + 0.5 * np.sin(i * np.pi / 4))
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling, asymmetric weights, and multi-scale kernel
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            # Multi-scale kernel for enhanced complexity
            kernel = np.exp(-dist / (2 * (0.05 + 0.02 * np.sin(i * np.pi / 3))**2))
            rbfs[i] = weight * kernel
        
        # Chaotic interaction using logistic map with sine modulation and phase shift
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm + np.pi/4) * np.cos(3 * self.logistic_seq + np.pi/6))
        
        # Asymmetric noise with dynamic scaling based on input magnitude and chaotic modulation
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.0, self.dim) * (1 + 0.3 * np.sin(self.logistic_seq)))
        
        # Higher-order polynomial interactions with chaotic coefficients and cross-terms
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**3 + 0.3 * x_norm**5 + 0.05 * x_norm**7))
        # Add cross-terms for increased complexity
        cross_terms = np.sum(np.outer(x_norm, x_norm) * np.random.uniform(-0.1, 0.1, (self.dim, self.dim)))
        
        # Add sharp transition zones using step functions with chaotic thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi + self.logistic_seq)) > 0.8)
        
        # Hybrid fitness aggregation with dynamic weights based on chaotic sequence
        dynamic_weights = np.abs(np.sin(self.logistic_seq * np.pi / 2)) + 0.1
        dynamic_weights = dynamic_weights / np.sum(dynamic_weights)
        
        total = (0.2 * np.sum(rbfs) + 
                 0.3 * chaotic + 
                 0.25 * noise + 
                 0.15 * poly_interaction + 
                 0.1 * transitions + 
                 0.05 * cross_terms)
        
        # Apply a novel chaotic conditioning factor with periodic modulation
        conditioning = 1 + 0.7 * np.sin(np.sum(x_norm**2) * np.pi / 2 + self.logistic_seq[0])
        total *= conditioning
        
        # Add a global scaling factor to increase conditioning and introduce more irregularity
        return total * (1 + 0.3 * np.sin(np.sum(x_norm**4)))
