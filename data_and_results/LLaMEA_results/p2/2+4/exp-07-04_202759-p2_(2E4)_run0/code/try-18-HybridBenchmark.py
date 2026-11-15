import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees and conditioning
        poly = np.sum(x**4) + 0.3 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Trigonometric component with varying frequencies, phases, and modulation
        trig = 0
        for i in range(self.dim):
            trig += np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.05 * x[i]**2) + 0.5 * np.sin(5 * x[i])
        
        # Radial basis function component with multiple centers and varying influence
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rbf += np.exp(-0.3 * (x[i] - center)**2) * np.sin(4 * (x[i] - center)) * (1 + 0.1 * np.abs(x[i]))
        
        # Enhanced cross-term interactions with non-linear coupling
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            cross += (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] - x[j])**2) * np.exp(-0.1 * (x[i] + x[j])**2)
        
        # Additional high-frequency oscillation for increased complexity
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(10 * x[i]) * np.cos(7 * x[i]) * (1 + 0.05 * x[i]**2)
        
        # Scale and combine components with adjusted weights
        return 0.25 * poly + 0.35 * trig + 0.25 * rbf + 0.1 * cross + 0.05 * high_freq