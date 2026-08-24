import numpy as np

class FractalPeakBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like peak structure with self-similar patterns at different scales
        fractal_peaks = 0
        scales = [1, 2, 3, 5]
        for scale in scales:
            peak_positions = np.linspace(-1, 1, scale * 4 + 1)[1::2]  # Midpoints
            for pos in peak_positions:
                # Multi-dimensional peak with varying width and height
                peak_height = 1.0 / (scale * 0.5)
                peak_width = 1.0 / (scale * 2.0)
                distance = np.sum((x_norm - pos)**2)
                fractal_peaks += peak_height * np.exp(-distance / (2 * peak_width**2))
        
        # Exponential interaction terms creating rugged terrain
        exp_interaction = np.sum(np.exp(5 * np.abs(x_norm)) * np.sin(10 * x_norm)**2)
        
        # Dynamic dimensionality scaling - different weights for different dimensions
        dim_weights = np.array([np.sin(i * np.pi / self.dim) + 1.5 for i in range(self.dim)])
        weighted_terms = np.sum(dim_weights * x_norm**4)
        
        # Multi-scale sinusoidal modulation with frequency that increases with dimension
        modulation = 0
        for i in range(self.dim):
            freq = (i + 1) * 8
            modulation += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x_norm[i] * x_norm[j])**3
        
        # Control parameter for landscape complexity
        complexity_factor = 1.0 + 0.5 * np.sin(self.dim * 0.3)
        
        # Combine all components
        result = complexity_factor * (fractal_peaks + 0.5 * exp_interaction + 0.3 * weighted_terms + 
                                    0.2 * modulation + 0.1 * cross_coupling)
        
        # Add noise with amplitude dependent on function value
        noise_amp = 0.01 * (1 + np.abs(result))
        noise = noise_amp * np.random.uniform(-0.5, 0.5)
        
        return result + noise