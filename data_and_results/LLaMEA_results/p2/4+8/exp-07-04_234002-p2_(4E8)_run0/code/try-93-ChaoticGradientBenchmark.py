import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with sine and cosine interactions
        for i in range(self.dim):
            result += 0.5 * np.sin(x[i]) * np.cos(x[i]) + 0.3 * np.sin(3.0 * x[i]) + 0.1 * np.cos(5.0 * x[i])
            
        # Add quadratic and quartic terms with varying coefficients
        for i in range(self.dim):
            result += 0.2 * x[i]**2 + 0.05 * x[i]**4
            
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                result += 0.1 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] - 0.3 * x[j]) + 0.02 * x[i] * x[j]
                
        # Dynamic scaling factor based on position
        scale_factor = 1.0 + 0.3 * np.sum(np.sin(0.5 * x)**2)
        
        # Add chaotic perturbation using logistic map-like behavior
        chaotic_perturbation = 1.0
        for i in range(self.dim):
            chaotic_perturbation += 0.03 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.01 * np.sin(15.0 * x[i])
            
        result = result * scale_factor * chaotic_perturbation
        
        # Add a small noise term to increase robustness testing
        result += 0.001 * np.sum(np.random.rand(self.dim) * x**2)
        
        return result