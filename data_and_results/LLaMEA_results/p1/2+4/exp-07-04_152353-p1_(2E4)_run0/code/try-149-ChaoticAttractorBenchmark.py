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
            # Increased chaos with dynamic parameter
            param = 3.8 + 0.3 * np.sin(i * 0.5 + np.pi/4)
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]**2) * param)
        
        # Enhanced nested attractor regions with exponential scaling
        attractor = 0
        for i in range(self.dim):
            # Exponential attraction with varying exponents
            region = np.abs(x_normalized[i] - np.sin(i * 0.4))**2.5 + np.abs(x_normalized[i] + np.cos(i * 0.5))**1.5
            attractor += region
            
        # Improved non-smooth component with fractional exponents
        smoothness = 0
        for i in range(self.dim):
            # Fractional smoothness with varying exponents
            exponent = 1.8 + 0.4 * np.sin(i * 0.7)
            smoothness += np.abs(x_normalized[i])**exponent
            
        # Enhanced discontinuous gradient regions
        discontinuous = 0
        for i in range(self.dim):
            # More frequent discontinuities with modified floor functions
            discontinuous += np.abs(np.floor(x_normalized[i] * 7.5) - x_normalized[i] * 7.5)**1.2
            
        # Combine all components with adjusted weights
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Enhanced perturbation term with higher frequency interactions
        perturbation = 0.05 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 6))
        result += perturbation
        
        return result