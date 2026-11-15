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
            param = 3.9 + 0.05 * np.sin(i * 1.3)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Nested attractor regions with different scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with different attraction points
            region = np.abs(x_normalized[i] - np.sin(i * 0.7)) + np.abs(x_normalized[i] + np.cos(i * 0.4))
            attractor += region**3.0
            
        # Non-smooth component with absolute value and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying step sizes
            step_size = 0.15 + 0.03 * np.sin(i * 0.8)
            smoothness += np.abs(x_normalized[i])**(1.7 + 0.3 * np.cos(i * 1.2))
            
        # Discontinuous gradient regions using sign and floor functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 4) - x_normalized[i] * 4)
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.3 * chaotic + 0.15 * attractor + 0.2 * smoothness + 0.1 * discontinuous
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6))
        result += perturbation
        
        return result