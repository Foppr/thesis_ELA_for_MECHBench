import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Adaptive RBF centers based on logistic sequence
        self.rbf_centers = self.logistic_seq * 2.0 - 1.0
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with adaptive centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            diff = x_norm - self.rbf_centers[i]
            rbfs[i] = np.exp(-np.sum(diff**2) / (2 * (0.05 + 0.1 * np.abs(self.logistic_seq[i])**2)))
        
        # Chaotic dynamics with higher frequency modulation
        chaotic = np.sum(np.sin(10 * self.logistic_seq * x_norm) * np.cos(5 * self.logistic_seq * x_norm))
        
        # Asymmetric Levy noise component
        levy_noise = np.sum(np.abs(x_norm)**(1.5) * np.random.standard_cauchy(self.dim))
        
        # Mixed-order polynomial interaction with non-uniform exponents
        poly_interaction = (np.sum(x_norm**3) + 
                           0.3 * np.sum(x_norm**4) + 
                           0.1 * np.sum(x_norm**6) + 
                           0.05 * np.sum(x_norm**8))
        
        # Additional sharp transition components
        transitions = np.sum(np.abs(x_norm - 0.5 * np.sin(self.logistic_seq)) < 0.1)
        
        # Combine all components with dynamic weights
        return (0.25 * np.sum(rbfs) + 
                0.35 * chaotic + 
                0.25 * levy_noise + 
                0.15 * poly_interaction + 
                0.05 * transitions)