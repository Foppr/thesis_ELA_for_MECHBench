import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with fractional-order dynamics and multiple attractors
        chaotic = 0
        for i in range(self.dim):
            # Fractional exponent chaotic term with multiple attractors
            param1 = 3.8 + 0.2 * np.sin(i * 0.7)
            param2 = 3.5 + 0.1 * np.cos(i * 0.9)
            chaotic += np.abs(x_normalized[i]**1.7 * (1 - x_normalized[i]**2) * param1) + \
                      np.abs(x_normalized[i]**2.3 * (1 - x_normalized[i]**1.5) * param2)
        
        # Multi-modal nested attractor regions with varying scales and rotations
        attractor = 0
        for i in range(self.dim):
            # Create multi-modal regions with different attraction points and scales
            scale = 1.0 + 0.5 * np.sin(i * 0.3)
            region1 = np.abs(x_normalized[i] - np.sin(i * 0.5))**2.8
            region2 = np.abs(x_normalized[i] + np.cos(i * 0.3))**3.2
            region3 = np.abs(x_normalized[i] - np.tan(i * 0.2))**2.1
            attractor += scale * (region1 + region2 + region3)
            
        # Non-smooth component with fractional exponents and multi-scale step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents and step sizes
            step_size = 0.05 + 0.03 * np.sin(i * 0.8)
            smoothness += np.abs(x_normalized[i])**(1.3 + 0.4 * np.cos(i * 0.6)) + \
                         np.abs(x_normalized[i] - step_size)**(1.8 + 0.2 * np.sin(i * 0.4))
            
        # Discontinuous gradient regions using multiple discontinuity functions
        discontinuous = 0
        for i in range(self.dim):
            # Create multiple discontinuities with different patterns
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                           np.abs(np.ceil(x_normalized[i] * 3) - x_normalized[i] * 3) + \
                           np.abs(np.sin(x_normalized[i] * 4) - x_normalized[i])
            
        # Multi-modal sine-wave interaction component
        sine_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_interaction += np.sin(x_normalized[i] * x_normalized[j] * 2) * \
                                  np.cos(x_normalized[i] * 0.5 + x_normalized[j] * 0.3)
                
        # Combine all components with different weights
        result = 0.25 * f1 + 0.3 * chaotic + 0.25 * attractor + 0.15 * smoothness + 0.05 * discontinuous + 0.05 * sine_interaction
        
        # Add a highly complex perturbation with multiple frequencies
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 7) * np.tan(x_normalized * 3))
        result += perturbation
        
        return result