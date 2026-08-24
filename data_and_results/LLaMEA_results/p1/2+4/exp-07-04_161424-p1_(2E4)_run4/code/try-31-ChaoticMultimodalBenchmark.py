import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos with higher dimensionality
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Additional chaotic sequence for saddle points
        self.saddle_seq = np.array([0.1])
        for i in range(dim * 15):
            self.saddle_seq = np.append(self.saddle_seq, 3.5 * self.saddle_seq[-1] * (1 - self.saddle_seq[-1]))
        self.saddle_seq = self.saddle_seq[:dim]
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * 0.05**2))
        
        # Logistic map chaotic dynamics with saddle points
        chaotic = np.sum(self.logistic_seq * np.sin(2 * np.pi * x_norm)) + 0.5 * np.sum(self.saddle_seq * np.cos(2 * np.pi * x_norm))
        
        # Asymmetric noise component with fractal scaling
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.3, 1.7, self.dim) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)))
        
        # Polynomial interaction with mixed degrees and fractal scaling
        poly_interaction = np.sum(x_norm**3) + 0.5 * np.sum(x_norm**5) + 0.1 * np.sum(x_norm**7) + 0.05 * np.sum(x_norm**9)
        
        # Add saddle point structure
        saddle_term = np.sum((x_norm**2 - 1)**2)
        
        # Combine components with varying weights
        return 0.25 * np.sum(rbfs) + 0.35 * chaotic + 0.25 * noise + 0.15 * poly_interaction + 0.05 * saddle_term