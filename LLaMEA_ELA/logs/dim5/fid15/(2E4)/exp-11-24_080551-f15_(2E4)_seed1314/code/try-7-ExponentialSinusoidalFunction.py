import numpy as np

class ExponentialSinusoidalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term centered at origin
        result = np.sum(x**2)
        
        # Exponentially decaying sinusoidal perturbations
        for i in range(self.dim):
            # Each dimension has a sinusoidal component with amplitude decaying as 1/(i+1)
            amplitude = 1.0 / (i + 1)
            result += amplitude * np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * x[i])
            
        # Cross-dimensional interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength decreases exponentially with dimension distance
                decay_factor = np.exp(-0.1 * (j - i))
                result += decay_factor * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Additional exponential decay term for global convergence
        result += 0.5 * np.exp(-0.5 * np.sum(x**2))
        
        return result