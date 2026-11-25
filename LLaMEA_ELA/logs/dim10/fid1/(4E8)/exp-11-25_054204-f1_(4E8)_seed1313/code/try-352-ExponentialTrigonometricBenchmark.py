import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like weights for radial interactions
        self.fractal_weights = np.power(0.5, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        f2 = 0.0
        for i in range(self.dim):
            f2 += 0.8 * np.exp(-np.abs(x[i]) / (1.0 + 0.5 * np.sin(i * 0.3))) * np.cos(2.0 * x[i])
        
        # Polynomial chaos with exponential coupling
        f3 = 0.0
        for i in range(self.dim):
            f3 += 0.6 * (x[i]**3) * np.exp(-x[i]**2 / 10.0) * np.sin(1.5 * x[i])
        
        # Fractal-inspired radial interaction with varying scaling
        f4 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)
            f4 += 0.7 * np.exp(-radial_dist / (5.0 + 0.3 * i)) * np.sin(3.0 * x[i])
        
        # Trigonometric coupling with dynamic frequency
        f5 = 0.0
        for i in range(self.dim - 1):
            freq = 2.0 + 0.8 * np.cos(i * 0.4)
            f5 += 0.5 * np.sin(freq * (x[i] + x[i+1]))
        
        # Cross-dimensional exponential interactions
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.4 * np.exp(-np.abs(x[i] - x[j]) / (2.0 + 0.1 * i)) * np.cos(1.2 * (x[i] + x[j]))
        
        # Adaptive harmonic oscillation with exponential decay
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.6 * np.sin(2.5 * x[i]) * np.exp(-x[i]**2 / 8.0) * np.cos(1.8 * x[i])
        
        # Multi-peak exponential component with fractal coupling
        f8 = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.cos(i * 0.6)
            f8 += 0.9 * np.exp(-((x[i] - peak_pos)**2) / 1.5) * np.sin(4.0 * x[i])
        
        # Radial power law with trigonometric modulation
        f9 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum(x**2)
            f9 += 0.5 * (x[i]**4) * np.exp(-radial_dist / 15.0) * np.cos(2.2 * x[i])
        
        # Fractal-like radial basis with sinusoidal coupling
        f10 = 0.0
        for i in range(self.dim):
            f10 += 0.7 * np.exp(-np.sum((x - 1.5)**2) / (3.0 + 0.2 * i)) * np.sin(2.0 * x[i])
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)