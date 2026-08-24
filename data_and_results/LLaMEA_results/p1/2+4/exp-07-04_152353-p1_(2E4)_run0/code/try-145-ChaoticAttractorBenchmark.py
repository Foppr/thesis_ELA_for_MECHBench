import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Enhanced chaotic component with multiple logistic map interactions
        chaotic = 0
        for i in range(self.dim):
            # Multi-parameter chaotic map with varying coefficients
            param1 = 3.9 + 0.2 * np.sin(i * 1.1)
            param2 = 2.3 + 0.3 * np.cos(i * 0.7)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param1 * np.sin(x_normalized[i] * param2))
        
        # Multi-scale nested attractor regions with fractional exponents
        attractor = 0
        for i in range(self.dim):
            # Multiple attraction points with varying influence scales
            region1 = np.abs(x_normalized[i] - np.sin(i * 0.5))**1.9
            region2 = np.abs(x_normalized[i] + np.cos(i * 0.8))**2.1
            region3 = np.abs(x_normalized[i] - np.tan(i * 0.4))**1.3
            attractor += region1 + region2 + region3
            
        # Fractional smoothness component with dynamic exponents
        smoothness = 0
        for i in range(self.dim):
            # Variable exponent based on position and dimension
            exponent = 1.9 + 0.5 * np.sin(i * 0.8 + x_normalized[i])
            smoothness += np.abs(x_normalized[i])**exponent
            
        # Discontinuous gradient regions with multi-frequency discontinuities
        discontinuous = 0
        for i in range(self.dim):
            # Multiple discontinuity patterns with different frequencies
            discontinuous += np.abs(np.floor(x_normalized[i] * 8) - x_normalized[i] * 8) + \
                            np.abs(np.floor(x_normalized[i] * 4) - x_normalized[i] * 4) + \
                            np.abs(np.floor(x_normalized[i] * 13) - x_normalized[i] * 13)
            
        # Combined multi-component landscape
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Enhanced perturbation term with multi-frequency sine-cosine interactions
        perturbation = 0.05 * np.sum(np.sin(x_normalized * 13) * np.cos(x_normalized * 8) * np.sin(x_normalized * 5))
        result += perturbation
        
        # Add a global scaling factor to increase problem difficulty
        result *= (1.0 + 0.1 * np.sum(np.sin(x_normalized * 17)))
        
        return result