import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic term for global basin attraction
        quadratic_term = np.sum(x_normalized**2)
        
        # Nested sinusoidal modulations with varying frequencies and amplitudes
        freq1 = 5 * np.pi
        freq2 = 11 * np.pi
        freq3 = 17 * np.pi
        sinusoidal_term = np.sum(
            np.sin(freq1 * x_normalized)**3 + 
            0.3 * np.sin(freq2 * x_normalized)**4 + 
            0.1 * np.sin(freq3 * x_normalized)**5
        )
        
        # Exponentially decaying Gaussian peaks to increase local minima density
        gaussian_peaks = np.sum(
            np.exp(-10 * x_normalized**2) * 
            (np.cos(3 * np.pi * x_normalized) + 0.5 * np.cos(7 * np.pi * x_normalized))
        )
        
        # Higher-order polynomial term for additional curvature and complexity
        quintic_term = np.sum(x_normalized**5)
        
        # Additional coupled cosine modulation to create more intricate terrain
        coupling_term = np.sum(np.cos(4 * np.pi * x_normalized) * np.sin(2 * np.pi * x_normalized))
        
        # Combine all terms with strategic weights to create a challenging landscape
        return 0.7 * quadratic_term + 0.4 * sinusoidal_term + 0.15 * gaussian_peaks + 0.25 * quintic_term + 0.1 * coupling_term