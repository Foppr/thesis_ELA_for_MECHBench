import numpy as np

class SaddleClusterBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Saddle-point cluster component with varying curvature
        saddle = 0
        for i in range(self.dim):
            # Adaptive scaling based on dimension
            scale = 1.0 + 0.3 * np.sin(0.5 * i)
            saddle += scale * (x[i]**4 - 2 * x[i]**2) * np.cos(0.3 * x[i])
        
        # Adaptive polynomial component with dynamic exponents
        poly = 0
        for i in range(self.dim):
            exp = 5 + 3 * np.sin(0.4 * i)
            poly += (x[i]**exp) * np.exp(-0.1 * np.abs(x[i]))
        
        # Dynamic sine-cosine coupling with varying frequencies
        trig = 0
        for i in range(self.dim):
            freq1 = 3 + 2 * np.sin(0.6 * i)
            freq2 = 4 + 2 * np.cos(0.6 * i)
            trig += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Cross-term interaction with variable coupling strength
        cross = 0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling = 1.5 + 0.8 * np.sin(0.7 * (x[i] + x[j]))
            cross += coupling * x[i] * x[j] * np.sin(0.5 * (x[i] - x[j])**2)
        
        # Multi-scale radial component with clustered centers
        radial = 0
        centers = np.linspace(-4.5, 4.5, min(8, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.2 + 0.6 * np.cos(0.3 * i)
            radial += weight * np.exp(-0.3 * (x[i] - center)**2) * np.sin(4 * (x[i] - center))
        
        # Combine all components with dynamic weights
        return 0.25 * saddle + 0.22 * poly + 0.20 * trig + 0.23 * cross + 0.10 * radial