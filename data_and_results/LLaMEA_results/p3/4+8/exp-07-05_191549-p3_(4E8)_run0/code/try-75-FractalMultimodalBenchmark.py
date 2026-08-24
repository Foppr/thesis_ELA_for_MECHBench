import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Add multiple fractal components with different scales and rotations
        for i in range(1, min(6, self.dim + 1)):
            # Scale factor for each dimension
            scale = 2 ** i
            
            # Create spiral-like pattern using harmonic functions
            spiral = np.sin(scale * np.pi * x_norm) * np.cos(scale * np.pi * x_norm)
            
            # Add logarithmic scaling component
            log_component = np.log(np.abs(x_norm) + 1e-8) * np.sin(scale * np.pi * x_norm**2)
            
            # Combine components with varying weights
            result += (0.5 * spiral**2 + 0.3 * log_component**2 + 
                      0.2 * np.sin(scale * np.pi * x_norm) * np.cos(scale * np.pi * x_norm))
        
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction between pairs of dimensions
                interaction = np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(np.pi * (x_norm[i] - x_norm[j]))
                result += 0.1 * interaction
        
        # Add global scaling and offset to ensure proper conditioning
        result = np.abs(result) + 0.1 * np.sum(x_norm**4)
        
        return result