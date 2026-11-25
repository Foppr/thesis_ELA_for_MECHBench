import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic base
        result = np.sum(x**2)
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.4 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.2 * np.sin(5 * x[i])**2
            
        # Add interaction terms between dimensions with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 * (1 + 0.5 * np.abs(x[i]) * np.abs(x[j]))
                result += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add polynomial interaction terms with higher order
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.05 * x[i]**6
            
        # Add cross-dimensional polynomial terms with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * (x[i]**3) * (x[j]**2) + 0.04 * (x[i]**2) * (x[j]**4)
                
        # Add Gaussian perturbations with multiple peaks
        for i in range(self.dim):
            result += 0.15 * np.exp(-0.5 * ((x[i] - 1.8) / 0.3)**2) + \
                      0.1 * np.exp(-0.5 * ((x[i] + 2.2) / 0.25)**2) + \
                      0.08 * np.exp(-0.5 * ((x[i] - 0.5) / 0.4)**2)
            
        # Add higher-order cross-dimensional terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.02 * x[i]**2 * x[j] * x[k] + 0.01 * x[i] * x[j]**3 * x[k]
                    
        # Add a small noise term to further increase landscape complexity
        noise = 0.01 * np.sum(np.sin(15 * x))
        result += noise
        
        return result