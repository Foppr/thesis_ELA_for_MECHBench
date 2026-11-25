import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        sum_squares = np.sum(x_norm**2)
        
        # Highly multimodal component with exponentially increasing local minima
        multimodal = 0.0
        for i in range(self.dim):
            # Create exponentially increasing frequency components
            freq = 2**(i+1) * np.pi
            multimodal += np.sin(freq * x_norm[i])**8 + 0.5 * np.sin(3 * freq * x_norm[i])**4
        
        # Additional complex term to create rugged landscape
        rugged = 0.0
        for i in range(self.dim):
            rugged += (x_norm[i]**2) * np.cos(10 * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Control condition number with higher order terms
        high_order = 0.05 * np.sum(np.abs(x_norm)**6)
        
        return sum_squares + multimodal + rugged + high_order