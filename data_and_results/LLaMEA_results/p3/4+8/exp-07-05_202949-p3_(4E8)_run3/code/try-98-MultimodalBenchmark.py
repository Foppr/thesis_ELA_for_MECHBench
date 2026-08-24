import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales and additional polynomial components
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.5)**2 + (x[i] + 1.5)**2 + 0.02 * x[i]**4 + 0.005 * x[i]**6
        
        # Exponentially increasing interaction terms with stronger scaling and additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use stronger exponential scaling for interaction strength
                interaction_strength = np.exp(1.5 * (i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Add saddle point structure with enhanced sinusoidal modulation
        for i in range(self.dim):
            result += 0.9 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + 0.4 * np.sin(5.5 * x[i])
        
        # Add a complex global minimum with high curvature and additional polynomial terms
        result += 0.003 * np.sum(x**2) + 0.0007 * np.sum(x**6) + 0.0002 * np.sum(x**8)
        
        # Add a highly periodic component to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.5 * x[i]) * np.cos(3.5 * x[i]) + 0.6 * np.sin(6.5 * x[i])
        result += 0.2 * periodic_term
        
        # Shift global minimum to encourage better convergence with additional offset
        result += 0.8 * np.sum((x - 0.4)**2) + 0.06 * np.sum((x - 0.4)**4)
        
        # Add a noise-like component to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(11.0 * x[i]) * np.cos(8.0 * x[i])
        result += noise
        
        return result