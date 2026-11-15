import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multi-modal component with exponentially decaying correlations
        modal = 0
        for i in range(self.dim):
            # Create multiple local minima using sinusoidal modulations
            modal += (x_normalized[i] - np.sin(i * 0.5))**2 + 0.5 * np.sin(x_normalized[i] * 3)**2
            
        # Trigonometric wave interference patterns
        wave = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                wave += np.sin(x_normalized[i] * x_normalized[j] * 2.0) * np.cos(x_normalized[i] + x_normalized[j] * 1.5)
                
        # Heavy-tailed noise component using Cauchy distribution
        noise = 0
        for i in range(self.dim):
            # Generate heavy-tailed noise using inverse transform sampling
            noise += np.tan(np.pi * (np.random.rand() - 0.5)) * np.exp(-i * 0.1)
            
        # Exponentially decaying correlation structure
        correlation = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                correlation += np.exp(-0.1 * (j - i)) * x_normalized[i] * x_normalized[j]
                
        # Combine all components with different weights
        result = 0.4 * f1 + 0.3 * modal + 0.2 * wave + 0.1 * correlation
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 7) * np.cos(x_normalized * 5))
        result += perturbation
        
        return result