import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base fractal component using recursive sine waves with diminishing amplitude
        fractal = 0.0
        for i in range(1, 6):
            freq = 2 ** i
            amp = 1.0 / (2 ** (i - 1))
            fractal += amp * np.sin(freq * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2))
        
        # Multi-scale Gaussian peaks with fractal-like distribution
        peaks = 0.0
        scales = [0.5, 1.0, 2.0, 3.0]
        for scale in scales:
            # Generate fractal peak locations
            peak_locs = np.sin(np.linspace(0, 2*np.pi, self.dim) * scale) * 0.5
            peak_locs = np.clip(peak_locs, -1, 1)
            peaks += np.exp(-5 * np.sum((x_norm - peak_locs)**2))
        
        # Chaotic logistic map component with varying control parameters
        logistic = 0.0
        r_values = [3.5, 3.8, 3.9, 4.0]
        for r in r_values:
            logistic += np.sum(np.sin(r * x_norm * (1 - x_norm)) * np.cos(2 * x_norm))
        
        # Fractional Brownian motion inspired component with Hurst parameter
        hurst = 0.3
        fbm = 0.0
        for i in range(1, 8):
            fbm += (1.0 / (2**i)) * np.sin(2**i * np.pi * x_norm) * (2**i)**(-hurst)
        
        # Cross-dimensional coupling with scale-dependent interactions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**4 * np.exp(-0.1 * np.abs(x_norm[i] + x_norm[i+1]))
        
        # Combine all components with dynamic weighting based on input magnitude
        magnitude = np.sqrt(np.sum(x_norm**2))
        weights = [0.25, 0.3, 0.15, 0.1, 0.2]
        result = weights[0] * fractal + weights[1] * peaks + weights[2] * logistic + weights[3] * fbm + weights[4] * coupling
        
        # Add scale-invariant noise term
        noise = 0.01 * np.random.uniform(-1, 1) * (1 + 0.5 * magnitude)
        
        return result + noise