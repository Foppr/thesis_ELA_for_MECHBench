import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with varying scales
        for i in range(1, min(self.dim + 1, 6)):  # Limit to 5 terms to avoid overfitting
            # Saddle point locations with exponential spacing
            saddle_x = i * 0.3 * np.sin(i * 1.5)
            saddle_y = i * 0.3 * np.cos(i * 1.5)
            
            # Chaotic distance from saddle point (2D only for first few dimensions)
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Add chaotic influence with exponential decay
                result += 3 * np.exp(-dist**2 / (2 * (i * 0.15)**2)) * np.sin(dist * i * 2)
            elif i <= self.dim:
                # For higher dimensions, use simpler chaotic terms
                result += 2 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.1)**2)) * np.sin(x[i-1] * i)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.3 * x[i]**4 - 1.5 * x[i]**2
        
        # Add noise component to increase ruggedness but reduce overall impact
        noise = 0.05 * np.sum(np.sin(8 * x))
        
        return result + noise