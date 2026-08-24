import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos with higher sensitivity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 15):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            distance = np.sum((x_norm - self.logistic_seq[i])**2)
            rbfs[i] = np.exp(-distance / (2 * (0.05 + 0.1 * np.abs(self.logistic_seq[i])**2)))
        
        # Enhanced chaotic dynamics with frequency modulation
        chaotic = np.sum(np.sin(2 * np.pi * x_norm * (1 + 0.5 * self.logistic_seq)))
        
        # Improved asymmetric noise with adaptive scaling
        noise = np.sum(np.abs(x_norm) * (1 + 0.3 * np.sin(3 * np.pi * self.logistic_seq)))
        
        # Modified polynomial interaction with cross-terms
        poly_interaction = np.sum(x_norm**3) + 0.3 * np.sum(x_norm**5) + 0.05 * np.sum(x_norm**7)
        
        # Cross-dimensional interactions
        cross_terms = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Combine components with optimized weights
        return 0.25 * np.sum(rbfs) + 0.35 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.05 * cross_terms