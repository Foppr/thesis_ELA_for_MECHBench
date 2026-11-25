import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        
        # Base quadratic term with shifted minima
        for i in range(self.dim):
            result += (x[i] - 1.0)**2
            
        # Enhanced sinusoidal perturbations creating multiple local minima
        for i in range(self.dim):
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Additional complex sinusoidal terms for increased landscape complexity
        for i in range(self.dim):
            result += 0.4 * np.sin(4.0 * x[i])**2 + 0.3 * np.cos(6.0 * x[i])
            
        # Cross-dimensional interaction terms with higher frequency components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(2.0 * (x[i] + x[j])) * np.cos(3.0 * (x[i] - x[j]))
                
        # Additional global modulation term
        result += 0.1 * np.sum(np.sin(x)**2)
        
        return result