import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        base = np.sum(x**2)
        
        # Fractal-like structure using trigonometric components with adaptive frequencies
        fractal = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on coordinate value
            freq = 1.0 + 0.5 * np.sin(x[i] / 2.0)
            # Self-similar pattern with multiple scales
            fractal += (np.sin(freq * x[i]) + np.cos(freq * x[i])) * \
                      (1.0 + 0.3 * np.sin(2 * freq * x[i])) * \
                      np.exp(-0.1 * np.abs(x[i]))
        
        # Rotated multi-modal components
        rotated = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional interaction with rotation
                rotated += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                          np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic-like chaotic component
            chaotic += np.sin(10 * np.sin(x[i])) * np.cos(7 * np.cos(x[i])) * \
                      np.exp(-0.03 * x[i]**2)
        
        # Multi-scale sinusoidal interference
        interference = 0.0
        for i in range(self.dim):
            interference += np.sin(3 * x[i]) * np.cos(4 * x[i]) * \
                          np.sin(5 * x[i]) * np.cos(6 * x[i]) * \
                          np.exp(-0.02 * x[i]**2)
        
        # Asymmetric penalty for large values
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * np.abs(x[i])**3 * np.sin(x[i])
        
        return base + 0.5 * fractal + 0.3 * rotated + 0.4 * chaotic + 0.2 * interference + 0.1 * penalty