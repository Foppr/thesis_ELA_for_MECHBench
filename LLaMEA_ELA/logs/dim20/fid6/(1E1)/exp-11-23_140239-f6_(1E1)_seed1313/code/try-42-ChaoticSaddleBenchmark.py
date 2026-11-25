import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with varying scales and shifted positions
        for i in range(1, min(self.dim + 1, 6)):  # Limit to 5 terms to avoid overfitting
            # Saddle point locations with exponential spacing and sinusoidal shifts
            saddle_x = i * 0.3 * np.sin(i * 1.5) + 0.2 * np.cos(i * 0.7)
            saddle_y = i * 0.3 * np.cos(i * 1.5) + 0.2 * np.sin(i * 0.7)
            
            # Chaotic distance from saddle point (2D only for first few dimensions)
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Add chaotic influence with exponential decay and modified frequency
                result += 3.5 * np.exp(-dist**2 / (2 * (i * 0.12)**2)) * np.sin(dist * i * 2.5)
            elif i <= self.dim:
                # For higher dimensions, use simpler chaotic terms with different coefficients
                result += 2.2 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.13)**2)) * np.sin(x[i-1] * i * 1.5)
        
        # Add higher-order polynomial terms for increased complexity with altered exponents
        for i in range(self.dim):
            result += 0.35 * x[i]**4 - 1.6 * x[i]**2 + 0.1 * x[i]**6
        
        # Add noise component to increase ruggedness but reduce overall impact
        noise = 0.06 * np.sum(np.sin(8 * x) * np.cos(3 * x))
        
        return result + noise