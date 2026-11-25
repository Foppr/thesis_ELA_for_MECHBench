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
        for i in range(1, min(self.dim + 1, 25)):  # Increased to 25 terms for more complexity
            # Saddle point locations with exponential spacing and chaotic perturbation
            saddle_x = i * 0.8 * np.sin(i * 3.0 + x[0] * 0.3) if self.dim > 0 else i * 0.8 * np.sin(i * 3.0)
            saddle_y = i * 0.8 * np.cos(i * 3.0 + x[1] * 0.3) if self.dim > 1 else i * 0.8 * np.cos(i * 3.0)
            
            # Chaotic distance from saddle point (2D only for first few dimensions)
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - saddle_x)**2 + (x[1] - saddle_y)**2)
                # Add chaotic influence with exponential decay and sinusoidal modulation
                result += 15 * np.exp(-dist**2 / (2 * (i * 0.35)**2)) * np.sin(dist * i * 8) * np.cos(x[0] * i * 1.3)
            elif i <= self.dim:
                # For higher dimensions, use more complex chaotic terms
                result += 10.0 * np.exp(-abs(x[i-1] - saddle_x)**2 / (2 * (i * 0.3)**2)) * np.sin(x[i-1] * i * 5.0) * np.cos(x[i-1] * 1.0)
        
        # Add higher-order polynomial terms for increased complexity with improved coefficients
        for i in range(self.dim):
            result += 2.5 * x[i]**5 - 6.0 * x[i]**3 + 4.0 * x[i]**2
        
        # Add multi-modal noise component with adaptive frequency to increase ruggedness and challenge optimization
        noise = 1.0 * np.sum(np.sin(35 * x) * np.cos(20 * x) * np.sin(10 * x))
        
        # Add dimensionality-dependent chaotic modulation factor
        dim_factor = 1.0 + 1.0 * np.sin(self.dim * 1.0)
        
        # Add additional chaotic harmonic terms for increased complexity
        harmonic_term = 0.5 * np.sum(np.sin(6.0 * x) * np.cos(7.0 * x) * np.sin(4.0 * x))
        
        # Add fractal-like multiscale component
        fractal_term = 0.4 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.sin(5 * x) * np.exp(-np.abs(x) / 5.0))
        
        # Add adaptive basin splitting based on dimensionality
        basin_split = 0.2 * np.sum(np.sin(4 * x) * np.cos(5 * x) * np.sin(6 * x) * np.tanh(x))
        
        # Add cross-dimensional coupling terms for increased complexity
        coupling_term = 0.25 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.sin(x[:-1] * 0.6))
        
        return (result * dim_factor + noise + harmonic_term + fractal_term + basin_split + coupling_term)