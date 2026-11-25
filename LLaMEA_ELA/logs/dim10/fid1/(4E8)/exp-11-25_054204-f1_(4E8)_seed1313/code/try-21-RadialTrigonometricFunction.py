import numpy as np

class RadialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add radial basis functions with different centers and variances
        centers = np.linspace(-4, 4, 9)
        for i in range(9):
            for j in range(9):
                center_i = centers[i]
                center_j = centers[j]
                distance = np.sqrt((x[0] - center_i)**2 + (x[1] - center_j)**2)
                result += 0.5 * np.exp(-0.1 * distance**2) * np.sin(2 * np.pi * distance)
        
        # Add trigonometric perturbations in higher dimensions
        for i in range(self.dim):
            result += 0.3 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Add cross-dimensional interaction terms with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interactions for complexity control
                freq = (i + j + 1) * 0.5
                result += 0.2 * np.sin(freq * x[i]) * np.cos(freq * x[j])
                
        # Add polynomial terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**3
            
        return result