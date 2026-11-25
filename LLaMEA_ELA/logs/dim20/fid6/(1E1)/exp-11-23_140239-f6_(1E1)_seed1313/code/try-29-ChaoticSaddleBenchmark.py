import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point function with increasing complexity
        result = 0.0
        
        # Base quadratic term
        result += 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with varying scales
        for i in range(1, self.dim + 1):
            # Saddle point locations with exponential spacing
            saddle_x = i * 0.5 * np.sin(i)
            saddle_y = i * 0.5 * np.cos(i)
            
            # Chaotic distance from saddle point
            dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
            
            # Add chaotic influence with exponential decay
            if self.dim > 1:
                result += 5 * np.exp(-dist**2 / (2 * (i * 0.1)**2)) * np.sin(dist * i)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2 * x[i]**2
        
        # Add noise component to increase ruggedness
        noise = 0.1 * np.sum(np.sin(10 * x))
        
        return result + noise