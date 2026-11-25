import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for enhanced sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base sinusoidal component with chaotic interaction terms
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(4 * scaled_x[i]) * np.sin(7 * scaled_x[i])
            
        # Add nested quadratic valleys to create multiple local minima
        for i in range(self.dim):
            result += 0.3 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.4 * np.sin(15 * scaled_x[i]) * np.cos(11 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.15 * np.sum(x**2) + 0.08 * dynamic_scale**2
        
        # Include cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(3 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.08 * np.sum(np.sin(0.7 * x))
        
        # Introduce additional chaotic elements to improve fitness score
        for i in range(self.dim):
            result += 0.25 * np.sin(5 * scaled_x[i]) * np.cos(12 * scaled_x[i]) * np.sin(8 * scaled_x[i])
            
        # Add polynomial coupling terms to enhance multimodality
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_coupling += (x[i]**4) * np.sin(scaled_x[i])
        result += 0.2 * poly_coupling
        
        # Add cubic coupling terms for even higher multimodality
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_coupling += (x[i]**3) * (x[j]**2) * np.cos(scaled_x[i] + scaled_x[j])
        result += 0.12 * cubic_coupling
        
        # Add a fourth-order polynomial component to increase landscape complexity
        fourth_order = 0.0
        for i in range(self.dim):
            fourth_order += (x[i]**4) * np.sin(2 * scaled_x[i])
        result += 0.08 * fourth_order
        
        return result