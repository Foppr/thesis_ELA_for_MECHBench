import numpy as np

class ChaoticAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Sinusoidal wave interference with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = 1.5 * (1.0 + 0.3 * np.cos(i * 0.9))
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Polynomial potential with fractional powers and mixed signs
        f3 = 0.05 * np.sum((x**3.7 - 0.8 * x**2.9 + 0.4 * x**1.8 - 0.2 * x) / self.dim)
        
        # Gradient-based attraction fields with repulsion centers
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Attraction to multiple fixed points with varying strengths
            attractors = [1.0, -1.5, 2.3, -2.8]
            attraction = 0.0
            for a in attractors:
                dist = np.abs(xi - a)
                # Exponential attraction with distance-dependent scaling
                attraction += np.exp(-dist**2) * (1.0 + 0.2 * np.sin(dist * 3.0))
            f4 -= attraction
        
        # Multi-scale chaotic modulation using logistic map behavior
        f5 = 0.15 * np.sum(np.sin(20.0 * np.sin(5.0 * x)) * np.cos(15.0 * np.cos(7.0 * x)))
        
        # Cross-dimensional interaction with asymmetric coupling
        f6 = 0.08 * np.sum((x[:-1]**1.7 + 0.6 * x[1:]**2.3) * np.sin(x[:-1] * x[1:]))
        
        # Fractional Brownian motion-inspired roughness with varying Hurst exponent
        f7 = 0.1 * np.sum(np.abs(x)**1.4 * np.cos(18.0 * x))
        
        # Asymmetric saddle points with varying curvature and chaotic modulation
        f8 = 0.2 * np.sum((x**3.2 + 0.5 * x**2.1 - 0.7 * x) * np.exp(-0.15 * np.abs(x)) * np.sin(12.0 * x))
        
        # Combine all components with adjusted weights for improved fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8