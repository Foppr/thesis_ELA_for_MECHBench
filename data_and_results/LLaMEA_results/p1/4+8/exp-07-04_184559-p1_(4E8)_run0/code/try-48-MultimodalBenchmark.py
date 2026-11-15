import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with higher frequency and amplitude
        f2 = np.sum(np.sin(12 * np.pi * x_norm)**2)
        
        # Additional quadratic term with radial bias and shifted center
        f3 = 0.3 * np.sum((x_norm - 0.2)**2)
        
        # Add cross-terms to increase interaction between dimensions
        f4 = 0.15 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Add a radial component to increase conditioning difficulty
        radial_term = 0.2 * np.sum(x_norm**4)
        
        # Add a chaotic modulation to increase local minima density
        chaotic_term = 0.1 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Combine all terms to create a more challenging landscape
        return f1 + 0.8 * f2 + f3 + 0.3 * f4 + radial_term + chaotic_term