import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic basin term
        quad_term = 0.1 * np.sum(x_norm**2)
        
        # Trigonometric composite potential with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 3**(i+1)
            amp = 1.0 / (1.0 + i * 0.1)
            trig_term += amp * np.sin(freq * x_norm[i]) * np.cos(2 * freq * x_norm[i])
        
        # Polynomial interactions with mixed degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += 0.05 * x_norm[i]**3 + 0.02 * x_norm[i]**4
        
        # Saddle-point structure with hyperbolic tangent interactions
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.03 * np.tanh(2.0 * x_norm[i]) * np.sin(5 * x_norm[i])
        
        # Composite chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 0.04 * np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(np.pi * self.dim / 8.0)
        
        # Multi-modal interaction term with exponential decay
        multimodal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interactions
                multimodal_term += 0.02 * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * np.sin(7 * x_norm[i])
        
        return scale_factor * (quad_term + trig_term + poly_term + saddle_term + chaotic_term + multimodal_term)