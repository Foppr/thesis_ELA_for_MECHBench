import numpy as np

class MultimodalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add exponentially decaying sinusoidal wells
        for i in range(1, min(self.dim + 1, 20)):
            # Create wells with exponentially increasing frequency and decreasing amplitude
            freq = 2 ** i
            amp = 10.0 / (1.0 + i * 0.5)
            
            # Well centers with chaotic distribution
            center = 5.0 * np.sin(i * 3.14159 * x[i % self.dim] * 0.1) if self.dim > 0 else 5.0 * np.sin(i * 3.14159)
            
            # Sinusoidal well with exponential decay
            well = amp * np.exp(-0.5 * ((x[i % self.dim] - center) / (0.5 * i))**2) * np.sin(freq * (x[i % self.dim] - center))
            result += well
        
        # Add cross-dimensional interference terms
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):  # Limited coupling to maintain tractability
                # Interference pattern between dimensions
                interference = 2.0 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += interference
        
        # Add high-frequency noise component
        noise = 0.5 * np.sum(np.sin(50 * x) + np.cos(30 * x) + np.sin(15 * x))
        
        # Add fractal-like scaling terms
        fractal = 0.3 * np.sum(np.abs(x)**1.7 + np.sin(x)**2)
        
        # Add dimensionality-dependent modulation
        modulator = 1.0 + 0.5 * np.sin(self.dim * 0.5)
        
        return result * modulator + noise + fractal