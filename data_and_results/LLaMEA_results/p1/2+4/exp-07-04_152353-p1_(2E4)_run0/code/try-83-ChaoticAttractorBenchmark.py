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
            
        # Non-smooth component with modified absolute value and step functions
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional exponents
            exponent = 1.3 + 0.4 * np.sin(i * 0.7)
            smoothness += np.abs(x_normalized[i])**exponent
            
        # Discontinuous gradient regions using sign and floor functions
        discontinuous = 0
        for i in range(self.dim):
            # Create discontinuities with floor and sign functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 4) - x_normalized[i] * 4)
            
        # Additional sine-wave interaction terms to increase complexity
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_normalized[i] * x_normalized[j] * 2.5) * np.cos(x_normalized[i] + x_normalized[j])
        
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.18 * attractor + 0.17 * smoothness + 0.08 * discontinuous + 0.02 * interaction
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 7) * np.cos(x_normalized * 5))
        result += perturbation
        
        # Introduce enhanced chaotic behavior through modified fractional exponents
        fractional_chaos = 0
        for i in range(self.dim):
            fractional_chaos += np.abs(x_normalized[i])**1.7 * np.sin(x_normalized[i] * 3.14)
        result += 0.05 * fractional_chaos
        
        # Add a multi-modal component to increase optimization challenge
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(x_normalized[i] * 10) * np.cos(x_normalized[i] * 5)
        result += 0.03 * multimodal
        
        return result