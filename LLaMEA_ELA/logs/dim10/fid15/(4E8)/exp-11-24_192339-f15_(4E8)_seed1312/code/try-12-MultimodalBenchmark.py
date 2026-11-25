import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillations with multiple frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 
                         0.5 * np.sin(4 * np.pi * x_norm) + 
                         0.3 * np.sin(6 * np.pi * x_norm))
        
        # Multiple Gaussian peaks with varying positions and heights
        gaussian_peaks = 0
        peak_positions = np.linspace(-1, 1, 7)
        peak_heights = np.array([1.0, 0.8, 1.2, 0.6, 1.0, 0.9, 1.1])
        
        for i, (pos, height) in enumerate(zip(peak_positions, peak_heights)):
            gaussian_peaks += height * np.exp(-30 * (x_norm - pos)**2)
            
        # Additional cosine term to increase complexity
        cos_term = np.sum(0.4 * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with different weights
        result = 0.4 * sin_term + 0.4 * gaussian_peaks + 0.2 * cos_term
        
        # Add a bowl-shaped quadratic term to guide convergence
        quadratic_term = 0.15 * np.sum(x_norm**2)
        
        # Add a small noise component to increase difficulty
        noise = 0.05 * np.random.random()
        
        return result + quadratic_term + noise