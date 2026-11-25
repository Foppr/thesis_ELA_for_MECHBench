import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple Gaussian peaks with exponential decay and sinusoidal modulation
        for i in range(1, min(self.dim + 1, 20)):
            # Peak locations with chaotic distribution
            peak_x = 5.0 * np.sin(i * 1.7 + x[0] * 0.3) if self.dim > 0 else 5.0 * np.sin(i * 1.7)
            peak_y = 5.0 * np.cos(i * 1.7 + x[1] * 0.3) if self.dim > 1 else 5.0 * np.cos(i * 1.7)
            
            # Distance from peak
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - peak_x)**2 + (x[1] - peak_y)**2)
                # Gaussian with sinusoidal modulation
                result += 10 * np.exp(-dist**2 / (2 * (i * 0.5)**2)) * np.sin(dist * i * 3) * np.cos(x[0] * i * 0.8)
            elif i <= self.dim:
                # For higher dimensions, use more complex chaotic terms
                result += 8.0 * np.exp(-abs(x[i-1] - peak_x)**2 / (2 * (i * 0.4)**2)) * np.sin(x[i-1] * i * 5.0) * np.cos(x[i-1] * 0.9)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 2.0 * x[i]**6 - 6.0 * x[i]**4 + 4.0 * x[i]**2
        
        # Add multi-modal noise component with adaptive frequency to increase ruggedness and challenge optimization
        noise = 1.2 * np.sum(np.sin(35 * x) * np.cos(20 * x) * np.sin(10 * x))
        
        # Add dimensionality-dependent chaotic modulation factor
        dim_factor = 1.0 + 1.2 * np.sin(self.dim * 1.5)
        
        # Add additional chaotic harmonic terms for increased complexity
        harmonic_term = 0.6 * np.sum(np.sin(6.0 * x) * np.cos(7.0 * x) * np.sin(4.0 * x))
        
        # Add fractal-like multiscale component
        fractal_term = 0.5 * np.sum(np.sin(25 * x) * np.cos(12 * x) * np.sin(5 * x) * np.exp(-np.abs(x) / 5.0))
        
        # Add adaptive basin splitting based on dimensionality
        basin_split = 0.2 * np.sum(np.sin(4 * x) * np.cos(5 * x) * np.sin(6 * x) * np.tanh(x))
        
        # Add cross-dimensional coupling terms for increased complexity
        coupling_term = 0.2 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.sin(x[:-1] * 0.6))
        
        return (result * dim_factor + noise + harmonic_term + fractal_term + basin_split + coupling_term)