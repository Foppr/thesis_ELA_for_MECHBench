import numpy as np

class MultimodalTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        
        # Base polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            # Quadratic term with sinusoidal perturbation
            result += xi**2 * (1 + 0.3 * np.sin(5 * xi))
            
            # Additional trigonometric components
            result += 0.5 * np.sin(2 * xi) * np.cos(3 * xi)
            result += 0.2 * np.sin(4 * xi)**2
            
        # Interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross terms creating complex interactions
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += 0.1 * np.sin(x[i] * x[j])
                
        # Add a global scaling factor based on input magnitude
        magnitude = np.sum(np.abs(x))
        result *= (1 + 0.2 * magnitude)
        
        # Ensure the function has a global minimum at the origin
        result += 10.0 * np.exp(-0.1 * magnitude)
        
        return result