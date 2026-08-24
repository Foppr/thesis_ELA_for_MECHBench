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
            # Modified logistic map with different parameter range and frequency
            param = 3.8 + 0.1 * np.sin(i * 1.1)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Modified nested attractor regions with different scaling and interaction
        attractor = 0
        for i in range(self.dim):
            # Modified attraction points with combined sine/cosine
            region = np.abs(x_normalized[i] - np.sin(i * 0.5)) + np.abs(x_normalized[i] + np.cos(i * 0.6))
            attractor += region**2.5
            
        # Modified non-smooth component with different exponents and interaction
        smoothness = 0
        for i in range(self.dim):
            # Changed step sizes and exponents with frequency modulation
            step_size = 0.03 + 0.08 * np.sin(i * 0.9)
            smoothness += np.abs(x_normalized[i])**(1.8 + 0.2 * np.cos(i * 0.7))
            
        # Discontinuous gradient regions with modified floor functions and interaction
        discontinuous = 0
        for i in range(self.dim):
            # Changed discontinuity pattern with interaction term
            discontinuous += np.abs(np.floor(x_normalized[i] * 7) - x_normalized[i] * 7) * np.cos(i * 0.4)
            
        # Combine all components with modified weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Modified perturbation term with different frequency
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 3))
        result += perturbation
        
        return result