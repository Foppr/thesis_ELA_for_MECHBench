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
            result += 0.6 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality with exponential factor
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale = np.exp(dynamic_scale) - 1.0
        
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.8 * np.sin(23 * scaled_x[i]) * np.cos(13 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.3 * np.sum(x**2) + 0.2 * dynamic_scale**2
        
        # Include stronger cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(8 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.15 * np.sum(np.sin(1.2 * x))
        
        # Enhanced polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.5 * (x[i]**5) * np.sin(3 * scaled_x[i])
            
        # Add a chaotic component with dynamic frequency modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(scaled_x[i] * (1 + 0.7 * np.sin(x[i]) * np.cos(2 * x[i])))
        result += 0.4 * chaotic_component
        
        # Add fractal-like self-similarity through recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(5 * scaled_x[i]) * np.cos(5 * scaled_x[i]) * np.sin(10 * scaled_x[i])
        result += 0.3 * fractal_term
        
        # Add a multi-modal peak structure with varying amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.4 * np.sin(6 * scaled_x[i]) * np.cos(6 * scaled_x[i])
        result += 0.35 * multimodal
        
        return result