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
            # Increased chaos with higher parameter sensitivity
            param = 3.8 + 0.4 * np.sin(i * 0.5 + np.pi/4)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Enhanced nested attractor regions with exponential scaling
        attractor = 0
        for i in range(self.dim):
            # Exponential attraction with varying scales
            scale = 2.0 + 1.5 * np.cos(i * 0.2)
            attractor += (np.abs(x_normalized[i] - np.sin(i * 0.4))**scale + 
                         np.abs(x_normalized[i] + np.cos(i * 0.3))**scale)
        
        # Modified non-smooth component with fractional exponents
        smoothness = 0
        for i in range(self.dim):
            # Fractional exponents to increase gradient discontinuity
            exponent = 1.5 + 0.8 * np.sin(i * 0.6)
            smoothness += np.abs(x_normalized[i])**(exponent)
            
        # Enhanced discontinuous gradient regions
        discontinuous = 0
        for i in range(self.dim):
            # More aggressive discontinuity pattern
            discontinuous += np.abs(np.floor(x_normalized[i] * 7) - x_normalized[i] * 7)**1.3
            
        # Combine all components with adjusted weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Enhanced perturbation term with higher frequency components
        perturbation = 0.05 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 6))
        result += perturbation
        
        return result