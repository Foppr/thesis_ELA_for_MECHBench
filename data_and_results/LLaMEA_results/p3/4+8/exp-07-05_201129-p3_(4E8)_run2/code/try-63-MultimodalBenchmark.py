import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
        # Precompute peak locations for scalability
        self.peaks = np.random.uniform(-4.0, 4.0, (10, dim))
        self.peak_heights = np.random.uniform(0.5, 2.0, 10)
        self.peak_widths = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        x_norm = x / 5.0
        
        # Multiple Gaussian peaks with varying heights and widths
        result = 0.0
        for i in range(len(self.peaks)):
            peak = self.peaks[i]
            height = self.peak_heights[i]
            width = self.peak_widths[i]
            # Gaussian peak contribution
            gaussian = height * np.exp(-0.5 * np.sum(((x - peak) / width)**2))
            result += gaussian
        
        # Add a global conditioning term that increases with dimensionality
        conditioning = 0.1 * self.dim * np.sum(x_norm**4)
        result += conditioning
        
        # Add a sinusoidal modulation to increase ruggedness
        modulation = 0.5 * np.sin(3.0 * np.sum(x_norm))
        result += modulation
        
        # Add a radial symmetry breaking term
        r = np.sqrt(np.sum(x_norm**2))
        symmetry_break = 0.2 * r * np.cos(2.0 * r)
        result += symmetry_break
        
        return result