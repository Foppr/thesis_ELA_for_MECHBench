import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with logistic map-like behavior and fractional dynamics
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with varying parameter and fractional exponent
            param = 3.9 + 0.2 * np.sin(i * 0.3)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**1.7) * param)**1.3
            
        # Nested attractor regions with different scaling and additional sine components
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with different attraction points and sine modulation
            region = np.abs(x_normalized[i] - np.sin(i * 0.4)) + np.abs(x_normalized[i] + np.cos(i * 0.6))
            attractor += region**3.2
            
        # Non-smooth component with modified absolute value and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents and additional sine modulation
            exponent = 1.5 + 0.6 * np.sin(i * 0.8)
            smoothness += np.abs(x_normalized[i])**exponent + 0.1 * np.sin(x_normalized[i] * 10)
            
        # Discontinuous gradient regions using sign and floor functions with additional noise
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions and additional noise
            discontinuous += np.abs(np.floor(x_normalized[i] * 6) - x_normalized[i] * 6) + 0.05 * np.sin(x_normalized[i] * 15)
            
        # Additional sine-wave interaction terms to increase complexity with higher frequency components
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_normalized[i] * x_normalized[j] * 3.0) * np.cos(x_normalized[i] + x_normalized[j]) * np.exp(-np.abs(x_normalized[i] - x_normalized[j]))
        
        # Novel discontinuity pattern with piecewise linear functions
        piecewise = 0
        for i in range(self.dim):
            # Piecewise linear function with random breakpoints
            piecewise += np.abs(x_normalized[i] - np.floor(x_normalized[i] * 3) / 3) * (1 + 0.3 * np.sin(i * 2.1))
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.20 * chaotic + 0.15 * attractor + 0.15 * smoothness + 0.10 * discontinuous + 0.08 * interaction + 0.07 * piecewise
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6))
        result += perturbation
        
        return result