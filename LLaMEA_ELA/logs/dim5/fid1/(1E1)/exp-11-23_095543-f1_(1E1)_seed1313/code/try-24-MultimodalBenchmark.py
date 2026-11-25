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
            result += 0.4 * np.sin(8 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            
        # Add a global scaling factor to ensure the function is well-conditioned
        result *= 1.0 + 0.15 * np.sum(x ** 2)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.12 * (x[i] ** 4) * (i + 1)
            
        # Add cross-term interactions with modified interaction strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.06 * x[i] * x[j] * np.sin(x[i] + x[j]) * np.cos(2 * x[i] - x[j])
                
        # Add additional high-frequency sinusoidal components with different interaction patterns
        for i in range(self.dim):
            result += 0.18 * np.sin(12 * x[i]) * np.cos(5 * x[(i + 2) % self.dim]) * np.sin(4 * x[(i + 3) % self.dim])
            
        # Add a fifth-order polynomial component with modified coefficients
        for i in range(self.dim):
            result += 0.02 * (x[i] ** 5) * (i + 1)
            
        # Add interaction terms between all dimensions with different weight
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += 0.015 * x[i] * x[j] * np.exp(-0.08 * (x[i] - x[j])**2)
                    
        # Add a modified cubic term to improve conditioning
        for i in range(self.dim):
            result += 0.08 * (x[i] ** 3) * (i + 1)
            
        return result