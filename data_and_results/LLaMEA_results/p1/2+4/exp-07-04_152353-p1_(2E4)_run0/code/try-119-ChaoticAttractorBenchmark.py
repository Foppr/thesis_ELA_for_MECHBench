import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Chaotic component with enhanced logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            # Increased chaos with parameter modulation
            param = 3.8 + 0.3 * np.sin(i * 0.9)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Enhanced nested attractor regions with polynomial scaling
        attractor = 0
        for i in range(self.dim):
            # Polynomial attraction with varying exponents
            region = (x_normalized[i] - np.sin(i * 0.4))**4 + (x_normalized[i] + np.cos(i * 0.5))**4
            attractor += region
            
        # Refined non-smooth component with exponential step sizes
        smoothness = 0
        for i in range(self.dim):
            # Exponential step sizes and modified exponents
            step_size = 0.02 * np.exp(i * 0.1)
            smoothness += np.abs(x_normalized[i])**(1.5 + 0.4 * np.sin(i * 0.7))
            
        # Enhanced discontinuous gradient regions with sine modulation
        discontinuous = 0
        for i in range(self.dim):
            # Sine-based discontinuity pattern
            discontinuous += np.abs(np.sin(x_normalized[i] * 7) - x_normalized[i] * 0.5)
            
        # Combine all components with adjusted weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Enhanced perturbation term with cross-dimensional coupling
        perturbation = 0.02 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 3) * np.sin(x_normalized * 8))
        result += perturbation
        
        return result