import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with variable exponents and interaction
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Chaotic sinusoidal perturbations with coupled interactions
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[(i + 1) % self.dim]) + 
                       0.5 * np.sin(7.0 * x[i]) * np.cos(3.0 * x[(i + 2) % self.dim]) +
                       0.3 * np.sin(5.0 * x[i]) * np.sin(2.0 * x[(i + 3) % self.dim]))
            
        # Novel chaotic component based on logistic map
        logistic = 0.0
        r = 3.9  # Chaotic parameter
        for i in range(self.dim):
            if i == 0:
                logistic += np.sin(r * x[i] * (1 - x[i]))
            else:
                logistic += np.sin(r * x[i] * (1 - x[i-1]))
        
        # Adaptive weight based on dimensionality
        adaptive_weight = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Modified Manhattan term with chaotic modulation
        manhattan = np.sum(np.abs(x)) * (1.0 + 0.05 * np.sin(2.0 * np.sum(x)) + 0.02 * logistic)
        
        # Add a novel interaction term between all dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) * (1.0 + 0.1 * np.cos(np.sum(x)))
                
        return adaptive_weight * polynomial + 0.3 * chaotic + 0.05 * manhattan + 0.1 * interaction