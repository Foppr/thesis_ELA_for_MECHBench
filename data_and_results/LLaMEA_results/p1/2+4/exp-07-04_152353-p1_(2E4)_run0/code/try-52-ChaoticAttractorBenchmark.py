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
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation between dimensions
                decay = np.exp(-0.1 * (i - j)**2)
                modal += decay * (x_normalized[i] - x_normalized[j])**2
                
        # Periodic sine-wave interactions
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(x_normalized[i] * 3.0) * np.cos(x_normalized[i] * 2.0)
            
        # Central repulsive force to create complex basins
        center_force = 0
        center = np.zeros(self.dim)
        for i in range(self.dim):
            center[i] = np.sin(i * 0.5)
        dist_to_center = np.linalg.norm(x_normalized - center)
        center_force = 1.0 / (1.0 + dist_to_center**2)
        
        # Additional high-frequency oscillation component
        oscillation = 0
        for i in range(self.dim):
            oscillation += np.sin(x_normalized[i] * 10.0) * np.cos(x_normalized[i] * 7.0)
            
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * modal + 0.20 * periodic + 0.15 * center_force + 0.10 * oscillation
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6))
        result += perturbation
        
        return result