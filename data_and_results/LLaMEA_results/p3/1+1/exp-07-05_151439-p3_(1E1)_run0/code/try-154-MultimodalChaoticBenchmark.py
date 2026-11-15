import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        rbfs = 0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        widths = 0.5 + 0.3 * np.sin(np.arange(self.dim) * 0.7)
        
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0
            rbfs += np.exp(-np.sum((x - center)**2) / (2 * widths[i]**2))
        
        # Sinusoidal oscillation component with multiple frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                         np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_coupling += np.exp(-0.1 * (i + 1)) * np.abs(x[i] - x[i+1])**2
        
        # Polynomial component with alternating signs
        poly_term = np.sum((-1)**np.arange(self.dim) * (x**2 + 0.1 * x**3 + 0.01 * x**4))
        
        # Multi-scale harmonic component
        harmonic = 0
        for k in range(1, 6):
            harmonic += np.sin(k * np.pi * x / 2.5) * np.cos(k * np.pi * x / 3.0)
        
        # Combine all components with adaptive weights
        weights = [0.3 + 0.1 * np.sin(self.dim * 0.5), 
                  0.25 + 0.1 * np.cos(self.dim * 0.7),
                  0.2 + 0.05 * np.sin(self.dim * 1.1),
                  0.15 + 0.05 * np.cos(self.dim * 1.3),
                  0.1 + 0.03 * np.sin(self.dim * 1.7)]
        
        result = (weights[0] * rbfs + 
                 weights[1] * sin_term + 
                 weights[2] * cross_coupling + 
                 weights[3] * poly_term + 
                 weights[4] * harmonic)
        
        # Add small random noise for robustness
        noise = 0.001 * np.random.randn()
        
        return result + noise