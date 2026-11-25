import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Add sinusoidal multimodal components
        for i in range(self.dim):
            f_val += 0.5 * np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
                
        return f_val