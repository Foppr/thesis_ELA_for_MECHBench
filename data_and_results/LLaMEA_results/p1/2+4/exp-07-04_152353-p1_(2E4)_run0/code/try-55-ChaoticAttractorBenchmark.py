import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with logistic map-like behavior and multiple parameters
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with varying parameter and chaotic feedback
            param = 3.9 + 0.2 * np.sin(i * 1.3) + 0.1 * np.cos(i * 0.7)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param + 0.05 * np.sin(x_normalized[i] * 10))
        
        # Nested attractor regions with different scaling and fractal-like behavior
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with different attraction points and fractal scaling
            region = np.abs(x_normalized[i] - np.sin(i * 0.5)) + np.abs(x_normalized[i] + np.cos(i * 0.3))
            attractor += region**(2.7 + 0.3 * np.sin(i * 0.9))
            
        # Non-smooth component with modified absolute value and step functions with varying exponents
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents and chaotic modulation
            exponent = 1.2 + 0.6 * np.sin(i * 0.7) + 0.1 * np.cos(i * 1.1)
            smoothness += np.abs(x_normalized[i])**exponent + 0.03 * np.sin(x_normalized[i] * 15)
            
        # Discontinuous gradient regions using sign and floor functions with multiple scales
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions at multiple scales
            discontinuous += np.abs(np.floor(x_normalized[i] * 6) - x_normalized[i] * 6) + \
                            0.02 * np.abs(np.floor(x_normalized[i] * 3) - x_normalized[i] * 3)
            
        # Additional sine-wave interaction terms with varying frequencies and amplitudes
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add complex interaction terms with multiple sine and cosine components
                interaction += (np.sin(x_normalized[i] * x_normalized[j] * 3.0) * 
                               np.cos(x_normalized[i] + x_normalized[j]) * 
                               np.sin(x_normalized[i] - x_normalized[j] * 0.5) * 
                               0.5)
        
        # Fractal-like component with recursive-like behavior
        fractal = 0
        for i in range(self.dim):
            # Add fractal-like behavior with recursive-like scaling
            fractal += np.abs(np.sin(x_normalized[i] * 20) * np.cos(x_normalized[i] * 15)) + \
                      0.01 * np.sin(x_normalized[i] * 50)
        
        # Combine all components with different weights and chaotic modulation
        result = (0.25 * f1 + 
                 0.20 * chaotic + 
                 0.15 * attractor + 
                 0.15 * smoothness + 
                 0.08 * discontinuous + 
                 0.05 * interaction + 
                 0.02 * fractal)
        
        # Add a highly complex random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 12) * np.cos(x_normalized * 8) * np.sin(x_normalized * 15))
        result += perturbation
        
        return result