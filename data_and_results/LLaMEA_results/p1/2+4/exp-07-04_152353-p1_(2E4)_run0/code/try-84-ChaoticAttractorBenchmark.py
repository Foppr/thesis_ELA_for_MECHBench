import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multimodal component with sine and cosine interactions
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(3 * x_normalized[i]) * np.cos(2 * x_normalized[i])
            
        # Polynomial interaction terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += (x_normalized[i]**3) * (x_normalized[j]**2) + (x_normalized[i]**2) * (x_normalized[j]**3)
                
        # Adaptive scaling based on dimension
        scaling = 0
        for i in range(self.dim):
            scaling += (i + 1) * np.abs(x_normalized[i])**1.5
            
        # Periodic landscape with varying frequencies
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(5 * x_normalized[i] + i * 0.5) + np.cos(4 * x_normalized[i] - i * 0.3)
            
        # Cross-terms with exponential decay
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-np.abs(x_normalized[i] - x_normalized[j])) * np.sin(x_normalized[i] * x_normalized[j])
                
        # Combine all components with different weights
        result = 0.25 * f1 + 0.2 * multimodal + 0.15 * polynomial + 0.2 * scaling + 0.15 * periodic + 0.05 * cross_term
        
        return result