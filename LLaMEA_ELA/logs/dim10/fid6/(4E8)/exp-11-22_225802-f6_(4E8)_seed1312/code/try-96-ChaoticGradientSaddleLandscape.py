import numpy as np

class ChaoticGradientSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for chaotic gradient behavior
        scaled_x = x * (np.pi / 5.0)
        
        # Base polynomial chaos component with alternating signs
        result = 0.0
        for i in range(self.dim):
            result += (-1)**i * (scaled_x[i]**5 - 2*scaled_x[i]**3 + scaled_x[i])
            
        # Add chaotic sinusoidal gradient terms with modified frequencies
        for i in range(self.dim):
            result += 0.6 * np.sin(9 * scaled_x[i]) * np.cos(7 * scaled_x[i])
            
        # Introduce saddle-point structure with hyperbolic tangent components
        for i in range(self.dim):
            result += 0.4 * np.tanh(4 * scaled_x[i]) * (scaled_x[i]**2 - 1)
            
        # Add dynamic coupling between dimensions based on polynomial interactions with altered coefficients
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i]**3 + x[j]**3) * np.sin(0.3 * (x[i] + x[j]))
        result += 0.3 * coupling_term
        
        # Include a global minimum shift with exponential penalty
        result += 0.15 * np.exp(-0.3 * np.sum(x**2))
        
        # Add high-frequency oscillatory component for increased complexity
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(13 * scaled_x[i]) * np.cos(11 * scaled_x[i])
        result += 0.5 * oscillation
        
        # Introduce a multi-modal structure with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.3 * (np.sin(4 * scaled_x[i]) + np.cos(3 * scaled_x[i]))**2
        result += multimodal
        
        # Add dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result