import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.5)**2 + (x[i] + 1.5)**2 + 0.02 * x[i]**4
        
        # Exponentially increasing interaction terms with modified scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use stronger exponential scaling for interaction strength
                interaction_strength = np.exp(0.7 * (i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Add saddle point structure with sinusoidal modulation
        for i in range(self.dim):
            result += 0.6 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i])
        
        # Add a complex global minimum with high curvature
        result += 0.0015 * np.sum(x**2) + 0.0002 * np.sum(x**6)
        
        # Add a periodic component to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(3.5 * x[i]) * np.cos(2.5 * x[i])
        result += 0.12 * periodic_term
        
        # Shift global minimum to encourage better convergence
        result += 0.5 * np.sum((x - 0.5)**2)
        
        return result