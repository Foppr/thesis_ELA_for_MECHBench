import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Exponentially decaying sinusoidal waves with varying frequencies and amplitudes
        waves = 0
        for i in range(1, self.dim + 1):
            freq = i * 3.0
            amp = np.exp(-0.1 * i)
            waves += amp * np.sin(freq * np.pi * x_norm[i-1]) * np.cos(freq * np.pi * x_norm[i-1])
        
        # Adaptive peak heights based on dimensionality
        peaks = 0
        for i in range(1, self.dim + 1):
            center = np.sin(i * np.pi / 4.0)
            height = 1.0 + 0.5 * np.sin(i * np.pi / 3.0)
            peaks += height * np.exp(-20 * (x_norm[i-1] - center)**2)
        
        # Cross-dimensional interaction terms with exponential decay
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-5 * np.abs(x_norm[i] - x_norm[i+1])) * (x_norm[i] + x_norm[i+1])**2
        
        # Fractional polynomial with varying exponents
        poly = np.sum(np.abs(x_norm)**(1.5 + np.abs(x_norm)))
        
        # Add noise with dimensionality-dependent intensity
        noise = np.random.normal(0, 0.01 * self.dim)
        
        # Combine all components with nonlinear weighting
        result = 0.4 * waves + 0.3 * peaks + 0.2 * cross_terms + 0.1 * poly + noise
        
        return result