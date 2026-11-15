import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with modified logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            # Use modified parameter for more chaotic behavior
            param = 3.9 + 0.05 * np.sin(i * 0.7)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Nested attractor regions with enhanced complexity
        attractor = 0
        for i in range(self.dim):
            # Create more complex nested regions with multiple attraction points
            region = (np.abs(x_normalized[i] - np.sin(i * 0.3)) + 
                     np.abs(x_normalized[i] + np.cos(i * 0.4)) + 
                     0.5 * np.abs(x_normalized[i] - np.tan(i * 0.2)))
            attractor += region**3.0
            
        # Enhanced non-smooth component with varying fractional exponents
        smoothness = 0
        for i in range(self.dim):
            # Use varying fractional powers to increase non-smoothness
            power = 1.2 + 0.8 * np.sin(i * 0.6)
            smoothness += np.abs(x_normalized[i])**power
            
        # Discontinuous gradient regions with enhanced step functions
        discontinuous = 0
        for i in range(self.dim):
            # Create more frequent discontinuities with multiple step functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                           0.3 * np.abs(np.ceil(x_normalized[i] * 4) - x_normalized[i] * 4)
            
        # Additional sine-wave interference to increase complexity
        interference = 0
        for i in range(self.dim):
            interference += np.sin(x_normalized[i] * 10 + i) * np.cos(x_normalized[i] * 7 + i)
            
        # Combine all components with optimized weights
        result = 0.25 * f1 + 0.3 * chaotic + 0.25 * attractor + 0.15 * smoothness + 0.05 * discontinuous + 0.05 * interference
        
        # Add controlled perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 9) * np.cos(x_normalized * 4))
        result += perturbation
        
        return result