import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with varying parameter
            param = 3.8 + 0.1 * np.sin(i)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Nested attractor regions with different scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with different attraction points
            region = np.abs(x_normalized[i] - np.sin(i * 0.5)) + np.abs(x_normalized[i] + np.cos(i * 0.3))
            attractor += region**2.5
            
        # Non-smooth component with absolute value and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying step sizes
            step_size = 0.1 + 0.05 * np.sin(i)
            smoothness += np.abs(x_normalized[i])**(1.5 + 0.5 * np.cos(i))
            
        # Discontinuous gradient regions using sign and floor functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 3) - x_normalized[i] * 3)
            
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 7) * np.cos(x_normalized * 5))
        result += perturbation
        
        return result