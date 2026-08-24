import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple Gaussian peaks with different centers, heights, and widths
        peaks = []
        centers = np.linspace(-0.9, 0.9, 11)  # 11 peaks, slightly shifted
        heights = np.linspace(0.6, 1.8, 11)  # Varying heights
        widths = np.linspace(0.12, 0.45, 11)  # Varying widths
        
        for i, (center, height, width) in enumerate(zip(centers, heights, widths)):
            # Create a Gaussian peak centered at 'center' with given height and width
            peak = height * np.exp(-0.5 * ((x_norm - center) / width) ** 2)
            peaks.append(peak)
        
        # Sum all peaks
        peak_sum = np.sum(peaks, axis=0)
        
        # Add quadratic term to encourage convergence to origin with modified coefficient
        quadratic = 0.15 * np.sum(x_norm**2)
        
        # Add a sinusoidal modulation to increase complexity with higher frequency
        modulation = 0.6 * np.sin(5 * np.pi * x_norm)
        
        # Add a cosine modulation to further increase landscape complexity
        cosine_mod = 0.3 * np.cos(4 * np.pi * x_norm)
        
        # Combine all components
        return np.sum(peak_sum + quadratic + modulation + cosine_mod)