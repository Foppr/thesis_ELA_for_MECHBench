import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos with modified growth rate
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 10):
            self.logistic_seq = np.append(self.logistic_seq, 3.8 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with variable width
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * 0.05**2))
        
        # Modified logistic map chaotic dynamics with phase shift
        chaotic = np.sum(np.sin(2 * np.pi * x_norm + self.logistic_seq) * np.cos(2 * np.pi * x_norm))
        
        # Asymmetric noise with sinusoidal modulation
        noise = np.sum(np.abs(x_norm) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)) * np.random.uniform(0.6, 1.4, self.dim))
        
        # Polynomial interaction with mixed degrees and cross-terms
        poly_interaction = np.sum(x_norm**4) + 0.3 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8) + 0.2 * np.sum(x_norm[1:] * x_norm[:-1])
        
        # Combine components with adjusted weights
        return 0.25 * np.sum(rbfs) + 0.45 * chaotic + 0.25 * noise + 0.05 * poly_interaction