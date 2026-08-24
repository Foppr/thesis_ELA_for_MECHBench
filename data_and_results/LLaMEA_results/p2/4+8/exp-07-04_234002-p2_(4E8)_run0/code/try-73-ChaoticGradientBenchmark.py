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
        
        # Chaotic component with exponential growth and sinusoidal modulation
        for i in range(self.dim):
            # Base quadratic term with chaotic scaling factor
            base = 0.5 * x[i]**2
            chaotic_factor = 1.0 + 0.3 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            result += base * chaotic_factor
            
        # Add cross-dimensional coupling with varying interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear interaction with chaotic modulation
                interaction = np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) + 0.1 * x[i] * x[j]**2
                coupling_strength = 0.5 + 0.2 * np.sin(5.0 * (x[i] + x[j]))
                result += coupling_strength * interaction
                
        # Add saddle point structure with varying curvature
        for i in range(self.dim):
            # Create regions with different curvatures
            curvature = 1.0 + 0.5 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
            result += 0.2 * x[i]**4 * curvature
            
        # Add fractal-like perturbations for increased complexity
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += 0.05 * np.sin(20.0 * x[i]) * np.cos(13.0 * x[i]) + 0.02 * np.sin(30.0 * x[i])
            
        result += fractal_perturbation
        
        # Apply non-uniform scaling based on dimension
        scaling = 1.0
        for i in range(self.dim):
            scaling *= (1.0 + 0.1 * np.abs(x[i]))
        result *= scaling
        
        return result