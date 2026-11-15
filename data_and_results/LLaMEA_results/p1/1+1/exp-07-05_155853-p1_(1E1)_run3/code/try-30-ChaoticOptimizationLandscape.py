import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using multiple sine/cosine combinations with varying frequencies and amplitudes
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(12 * x[i]) * np.cos(9 * x[i]) + 
                       0.7 * np.sin(18 * x[i]) * np.cos(11 * x[i]) + 
                       0.3 * np.sin(25 * x[i]))
        
        # High-order polynomial potential with mixed degrees and cross-terms
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.1 * x[i]**6 + 0.2 * x[i]**5 - 0.15 * x[i]**4 + 
                          0.1 * x[i]**3 - 0.05 * x[i]**2 + 0.02 * x[i])
        
        # Cross-dimensional interaction with long-range couplings and non-linear decay
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Long-range interactions up to 5 dimensions
                cross_interaction += (np.exp(-0.05 * (x[i] - x[j])**2) * 
                                    (x[i]**3 + x[j]**3 + 0.5 * x[i] * x[j]))
        
        # Add adaptive noise component based on position and dimensionality
        noise = 0
        for i in range(self.dim):
            noise += 0.05 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * (1 + 0.1 * self.dim)
        
        # Global scaling factor with dynamic modulation
        scaling = 1.5 + 0.5 * np.sin(0.3 * np.sum(x**2)) * np.cos(0.2 * np.sum(x))
        
        # Combine all components
        return scaling * (chaotic + polynomial + cross_interaction + noise)