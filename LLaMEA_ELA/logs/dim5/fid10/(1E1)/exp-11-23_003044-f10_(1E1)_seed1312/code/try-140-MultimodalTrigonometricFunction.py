import numpy as np

class MultimodalTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        
        # Polynomial base terms with sinusoidal modulation
        for i in range(self.dim):
            # Quadratic term modulated by sine
            result += (x[i] ** 2) * (1 + 0.3 * np.sin(5 * x[i]))
            
            # Add higher-order polynomial with cosine modulation
            result += 0.5 * (x[i] ** 3) * np.cos(2 * x[i])
            
        # Interaction terms between dimensions creating complex landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross terms with trigonometric modulation
                result += 0.3 * np.sin(x[i]) * np.cos(x[j]) * (x[i] + x[j])**2
                
        # Global conditioning factor to control problem difficulty
        condition_factor = 1 + 0.2 * np.sum(np.abs(x))
        
        # Add a periodic component that creates multiple minima
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x[i] / 2.5) * np.cos(3 * np.pi * x[i] / 2.5)
        
        result = result * condition_factor + 0.5 * periodic_term
        
        return result