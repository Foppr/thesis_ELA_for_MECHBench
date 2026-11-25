import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Radial basin term - pulls solutions toward origin
        radius = np.sqrt(np.sum(x**2))
        result += 0.5 * radius**2
        
        # Sinusoidal oscillations in each dimension
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-terms creating non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Additional chaotic component with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-0.1 * abs(x[i])) * np.sin(5.0 * x[i]**2)
        result += chaotic_term
        
        # Add a small quadratic penalty to encourage staying within bounds
        bound_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                bound_penalty += 10.0 * (abs(x[i]) - 4.5)**2
        result += bound_penalty
        
        return result