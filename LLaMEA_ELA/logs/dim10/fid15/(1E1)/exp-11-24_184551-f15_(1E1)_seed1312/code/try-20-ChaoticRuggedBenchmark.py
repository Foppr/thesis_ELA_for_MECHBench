import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add sinusoidal oscillations in all dimensions
        for i in range(self.dim):
            result += np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i])
        
        # Add exponential barrier terms to create ruggedness
        for i in range(self.dim):
            # Create sharp barriers at specific points
            barrier_term = 0.0
            for j in range(-2, 3):
                barrier_term += np.exp(-10 * (x[i] - j)**2) + 0.5 * np.exp(-5 * (x[i] - j)**2)
            result += barrier_term
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        result += interaction
        
        # Add a global scaling factor to control the difficulty
        result *= 0.5
        
        # Add small noise to make it non-trivial
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + noise