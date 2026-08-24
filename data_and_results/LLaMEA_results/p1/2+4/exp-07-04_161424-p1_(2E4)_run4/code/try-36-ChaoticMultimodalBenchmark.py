import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 10):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling and shift
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            shift = np.sin(self.logistic_seq[i] * np.pi)
            rbfs[i] = np.exp(-np.sum((x_norm - shift)**2) / (2 * 0.15**2))
        
        # Logistic map chaotic dynamics
        chaotic = np.sum(self.logistic_seq * np.sin(3 * np.pi * x_norm))
        
        # Asymmetric noise component with modified range
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.3, 1.7, self.dim))
        
        # Increased polynomial interaction with higher degrees
        poly_interaction = np.sum(x_norm**4) + 0.3 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Combine components with varying weights
        return 0.25 * np.sum(rbfs) + 0.45 * chaotic + 0.25 * noise + 0.05 * poly_interaction