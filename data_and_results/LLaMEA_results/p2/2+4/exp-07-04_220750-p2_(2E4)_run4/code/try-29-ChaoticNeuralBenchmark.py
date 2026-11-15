import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sigmoidal activation terms with varying scales
        sig1 = np.sum(1.0 / (1.0 + np.exp(-x_norm)))
        sig2 = np.sum(1.0 / (1.0 + np.exp(-3 * x_norm**2)))
        sig3 = np.sum(1.0 / (1.0 + np.exp(-0.5 * x_norm**3)))
        
        # Recursive feedback component with chaotic behavior
        feedback = 0.0
        for i in range(min(5, self.dim)):
            if i < len(x_norm):
                feedback += np.sin(x_norm[i] * np.cos(x_norm[i]) * (i + 1))
        
        # Multi-scale resonance terms with different frequencies
        resonance = 0.0
        for i in range(1, 6):
            resonance += np.sin(i * x_norm**i).sum() * np.cos(i * x_norm**2).sum()
        
        # Polynomial coupling with exponential weights
        poly_coupling = np.sum(np.exp(0.1 * x_norm**4) * x_norm**2)
        
        # Cross-dimensional interaction with chaotic sine-wave coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x_norm) and j < len(x_norm):
                    cross_interaction += np.sin(x_norm[i] * x_norm[j] * (i + j + 1))
        
        # Combine all terms to form the final landscape
        return 0.5 * sig1 + 0.3 * sig2 + 0.2 * sig3 + 0.1 * feedback + 0.05 * resonance + 0.02 * poly_coupling + 0.01 * cross_interaction