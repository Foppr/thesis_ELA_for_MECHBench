import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with enhanced logistic map behavior
        chaotic = 0
        for i in range(self.dim):
            # Enhanced chaotic dynamics with fractional exponents
            param = 3.9 + 0.05 * np.sin(i * 1.3)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)**1.3
            
        # Nested attractor regions with sine-cosine interactions
        attractor = 0
        for i in range(self.dim):
            # Create nested regions with sine-cosine attraction points
            attractor += (np.abs(x_normalized[i] - np.sin(i * 0.7))**1.8 + 
                         np.abs(x_normalized[i] + np.cos(i * 0.4))**1.8)
            
        # Non-smooth component with varying fractional exponents
        smoothness = 0
        for i in range(self.dim):
            # Add non-smooth elements with varying fractional powers
            power = 1.2 + 0.6 * np.sin(i * 0.8)
            smoothness += np.abs(x_normalized[i])**power
            
        # Discontinuous gradient regions with enhanced step functions
        discontinuous = 0
        for i in range(self.dim):
            # Create stronger discontinuities with multiple step functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 5) - x_normalized[i] * 5) + \
                           0.3 * np.abs(np.ceil(x_normalized[i] * 4) - x_normalized[i] * 4)
            
        # Combine all components with optimized weights
        result = 0.25 * f1 + 0.3 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Add multi-scale perturbation to increase problem difficulty
        perturbation = 0.015 * np.sum(np.sin(x_normalized * 8) * np.cos(x_normalized * 6) * np.tan(x_normalized * 3))
        result += perturbation
        
        return result