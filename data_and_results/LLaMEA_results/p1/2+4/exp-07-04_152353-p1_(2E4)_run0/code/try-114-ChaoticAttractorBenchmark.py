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
            
        # Enhanced fractal dimensionality with dynamic coupling
        dynamic_fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_fractal += np.sin(x_normalized[i] * x_normalized[j] * 15) * \
                                  np.cos(x_normalized[i] * 2 + x_normalized[j] * 3) * \
                                  np.exp(-np.abs(x_normalized[i] - x_normalized[j]) * 2)
        
        # Dynamic coupling terms between dimensions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x_normalized[i] * x_normalized[j] * 7.5) * \
                           np.cos(x_normalized[i] + x_normalized[j] * 1.3) * \
                           np.exp(-np.abs(x_normalized[i] - x_normalized[j]) * 0.5)
        
        # Increased parameter sensitivity through dynamic exponents
        sensitivity = 0
        for i in range(self.dim):
            # Dynamic exponent based on neighbor values
            neighbor_sum = np.sum(x_normalized[max(0, i-2):min(self.dim, i+3)])
            dynamic_exp = 1.5 + 0.8 * np.sin(neighbor_sum * 2.3 + i * 0.7)
            sensitivity += np.abs(x_normalized[i])**dynamic_exp
            
        # Combine all components with different weights
        result = 0.25 * f1 + 0.22 * chaotic + 0.15 * attractor + 0.12 * smoothness + \
                 0.08 * discontinuous + 0.05 * interaction + 0.13 * fractal + \
                 0.03 * dynamic_fractal + 0.04 * coupling + 0.03 * sensitivity
        
        # Add a complex random perturbation to increase problem difficulty
        perturbation = 0.03 * np.sum(np.sin(x_normalized * 9) * np.cos(x_normalized * 6) * np.tan(x_normalized * 2))
        result += perturbation
        
        return result