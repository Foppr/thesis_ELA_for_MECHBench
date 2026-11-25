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
                result += 6 * np.exp(-dist**2 / (2 * (i * 0.25)**2)) * np.sin(dist * i * 4) * np.cos(x[0] * i * 0.7)
            elif i <= self.dim:
                # For higher dimensions, use more complex chaotic terms
                result += 4.0 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.2)**2)) * np.sin(x[i-1] * i * 2.5) * np.cos(x[i-1] * 0.5)
        
        # Add higher-order polynomial terms for increased complexity with improved coefficients
        for i in range(self.dim):
            result += 1.2 * x[i]**5 - 3.5 * x[i]**3 + 1.8 * x[i]**2
        
        # Add multi-modal noise component with adaptive frequency to increase ruggedness and challenge optimization
        noise = 0.35 * np.sum(np.sin(20 * x) * np.cos(9 * x) * np.sin(5 * x))
        
        # Add dimensionality-dependent chaotic modulation factor
        dim_factor = 1.0 + 0.45 * np.sin(self.dim * 0.65)
        
        # Add additional chaotic harmonic terms for increased complexity
        harmonic_term = 0.2 * np.sum(np.sin(3.5 * x) * np.cos(4.2 * x) * np.sin(2.1 * x))
        
        return (result * dim_factor + noise + harmonic_term)