import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 15):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * 0.1**2))
        
        # Logistic map chaotic dynamics with fractal scaling
        chaotic = np.sum(self.logistic_seq * np.sin(2 * np.pi * x_norm) * np.cos(np.pi * x_norm))
        
        # Asymmetric noise component with adaptive scaling
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.3, 1.7, self.dim) * (1 + 0.5 * np.sin(self.logistic_seq)))
        
        # Polynomial interaction with mixed degrees and saddle points
        poly_interaction = np.sum(x_norm**3) + 0.5 * np.sum(x_norm**5) + 0.1 * np.sum(x_norm**7) - 0.05 * np.sum(x_norm**2)
        
        # Add saddle point structures
        saddle = 0.3 * np.sum(np.sin(3 * x_norm) * np.cos(2 * x_norm))
        
        # Combine components with varying weights
        return 0.25 * np.sum(rbfs) + 0.35 * chaotic + 0.25 * noise + 0.15 * poly_interaction + 0.05 * saddle