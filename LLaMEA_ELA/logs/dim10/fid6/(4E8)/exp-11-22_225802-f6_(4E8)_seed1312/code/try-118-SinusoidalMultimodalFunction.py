import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for even greater sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base highly complex sinusoidal component with multiple frequencies
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(4 * scaled_x[i]) * np.sin(7 * scaled_x[i]) * np.cos(11 * scaled_x[i])
            
        # Add multiple nested quadratic valleys with varying coefficients
        for i in range(self.dim):
            result += 0.6 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2) + 0.3 * (x[i]**4)
            
        # Introduce dynamic scaling with exponential growth based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale = np.exp(dynamic_scale) - 1.0
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.8 * np.sin(23 * scaled_x[i]) * np.cos(15 * scaled_x[i]) * np.sin(19 * scaled_x[i])
            
        # Add a global minimum at the origin with strong penalty terms
        result += 0.3 * np.sum(x**2) + 0.2 * dynamic_scale**2 + 0.1 * np.sum(x**4)
        
        # Include extremely strong cross-dimension interactions with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(8 * (scaled_x[i] - scaled_x[j])) * np.sin(5 * (scaled_x[i] + scaled_x[j]))
                
        # Add a substantial shift to the global minimum with multiple sine components
        result += 0.15 * np.sum(np.sin(1.2 * x) + np.sin(0.7 * x))
        
        # Enhanced polynomial terms with higher exponents for increased complexity
        for i in range(self.dim):
            result += 0.5 * (x[i]**6) * np.sin(3 * scaled_x[i]) + 0.4 * (x[i]**8)
            
        # Add a chaotic component with time-varying frequency modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(scaled_x[i] * (1 + 0.7 * np.sin(x[i]) * np.cos(2 * x[i])))
        result += 0.4 * chaotic_component
        
        # Add a fractal-like component with recursive sinusoidal interactions
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(scaled_x[i] + 0.5 * np.sin(2 * scaled_x[i]) + 0.3 * np.sin(3 * scaled_x[i]))
        result += 0.2 * fractal_component**2
        
        return result