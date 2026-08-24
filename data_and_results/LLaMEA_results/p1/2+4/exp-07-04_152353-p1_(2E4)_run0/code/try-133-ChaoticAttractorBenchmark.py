import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with logistic map-like behavior and time-varying parameters
        chaotic = 0
        for i in range(self.dim):
            # Logistic map inspired term with time-varying parameter
            param = 3.9 + 0.2 * np.sin(i * 0.3 + np.sum(x_normalized[:i+1]) if i > 0 else 0)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Nested attractor regions with fractal-like scaling
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with fractal-like attraction points
            region = np.abs(x_normalized[i] - np.sin(i * 0.7)) + np.abs(x_normalized[i] + np.cos(i * 0.4))
            attractor += region**(2.7 + 0.3 * np.sin(i * 0.5))
            
        # Non-smooth component with varying fractional exponents and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents and step functions
            exponent = 1.2 + 0.6 * np.sin(i * 0.8 + np.sum(x_normalized[:i+1]) if i > 0 else 0)
            smoothness += np.abs(x_normalized[i])**exponent
            
        # Discontinuous gradient regions using sign, floor, and ceiling functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions, plus ceiling for added complexity
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                            np.abs(np.ceil(x_normalized[i] * 3) - x_normalized[i] * 3)
            
        # Additional sine-wave interaction terms with higher frequency and amplitude
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_normalized[i] * x_normalized[j] * 3.2) * \
                              np.cos(x_normalized[i] + x_normalized[j]) * \
                              np.exp(-np.abs(x_normalized[i] - x_normalized[j]))
        
        # Multi-scale fractal component for increased complexity
        fractal = 0
        for i in range(self.dim):
            fractal += np.abs(np.sin(x_normalized[i] * 10) * np.cos(x_normalized[i] * 7)) ** 1.5
            
        # Hybrid fractal-chaotic component with dynamic modulation
        hybrid = 0
        for i in range(self.dim):
            # Dynamic modulation using multiple sine and cosine terms
            modulator = np.sin(x_normalized[i] * 15) * np.cos(x_normalized[i] * 12) * np.tan(x_normalized[i] * 8)
            hybrid += np.abs(modulator) ** (1.3 + 0.2 * np.sin(i * 0.6))
            
        # Dynamic parameter modulation for increased complexity
        dynamic = 0
        for i in range(self.dim):
            # Use dynamic parameters that depend on all previous dimensions
            dynamic_param = 2.5 + 1.5 * np.sin(np.sum(x_normalized[:i+1]) * 0.5)
            dynamic += np.abs(x_normalized[i])**dynamic_param
            
        # Combine all components with different weights
        result = 0.20 * f1 + 0.20 * chaotic + 0.14 * attractor + 0.10 * smoothness + \
                 0.07 * discontinuous + 0.06 * interaction + 0.11 * fractal + 0.08 * hybrid + 0.04 * dynamic
        
        # Add a complex random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 9) * np.cos(x_normalized * 6) * np.tan(x_normalized * 2))
        result += perturbation
        
        return result