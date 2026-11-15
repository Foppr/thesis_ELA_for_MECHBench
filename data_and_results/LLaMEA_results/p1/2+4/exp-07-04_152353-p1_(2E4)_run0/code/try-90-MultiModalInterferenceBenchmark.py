import numpy as np

class MultiModalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base polynomial term
        f1 = np.sum(x_normalized**4)
        
        # Sinusoidal interference pattern
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin(x_normalized[i] * x_normalized[j] * np.pi) * np.cos(x_normalized[i] + x_normalized[j])
        
        # Multi-modal component with polynomial mixing
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using polynomial combinations
            multimodal += (x_normalized[i]**6 + 0.5 * x_normalized[i]**4 + 0.1 * x_normalized[i]**2)
            
        # Gradient variation term with exponential scaling
        gradient_var = 0
        for i in range(self.dim):
            # Exponential scaling to create varying gradient magnitudes
            gradient_var += np.exp(np.abs(x_normalized[i]) * 2) * np.sin(x_normalized[i] * 3)
            
        # Cross-term interactions with fractional powers
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional power interaction to introduce non-smoothness
                cross_terms += (x_normalized[i]**1.5 + x_normalized[j]**1.7) * np.cos(x_normalized[i] * x_normalized[j])
        
        # Combine all components with different weights
        result = 0.3 * f1 + 0.25 * interference + 0.2 * multimodal + 0.15 * gradient_var + 0.1 * cross_terms
        
        # Add a small random perturbation to increase problem difficulty
        perturbation = 0.01 * np.sum(np.sin(x_normalized * 10) * np.cos(x_normalized * 8))
        result += perturbation
        
        return result