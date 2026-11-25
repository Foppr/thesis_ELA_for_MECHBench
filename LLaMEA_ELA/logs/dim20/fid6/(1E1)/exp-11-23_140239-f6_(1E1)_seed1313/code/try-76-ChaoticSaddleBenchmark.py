import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Add multiple chaotic saddle points with exponential spacing and chaotic perturbation
        for i in range(1, min(self.dim + 1, 10)):  # Increased to 9 terms for more complexity
            # Saddle point locations with exponential spacing and chaotic perturbation
            saddle_x = i * 0.5 * np.sin(i * 2.0 + x[0] * 0.2) if self.dim > 0 else i * 0.5 * np.sin(i * 2.0)
            saddle_y = i * 0.5 * np.cos(i * 2.0 + x[1] * 0.2) if self.dim > 1 else i * 0.5 * np.cos(i * 2.0)
            
            # Chaotic distance from saddle point (2D only for first few dimensions)
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Add chaotic influence with exponential decay and sinusoidal modulation
                result += 6 * np.exp(-dist**2 / (2 * (i * 0.25)**2)) * np.sin(dist * i * 5) * np.cos(x[0] * i * 0.7)
            elif i <= self.dim:
                # For higher dimensions, use more complex chaotic terms
                result += 4.0 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.2)**2)) * np.sin(x[i-1] * i * 3.0) * np.cos(x[i-1] * 0.5)
        
        # Add cross-dimensional coupling terms for increased complexity
        for i in range(0, self.dim - 1):
            for j in range(i + 1, min(self.dim, i + 4)):
                coupling = np.sin(x[i] * x[j] * (i + j) * 0.1) * np.cos((x[i] + x[j]) * 0.3)
                result += 0.8 * coupling
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.7 * x[i]**5 - 2.5 * x[i]**3 + 1.5 * x[i]**2
        
        # Add multi-modal noise component with adaptive frequency to increase ruggedness and challenge optimization
        noise = 0.2 * np.sum(np.sin(20 * x) * np.cos(8 * x))
        
        # Add dimensionality-dependent chaotic modulation factor
        dim_factor = 1.0 + 0.3 * np.sin(self.dim * 0.6)
        return result * dim_factor + noise