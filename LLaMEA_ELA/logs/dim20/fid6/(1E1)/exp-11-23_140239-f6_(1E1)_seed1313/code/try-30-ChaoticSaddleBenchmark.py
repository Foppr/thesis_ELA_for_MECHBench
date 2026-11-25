import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with exponential spacing and varying influence
        for i in range(1, min(self.dim + 3, 10)):  # Limit to avoid excessive computation
            # Saddle point locations with chaotic distribution
            saddle_x = i * 0.7 * np.sin(i * 1.3)
            saddle_y = i * 0.7 * np.cos(i * 1.7)
            
            # Adaptive distance based on dimensionality
            if self.dim > 1:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Exponentially increasing influence with chaotic decay
                influence = 10 * np.exp(-dist**2 / (2 * (i * 0.2)**2)) * np.sin(dist * i * 0.5)
                result += influence
        
        # Add higher-order polynomial terms for increased complexity and non-convexity
        for i in range(self.dim):
            result += 0.3 * x[i]**6 - 1.5 * x[i]**4 + 2 * x[i]**2
        
        # Add adaptive noise component with chaotic scaling
        noise = 0.2 * np.sum(np.sin(15 * x) * np.cos(7 * x))
        
        # Add cross-dimensional interaction terms for increased complexity
        if self.dim > 2:
            for i in range(self.dim - 2):
                result += 0.1 * x[i] * x[i+1] * np.sin(x[i+2])
        
        # Add chaotic perturbation term that scales with problem dimension
        chaos_term = 0.5 * np.sum(np.sin(20 * x) * np.cos(15 * x))
        result += chaos_term
        
        return result + noise