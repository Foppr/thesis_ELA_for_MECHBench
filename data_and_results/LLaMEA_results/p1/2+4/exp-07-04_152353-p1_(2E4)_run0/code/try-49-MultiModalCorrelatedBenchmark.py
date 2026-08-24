import numpy as np

class MultiModalCorrelatedBenchmark:
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
            # Create multiple local minima with varying distances
            for j in range(1, 4):
                modal += np.exp(-j * np.abs(x_normalized[i] - j * 0.3)) * np.sin(j * x_normalized[i])
        
        # Asymmetric saddle point regions
        saddle = 0
        for i in range(self.dim):
            # Create asymmetric regions using piecewise functions
            if x_normalized[i] < 0:
                saddle += (x_normalized[i] + 0.5)**3
            else:
                saddle += (x_normalized[i] - 0.5)**3
                
        # Correlated noise component with varying strength
        noise = 0
        for i in range(self.dim):
            # Exponentially decaying correlation with previous dimensions
            for j in range(i):
                noise += 0.1 * np.exp(-0.1 * (i - j)) * x_normalized[i] * x_normalized[j]
        
        # High-frequency oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(10 * x_normalized[i]) * np.cos(7 * x_normalized[i])
            
        # Combine all components with different weights
        result = 0.4 * f1 + 0.3 * modal + 0.15 * saddle + 0.1 * noise + 0.05 * oscillatory
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 9))
        result += perturbation
        
        return result