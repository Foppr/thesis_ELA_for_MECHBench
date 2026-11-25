import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with shifted minimum
            result += (x[i] - 1.0)**2
            
            # Enhanced sinusoidal perturbations creating multiple local minima
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
            # Additional sinusoidal term with higher frequency for more complexity
            result += 0.4 * np.sin(7.0 * x[i])**2
            
            # Third sinusoidal component for added challenge
            result += 0.3 * np.cos(4.0 * x[i]) * np.sin(x[i])
            
        # Add stronger interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction term with combined sinusoidal effects
                result += 0.2 * np.sin(2.0 * x[i] + x[j]) * np.cos(x[i] - 2.0 * x[j])
                
        # Add a global scaling factor to improve fitness characteristics
        result *= 1.2
        
        return result