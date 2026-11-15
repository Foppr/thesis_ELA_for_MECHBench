import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial chaos components with dynamic exponents
        for i in range(self.dim):
            # Dynamic exponent based on position
            exp = 2.0 + 1.5 * np.sin(x[i] * 0.5)
            result += 0.5 * x[i]**exp + 0.1 * x[i]**4 + 0.02 * x[i]**6
            
        # Chaotic feedback loops with recursive interactions
        for i in range(self.dim):
            feedback = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling with sine and cosine interactions
                    feedback += 0.3 * np.sin(x[i] * x[j]) * np.cos(0.7 * x[i] + 0.3 * x[j])
            result += 0.2 * feedback**2
            
        # Dynamic dimension coupling with time-delayed effects
        coupling_strength = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling_strength += 0.1 * np.sin(x[i] + x[j]) * np.cos(1.3 * x[i] - 0.8 * x[j])
        result += coupling_strength * (1.0 + 0.2 * np.sum(x**2))
        
        # Add discontinuous regions using step functions and fractal-like behavior
        discontinuity = 0.0
        for i in range(self.dim):
            # Create discontinuous behavior using sign and floor functions
            discontinuity += 0.05 * np.abs(x[i] - np.floor(x[i] + 0.5)) * np.sin(10.0 * x[i])
            
        # Add chaotic perturbations with varying frequencies
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += 0.03 * np.sin(23.0 * x[i]) * np.cos(17.0 * x[i]) + \
                                  0.02 * np.sin(31.0 * x[i]**2) * np.cos(19.0 * x[i]**2)
            
        result = result + discontinuity + chaotic_perturbation
        
        # Add global conditioning with variable scaling
        scaling_factor = 1.0 + 0.1 * np.sum(np.abs(x)) + 0.05 * np.sum(x**3)
        result = result * scaling_factor
        
        return result