import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-frequency sinusoidal components with exponential growth
        f1 = np.sum(np.sin(2 ** (np.arange(1, self.dim + 1)) * np.pi * x_norm))
        
        # Saddle-point structure in the middle dimensions
        if self.dim >= 4:
            saddle = np.sum(x_norm[2:self.dim//2]**2 - x_norm[self.dim//2:3*self.dim//4]**2)
        else:
            saddle = 0.0
            
        # Quadratic basin term with adaptive scaling
        f2 = np.sum(x_norm**2) * (1.0 + 0.5 * np.sin(np.sum(x_norm**2)))
        
        # Additional multimodal component with varying amplitudes and frequencies
        f3 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                   np.exp(-np.abs(x_norm)) * (1.0 + 0.3 * np.sin(5 * x_norm)))
        
        # Add a global shaping term that modifies the landscape based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x_norm**2))
        shape_term = 0.3 * np.exp(-dist_from_origin) * np.sin(10 * dist_from_origin)
        
        # Combine all components with varying weights and non-linear interactions
        result = 0.15 * f1 + 0.4 * f2 + 0.3 * f3 + 0.1 * saddle + shape_term + 2.0
        
        return result