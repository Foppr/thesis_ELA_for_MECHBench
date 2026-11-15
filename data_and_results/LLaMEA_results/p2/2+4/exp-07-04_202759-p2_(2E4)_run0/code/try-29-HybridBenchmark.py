import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees and chaotic scaling
        poly = np.sum(x**6) + 0.7 * np.sum(x**5) + 0.3 * np.sum(x**4) + 0.1 * np.sum(x**3)
        
        # Trigonometric component with chaotic modulation and varying frequencies
        trig = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x[i] * 0.5)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.05 * x[i]**2)
        
        # Radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 1.0 + 0.5 * np.sin(0.3 * i)
            rbf += weight * np.exp(-0.3 * (x[i] - center)**2) * np.sin(4 * (x[i] - center))
        
        # Cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 1.0 + 0.3 * np.sin(0.2 * (x[i] + x[j]))
            cross += coupling * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] - x[j])**2)
        
        # Chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.1 * np.sin(2 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.1 * np.cos(2 * x[i])))
        
        # Additional chaotic perturbation and enhanced non-linearity
        perturbation = 0
        for i in range(self.dim):
            perturbation += np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2) * (1 + 0.2 * np.sin(0.5 * x[i]))
        
        # Scale and combine all components with dynamic weights
        return 0.25 * poly + 0.35 * trig + 0.25 * rbf + 0.1 * cross + 0.05 * chaotic + 0.05 * perturbation