import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with multiple logistic map-like behaviors
        chaotic = 0
        for i in range(self.dim):
            # Multiple chaotic parameters with temporal modulation
            param1 = 3.9 + 0.2 * np.sin(i * 0.3)
            param2 = 3.7 + 0.15 * np.cos(i * 0.4)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param1) + \
                      np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param2)
        
        # Nested attractor regions with fractal-like scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with fractal-like attraction points
            region1 = np.abs(x_normalized[i] - np.sin(i * 0.5)) + np.abs(x_normalized[i] + np.cos(i * 0.3))
            region2 = np.abs(x_normalized[i] - np.sin(i * 0.7)) + np.abs(x_normalized[i] + np.cos(i * 0.2))
            attractor += (region1**2.7 + region2**1.8)
            
        # Non-smooth component with varying fractional exponents and multi-scale effects
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents and multi-scale modulation
            exponent1 = 1.2 + 0.5 * np.sin(i * 0.6)
            exponent2 = 1.8 + 0.3 * np.cos(i * 0.8)
            smoothness += np.abs(x_normalized[i])**exponent1 + np.abs(x_normalized[i])**exponent2
            
        # Discontinuous gradient regions using multiple discontinuity functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with multiple floor and sign functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                           np.abs(np.ceil(x_normalized[i] * 3) - x_normalized[i] * 3)
            
        # Additional multi-scale sine-wave interaction terms
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                interaction += np.sin(x_normalized[i] * x_normalized[j] * 3.0) * \
                              np.cos(x_normalized[i] + x_normalized[j]) * \
                              np.sin((x_normalized[i] - x_normalized[j]) * 2.0)
        
        # Multi-scale fractal-like component
        fractal = 0
        for i in range(self.dim):
            fractal += np.abs(np.sin(x_normalized[i] * 10))**1.5 + \
                      np.abs(np.cos(x_normalized[i] * 7))**2.2
        
        # Combine all components with different weights
        result = 0.25 * f1 + 0.20 * chaotic + 0.15 * attractor + 0.15 * smoothness + \
                0.10 * discontinuous + 0.08 * interaction + 0.07 * fractal
        
        # Add a complex random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6) * np.sin(x_normalized * 4))
        result += perturbation
        
        return result