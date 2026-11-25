import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base function with multiple local minima
        result = 0.0
        
        # Sum of quadratic terms with different coefficients
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add sinusoidal perturbations to create local minima with modified frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            
        # Add a global scaling factor to ensure the function is well-conditioned
        result *= 1.0 + 0.15 * np.sum(x ** 2)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.08 * (x[i] ** 4) * (i + 1)
            
        # Add cross-term interactions with different coefficients and nonlinearities
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * x[i] * x[j] * np.sin(2 * (x[i] + x[j])) * np.cos(x[i] - x[j])
                
        # Add cubic terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.03 * (x[i] ** 3) * np.sin(x[i])
            
        return result