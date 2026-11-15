import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Multi-modal component with sinusoidal wells
        modal = 0
        for i in range(self.dim):
            # Create multiple wells using sinusoidal modulation
            modal += np.sin(x_normalized[i] * 5) * np.cos(x_normalized[i] * 3) + \
                     np.sin(x_normalized[i] * 2) * np.cos(x_normalized[i] * 7)
            
        # Radial basis function component with multiple centers
        rbf = 0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            # Use multiple radial basis functions with different centers
            center = centers[i % len(centers)] if self.dim > 5 else x_normalized[i]
            rbf += np.exp(-10 * (x_normalized[i] - center)**2)
            
        # Cross-term interactions creating complex coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add interaction terms that create complex coupling
                cross += np.sin(x_normalized[i] * x_normalized[j] * 2) * \
                         np.cos(x_normalized[i] + x_normalized[j]) * \
                         np.exp(-0.5 * (x_normalized[i] - x_normalized[j])**2)
                
        # Saddle point component with hyperbolic tangent terms
        saddle = 0
        for i in range(self.dim):
            # Create saddle points using hyperbolic tangent
            saddle += np.tanh(x_normalized[i] * 3) * np.sin(x_normalized[i] * 4)
            
        # High-frequency oscillation component
        oscillation = 0
        for i in range(self.dim):
            # Add high-frequency oscillations to increase complexity
            oscillation += np.sin(x_normalized[i] * 20) * np.cos(x_normalized[i] * 15)
            
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * modal + 0.2 * rbf + 0.1 * cross + \
                 0.1 * saddle + 0.05 * oscillation
        
        # Add a complex random perturbation to increase problem difficulty
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 12) * np.cos(x_normalized * 8))
        result += perturbation
        
        return result