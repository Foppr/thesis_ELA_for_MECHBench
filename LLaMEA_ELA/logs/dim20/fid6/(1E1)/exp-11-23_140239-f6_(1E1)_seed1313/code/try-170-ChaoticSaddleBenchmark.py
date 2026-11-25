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
        for i in range(1, min(self.dim + 1, 40)):  # Increased to 40 terms for more complexity
            # Saddle point locations with exponential spacing and chaotic perturbation
            saddle_x = i * 0.9 * np.sin(i * 2.5 + x[0] * 0.4) if self.dim > 0 else i * 0.9 * np.sin(i * 2.5)
            saddle_y = i * 0.9 * np.cos(i * 2.5 + x[1] * 0.4) if self.dim > 1 else i * 0.9 * np.cos(i * 2.5)
            
            # Chaotic distance from saddle point (2D only for first few dimensions)
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Add chaotic influence with exponential decay and sinusoidal modulation
                result += 30 * np.exp(-dist**2 / (2 * (i * 0.4)**2)) * np.sin(dist * i * 15) * np.cos(x[0] * i * 2.0)
            elif i <= self.dim:
                # For higher dimensions, use more complex chaotic terms
                result += 25.0 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.35)**2)) * np.sin(x[i-1] * i * 8.0) * np.cos(x[i-1] * 1.6)
        
        # Add higher-order polynomial terms for increased complexity with improved coefficients
        for i in range(self.dim):
            result += 5.0 * x[i]**5 - 10.0 * x[i]**3 + 8.0 * x[i]**2
        
        # Add multi-modal noise component with adaptive frequency to increase ruggedness and challenge optimization
        noise = 2.5 * np.sum(np.sin(60 * x) * np.cos(35 * x) * np.sin(25 * x))
        
        # Add dimensionality-dependent chaotic modulation factor
        dim_factor = 1.0 + 2.5 * np.sin(self.dim * 1.7)
        
        # Add additional chaotic harmonic terms for increased complexity
        harmonic_term = 1.1 * np.sum(np.sin(9.0 * x) * np.cos(10.0 * x) * np.sin(7.0 * x))
        
        # Add fractal-like multiscale component
        fractal_term = 1.0 * np.sum(np.sin(50 * x) * np.cos(25 * x) * np.sin(8 * x) * np.exp(-np.abs(x) / 8.0))
        
        # Add adaptive basin splitting based on dimensionality
        basin_split = 0.5 * np.sum(np.sin(7 * x) * np.cos(8 * x) * np.sin(9 * x) * np.tanh(x))
        
        # Add cross-dimensional coupling terms for increased complexity
        coupling_term = 0.5 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.sin(x[:-1] * 0.9))
        
        return (result * dim_factor + noise + harmonic_term + fractal_term + basin_split + coupling_term)