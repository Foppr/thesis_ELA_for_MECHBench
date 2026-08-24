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
        centers = np.linspace(-1, 1, 9)  # 9 peaks
        heights = np.linspace(0.5, 2.0, 9)  # Varying heights
        widths = np.linspace(0.1, 0.5, 9)  # Varying widths
        
        for i, (center, height, width) in enumerate(zip(centers, heights, widths)):
            # Create a Gaussian peak centered at 'center' with given height and width
            peak = height * np.exp(-0.5 * ((x_norm - center) / width) ** 2)
            peaks.append(peak)
        
        # Sum all peaks
        peak_sum = np.sum(peaks, axis=0)
        
        # Add quadratic term to encourage convergence to origin
        quadratic = 0.1 * np.sum(x_norm**2)
        
        # Add a sinusoidal modulation to increase complexity
        modulation = 0.5 * np.sin(3 * np.pi * x_norm)
        
        # Combine all components
        return np.sum(peak_sum + quadratic + modulation)