import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced chaotic component with fractional exponents and sine interactions
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with varying parameter and fractional exponent
            param = 3.9 + 0.05 * np.sin(i * 0.7)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**1.3) * param)**0.7
            
        # Modified nested attractor regions with exponential scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with exponential attraction points
            region = np.exp(np.abs(x_normalized[i] - np.sin(i * 0.4))) + np.exp(np.abs(x_normalized[i] + np.cos(i * 0.6)))
            attractor += region**1.8
            
        # Enhanced non-smooth component with varying fractional powers
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents
            power = 1.2 + 0.6 * np.sin(i * 0.3)
            smoothness += np.abs(x_normalized[i])**power
            
        # Improved discontinuous gradient regions using tanh and step functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with tanh and step functions for sharper gradients
            discontinuous += np.abs(np.tanh(x_normalized[i] * 4) - x_normalized[i] * 0.5)
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.3 * chaotic + 0.25 * attractor + 0.15 * smoothness + 0.05 * discontinuous
        
        # Add a more complex perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6) * np.tanh(x_normalized))
        result += perturbation
        
        return result