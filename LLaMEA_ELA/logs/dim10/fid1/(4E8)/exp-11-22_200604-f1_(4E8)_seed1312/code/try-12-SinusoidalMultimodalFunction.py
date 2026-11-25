import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Add sinusoidal multimodal components with modified frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.7 * np.sin(6 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i])
            
        # Add interaction terms between dimensions with different coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
                
        # Add shifted sinusoidal terms to create additional local minima
        for i in range(self.dim):
            f_val += 0.2 * np.sin(8 * np.pi * (x_norm[i] + 0.3)) + 0.1 * np.cos(7 * np.pi * (x_norm[i] - 0.2))
                
        return f_val