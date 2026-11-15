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
        centers = np.linspace(-1, 1, 13)  # Increased number of peaks
        heights = np.linspace(0.3, 2.5, 13)  # Extended height range
        widths = np.linspace(0.05, 0.6, 13)  # Extended width range
        
        for i, (center, height, width) in enumerate(zip(centers, heights, widths)):
            # Create a Gaussian peak centered at 'center' with given height and width
            peak = height * np.exp(-0.5 * ((x_norm - center) / width) ** 2)
            peaks.append(peak)
        
        # Sum all peaks
        peak_sum = np.sum(peaks, axis=0)
        
        # Add quadratic term to encourage convergence to origin
        quadratic = 0.15 * np.sum(x_norm**2)
        
        # Add a sinusoidal modulation with higher frequency and amplitude
        modulation = 0.8 * np.sin(5 * np.pi * x_norm)
        
        # Add cross-terms to increase interaction between dimensions
        cross_term = 0.05 * np.sum(x_norm[:-1] * x_norm[1:], axis=0)
        
        # Add a small cubic term for additional nonlinearity
        cubic = 0.02 * np.sum(x_norm**3, axis=0)
        
        # Combine all components
        return np.sum(peak_sum + quadratic + modulation + cross_term + cubic)