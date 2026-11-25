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
            
        # Add sinusoidal perturbations to create local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            
        # Add a global scaling factor to ensure the function is well-conditioned
        result *= 1.0 + 0.3 * np.sum(x ** 2)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.18 * (x[i] ** 4) * (i + 1)
            
        # Add cross-term interactions to increase landscape complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * x[i] * x[j] * np.sin(x[i] + x[j]) * np.cos(5 * x[i] - x[j])
                
        # Add additional high-frequency sinusoidal components
        for i in range(self.dim):
            result += 0.25 * np.sin(15 * x[i]) * np.cos(7 * x[(i + 2) % self.dim]) * np.sin(6 * x[(i + 3) % self.dim])
            
        # Add a fifth-order polynomial component
        for i in range(self.dim):
            result += 0.08 * (x[i] ** 5) * (i + 1)
            
        # Add interaction terms between all dimensions
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += 0.02 * x[i] * x[j] * np.exp(-0.15 * (x[i] - x[j])**2)
                    
        # Add a sixth-order polynomial component for increased complexity
        for i in range(self.dim):
            result += 0.03 * (x[i] ** 6) * (i + 1)
            
        # Add a highly oscillatory component with multiple frequencies
        for i in range(self.dim):
            result += 0.15 * np.sin(20 * x[i]) * np.cos(8 * x[(i + 1) % self.dim]) * np.sin(9 * x[(i + 2) % self.dim]) * np.cos(3 * x[(i + 3) % self.dim])
            
        # Add a radial component with increased nonlinearity
        r_squared = np.sum(x ** 2)
        result += 0.2 * np.sin(12 * np.sqrt(r_squared)) * np.exp(-0.05 * r_squared)
        
        return result