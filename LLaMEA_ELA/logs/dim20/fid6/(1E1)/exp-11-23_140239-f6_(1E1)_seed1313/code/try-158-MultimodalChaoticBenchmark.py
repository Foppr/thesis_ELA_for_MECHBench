import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple Gaussian peaks with exponentially decaying heights and sinusoidal modulation
        for i in range(1, min(self.dim + 1, 25)):
            # Peak locations with chaotic distribution
            peak_x = 5.0 * np.sin(i * 1.7 + x[0] * 0.3) if self.dim > 0 else 5.0 * np.sin(i * 1.7)
            peak_y = 5.0 * np.cos(i * 1.7 + x[1] * 0.3) if self.dim > 1 else 5.0 * np.cos(i * 1.7)
            
            # Gaussian peak with exponential decay
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - peak_x)**2 + (x[1] - peak_y)**2)
                height = 25.0 * np.exp(-i * 0.3) * (1.0 + 0.5 * np.sin(i * 3.0))
                result += height * np.exp(-dist**2 / (2 * (0.5 * i)**2)) * np.cos(dist * i * 2.0)
            elif i <= self.dim:
                # Higher dimensional peaks with varying influence
                dist = abs(x[i-1] - peak_x)
                height = 20.0 * np.exp(-i * 0.4) * (1.0 + 0.3 * np.cos(i * 2.5))
                result += height * np.exp(-dist**2 / (2 * (0.6 * i)**2)) * np.sin(dist * i * 1.5)
        
        # Add sinusoidal modulation to increase complexity
        mod_term = 2.0 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.sin(x * 0.5))
        
        # Add multi-modal noise component with varying frequency and amplitude
        noise = 1.2 * np.sum(np.sin(35 * x) * np.cos(20 * x) * np.sin(10 * x))
        
        # Add fractal-like scaling factor based on dimensionality
        scale_factor = 1.0 + 0.8 * np.sin(self.dim * 0.7)
        
        # Add cross-dimensional coupling with chaotic interaction terms
        coupling = 0.5 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] / (x[1:] + 1e-8)) * np.sin(x[1:] * 0.3))
        
        # Add polynomial perturbations for increased ruggedness
        poly_term = 0.8 * np.sum(2.0 * x**6 - 5.0 * x**4 + 3.0 * x**2)
        
        return (result * scale_factor + mod_term + noise + coupling + poly_term)