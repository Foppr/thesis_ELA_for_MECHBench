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
            # Modified logistic map with different parameter range and added noise
            param = 3.8 + 0.3 * np.sin(i * 0.9) + 0.05 * np.random.randn()
            chaotic += np.abs(x_normalized[i] * (1 - x_normalized[i]) * param)
        
        # Modified nested attractor regions with different scaling and fractional exponents
        attractor = 0
        for i in range(self.dim):
            # Modified attraction points and fractional exponents
            region = (np.abs(x_normalized[i] - np.sin(i * 0.3))**1.5 + 
                     np.abs(x_normalized[i] + np.cos(i * 0.4))**1.7)
            attractor += region
            
        # Modified non-smooth component with different exponents and additional sine modulation
        smoothness = 0
        for i in range(self.dim):
            # Changed step sizes, exponents, and added sine modulation
            step_size = 0.03 + 0.15 * np.sin(i * 0.8)
            smoothness += np.abs(x_normalized[i])**(2.5 + 0.4 * np.cos(i * 0.6) + 0.1 * np.sin(i * 1.2))
            
        # Discontinuous gradient regions with modified floor functions and additional chaos
        discontinuous = 0
        for i in range(self.dim):
            # Changed discontinuity pattern and added chaotic perturbation
            base_discontinuity = np.abs(np.floor(x_normalized[i] * 7) - x_normalized[i] * 7)
            chaotic_perturbation = 0.02 * np.sin(x_normalized[i] * 13)
            discontinuous += base_discontinuity + chaotic_perturbation
            
        # Combine all components with modified weights and added cross-terms
        result = 0.3 * f1 + 0.25 * chaotic + 0.2 * attractor + 0.15 * smoothness + 0.1 * discontinuous
        
        # Modified perturbation term with higher frequency components
        perturbation = 0.05 * np.sum(np.sin(x_normalized * 11) * np.cos(x_normalized * 6) * np.sin(x_normalized * 3))
        result += perturbation
        
        # Add a multi-modal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.abs(x_normalized[i] - np.sin(i * 0.5))**4 + \
                         np.abs(x_normalized[i] + np.cos(i * 0.7))**3 + \
                         0.1 * np.sin(x_normalized[i] * 15)
        result += 0.1 * multimodal
        
        return result