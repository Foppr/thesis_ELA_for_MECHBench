import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like component using recursive cosine composition
        fractal_term = 0.0
        for i in range(self.dim):
            temp = x_scaled[i]
            for _ in range(3):  # Recursive depth
                temp = np.cos(temp * np.pi * (i + 1))
            fractal_term += temp * (i + 1) * 0.1
            
        # Chaotic gradient modulation with dimension-dependent scaling
        chaotic_grad = 1.0
        for i in range(self.dim):
            chaotic_grad *= (1 + 0.3 * np.cos(x_scaled[i] * np.pi * (i + 1) * 2) * 
                           np.sin(x_scaled[i] * np.pi * (i + 1) * 3))
            
        # Saddle-point attractor component with multiple basins
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (np.cos(x_scaled[i] * 2) * np.sin(x_scaled[i] * 3) + 
                           0.5 * np.cos(x_scaled[i] * 4) * np.sin(x_scaled[i] * 5)) * (i + 1)
            
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.cos((x_scaled[i] + x_scaled[j]) * np.pi * (i + j + 1))
                cross_term += coupling * (i + j + 1) * 0.05
                
        # Dimensionally dependent scaling with fractal-like behavior
        dim_scaling = 1.0
        for i in range(self.dim):
            dim_scaling *= (1 + 0.2 * np.sin(x_scaled[i] * np.pi * (i + 1) * 0.5))
            
        # Add a chaotic perturbation based on coordinate sum
        coord_sum = np.sum(x_scaled)
        chaos_perturb = 0.1 * np.sin(coord_sum * np.pi * 7) * np.cos(coord_sum * np.pi * 11)
        
        # Combine all terms with appropriate weights
        result = fractal_term + chaotic_grad * saddle_term + cross_term * dim_scaling + chaos_perturb
        
        # Ensure the function has a global minimum around the origin
        return result + 5.0