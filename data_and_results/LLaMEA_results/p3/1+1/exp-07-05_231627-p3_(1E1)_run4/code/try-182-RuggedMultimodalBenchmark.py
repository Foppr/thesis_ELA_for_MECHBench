import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Base quadratic component
        quadratic = np.sum(x_norm**2)
        
        # Exponentially decaying sinusoidal waves with varying frequencies and amplitudes
        waves = 0
        for i in range(1, min(21, self.dim + 1)):
            freq = 2**i
            amp = np.exp(-0.1 * i)
            waves += amp * np.sin(freq * np.pi * x_norm) * np.cos(freq * np.pi * x_norm)
        
        # Adaptive peak density based on dimensionality
        peaks = 0
        peak_count = max(5, self.dim // 2)
        for i in range(peak_count):
            # Random peak positions with clustering tendency
            pos = np.sin(np.linspace(0, 2 * np.pi, peak_count, endpoint=False) + i * 0.5)
            # Varying peak heights and widths
            height = 1.0 + 0.5 * np.sin(i)
            width = 0.5 + 0.3 * np.cos(i)
            peaks += height * np.exp(-np.sum(((x_norm - pos)**2) / (2 * width**2)))
        
        # Cross-dimensional interaction terms with varying strength
        interaction = 0
        for i in range(self.dim - 1):
            interaction += (x_norm[i] - x_norm[i+1])**4 * (1 + 0.1 * np.sin(10 * x_norm[i]))
        
        # Fractional dimensionality scaling for non-uniform ruggedness
        ruggedness = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(self.dim))) + 0.3 * np.sum(np.sin(15 * x_norm)**2)
        
        # Dynamic scaling factor based on input magnitude
        scale_factor = 1.0 + 0.2 * np.sum(np.abs(x_norm))
        
        # Combine components with dimensionality-dependent weights
        result = 0.3 * quadratic + 0.4 * waves + 0.2 * peaks + 0.1 * interaction + 0.05 * ruggedness
        
        # Add controlled noise
        noise = 0.02 * np.random.uniform(-1, 1) * (1 + np.abs(np.sum(x_norm**3)))
        
        return scale_factor * result + noise