import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Chaotic multimodal term with fractal-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(13 * np.pi * x[i]) ** 2 * np.exp(-0.1 * np.abs(x[i]))
        
        # Exponential interaction terms between dimensions
        exp_interaction = 0.0
        for i in range(self.dim - 1):
            exp_interaction += np.exp(0.5 * (x[i] - x[i+1])**2)
        
        # Add higher-order polynomial interaction terms
        poly_interaction = 0.0
        for i in range(self.dim - 3):
            poly_interaction += (x[i] * x[i+1] * x[i+2] * x[i+3])**2
        
        # Add a complex periodic component with multiple frequencies
        multi_freq = 0.0
        for i in range(self.dim):
            multi_freq += np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) + \
                         np.sin(3 * np.pi * x[i]) * np.cos(11 * np.pi * x[i])
        
        # Shift global minimum to create more challenging landscape
        shift = 1.2
        
        # Combine terms to create extremely challenging landscape
        return quadratic + 0.3 * chaotic + 0.15 * exp_interaction + 0.1 * poly_interaction + 0.05 * multi_freq + shift