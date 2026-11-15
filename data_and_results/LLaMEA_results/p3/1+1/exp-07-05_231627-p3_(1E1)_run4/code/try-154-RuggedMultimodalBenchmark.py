import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Exponentially decaying Gaussian peaks with varying widths and heights
        peaks = 0
        num_peaks = 20
        for i in range(num_peaks):
            # Random center in [-1, 1]
            center = np.random.uniform(-1, 1, self.dim)
            # Random width and height
            width = np.random.uniform(0.1, 0.5)
            height = np.random.uniform(0.5, 2.0)
            # Gaussian peak
            peak = height * np.exp(-np.sum(((x_norm - center) / width)**2) / 2)
            peaks += peak
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal = 0
        for i in range(10):
            freq = np.random.uniform(5, 20)
            amp = np.random.uniform(0.1, 0.5)
            phase = np.random.uniform(0, 2 * np.pi)
            sinusoidal += amp * np.sin(freq * np.sum(x_norm) + phase)
        
        # Rugged terrain component with fractional Brownian motion-like behavior
        rugged = 0
        for i in range(5):
            freq = np.random.uniform(10, 30)
            amp = np.random.uniform(0.2, 1.0)
            rugged += amp * np.abs(np.sin(freq * np.sum(x_norm**1.5))) * np.exp(-np.sum(np.abs(x_norm)))
        
        # Cross-dimensional interaction terms with varying strength
        interaction = 0
        for i in range(self.dim - 1):
            interaction += np.abs(x_norm[i] - x_norm[i+1])**3.5
        
        # Combine components with dynamic weights
        result = 0.4 * quadratic + 0.35 * peaks + 0.15 * sinusoidal + 0.08 * rugged + 0.02 * interaction
        
        # Add noise with amplitude proportional to function value
        noise = 0.01 * (1 + np.abs(result)) * np.random.uniform(-1, 1)
        
        return result + noise