import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with sine-wave modulation
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with varying parameter
            param = 3.8 + 0.2 * np.sin(i * 0.7)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Nested attractor regions with coupled sine-wave scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with different attraction points using sine modulation
            region = np.abs(x_normalized[i] - np.sin(i * 0.4 + 1)) + np.abs(x_normalized[i] + np.cos(i * 0.3 + 2))
            attractor += region**(2.0 + 0.3 * np.sin(i * 0.5))
            
        # Non-smooth component with coupled power and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying step sizes and sine coupling
            step_size = 0.15 + 0.08 * np.sin(i * 0.6)
            smoothness += np.abs(x_normalized[i])**(1.3 + 0.4 * np.cos(i * 0.4))
            
        # Discontinuous gradient regions using sign and floor functions with sine modulation
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions, modulated by sine
            mod = 1 + 0.2 * np.sin(i * 0.3)
            discontinuous += np.abs(np.floor(x_normalized[i] * 4 * mod) - x_normalized[i] * 4 * mod)
            
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Add a small random perturbation to increase problem difficulty with sine coupling
        perturbation = 0.015 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 4) * np.sin(x_normalized * 2))
        result += perturbation
        
        return result