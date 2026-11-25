import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Tent map chaotic component with parameter control
        tent_map = 0.0
        a = 1.8  # Chaotic parameter
        for i in range(self.dim):
            tent_map += np.abs(x_scaled[i] * a - np.floor(x_scaled[i] * a + 0.5))
        
        # Polynomial interaction terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2 * x[j]**3 + 
                             0.5 * x[i]**3 * x[j]**2 + 
                             0.3 * x[i] * x[j]**4 + 
                             0.2 * x[i]**4 * x[j])
                
        # Fractal-like self-similarity component using multiple scales
        fractal_term = 0.0
        for scale in [0.5, 1.0, 2.0, 3.0]:
            for i in range(self.dim):
                fractal_term += np.sin(scale * x[i]) * np.cos(scale * x[i]**2) * np.sin(scale * x[i]**3)
                
        # Cross-dimensional coupling with exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                
        # Asymmetric multimodal component with different frequencies per dimension
        asym_term = 0.0
        for i in range(self.dim):
            asym_term += (np.sin(2 * x[i]) + 
                         0.7 * np.cos(3 * x[i]) + 
                         0.4 * np.sin(5 * x[i]) + 
                         0.2 * np.cos(7 * x[i]) +
                         0.1 * np.sin(9 * x[i]))
            
        # Add a global periodic modulation based on the product of coordinates
        coord_product = np.prod(x)
        periodic_mod = 1.0 + 0.4 * np.sin(0.3 * coord_product) * np.cos(0.2 * coord_product)
        
        # Combine all terms with different weights
        return tent_map + poly_term + fractal_term + coupling_term + asym_term + periodic_mod + 3.0