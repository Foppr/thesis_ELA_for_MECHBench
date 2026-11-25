import numpy as np

class RuggedChaoticPeaksBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Multiple Gaussian peaks with varying heights and widths
        for i in range(10):
            peak_center = np.random.uniform(-4.0, 4.0, self.dim)
            peak_height = np.random.uniform(0.5, 2.0)
            peak_width = np.random.uniform(0.5, 2.0)
            
            dist = np.sum((x - peak_center)**2)
            result += peak_height * np.exp(-dist / (2.0 * peak_width**2))
        
        # Sinusoidal modulation across dimensions
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(3.0 * xi) * np.cos(2.0 * xi) * (1.0 + 0.3 * np.sin(7.0 * xi))
        
        # Chaotic attractor component using logistic map dynamics
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map with parameter control
            r = 3.9  # Chaos-inducing parameter
            logistic_val = r * xi * (1.0 - xi)
            chaotic_term += 0.3 * np.sin(logistic_val * 10.0) * np.cos(logistic_val * 7.0)
        result += chaotic_term
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling_strength = 0.2 * np.exp(-abs(xi - xj) / 3.0)
                result += coupling_strength * np.sin(xi + xj) * np.cos(xi - xj)
        
        # Multi-scale harmonic interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(15.0 * xi) * np.cos(12.0 * xi) * (1.0 + 0.2 * np.sin(5.0 * xi))
        
        # Radial component with chaotic perturbation
        r = np.sqrt(np.sum(x**2))
        result += 0.6 * r * np.sin(4.0 * r) * np.cos(3.0 * r) * (1.0 + 0.1 * np.sin(8.0 * r))
        
        # Additional high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise += 0.2 * np.sin(50.0 * xi) * np.cos(30.0 * xi)
        result += noise
        
        return result