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
            # Modified logistic map with different parameter range
            param = 3.8 + 0.1 * np.sin(i * 0.9)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Modified nested attractor regions with different scaling
        attractor = 0
        for i in range(self.dim):
            # Modified attraction points and exponents
            region = np.abs(x_normalized[i] - np.sin(i * 0.4)) + np.abs(x_normalized[i] + np.cos(i * 0.5))
            attractor += region**3.5
            
        # Modified non-smooth component with different exponents
        smoothness = 0
        for i in range(self.dim):
            # Changed step sizes and exponents
            step_size = 0.03 + 0.15 * np.sin(i * 0.7)
            smoothness += np.abs(x_normalized[i])**(2.5 + 0.2 * np.cos(i * 0.5))
            
        # Discontinuous gradient regions with modified floor functions
        discontinuous = 0
        for i in range(self.dim):
            # Changed discontinuity pattern
            discontinuous += np.abs(np.floor(x_normalized[i] * 7) - x_normalized[i] * 7)
            
        # Combine all components with modified weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.18 * attractor + 0.22 * smoothness + 0.05 * discontinuous
        
        # Modified perturbation term
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 3))
        result += perturbation
        
        return result