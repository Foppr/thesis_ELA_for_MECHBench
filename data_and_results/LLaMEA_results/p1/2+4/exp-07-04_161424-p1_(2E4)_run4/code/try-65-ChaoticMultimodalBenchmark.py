import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and entropy
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients with entropy-based distribution
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, dim)
        
        # Precompute entropy-based weights for RBFs
        self.rbf_weights = np.random.exponential(1.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling, entropy weights, and cross-terms
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = self.rbf_weights[i] * (np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5)
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2))
        
        # Chaotic interaction using logistic map with sine modulation and entropy
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm) * np.cos(3 * self.logistic_seq) * 
                         np.exp(-np.sum(np.abs(x_norm)) / self.dim))
        
        # Novel entropy-based noise with dynamic scaling and cross-correlation
        entropy_noise = np.sum(np.abs(x_norm) * np.random.exponential(1.0, self.dim))
        
        # Higher-order polynomial interactions with chaotic coefficients and entropy
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**5 + 0.5 * x_norm**7 + 0.05 * x_norm**9))
        
        # Add sharp transition zones using step functions with entropy
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > 0.8)
        
        # Add entropy-based conditioning factor
        entropy_cond = 1 + 0.8 * np.std(np.abs(x_norm))
        
        # Combine all components with dynamic weights
        total = 0.25 * np.sum(rbfs) + 0.25 * chaotic + 0.2 * entropy_noise + 0.15 * poly_interaction + 0.15 * transitions
        
        # Add global scaling factor with entropy-based adjustment
        return total * entropy_cond * (1 + 0.5 * np.sin(np.sum(x_norm**2) / self.dim))