import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like weights for radial interactions with slight modification
        self.fractal_weights = np.power(0.6, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation - slightly modified frequencies
        f2 = 0.0
        for i in range(self.dim):
            f2 += 0.8 * np.exp(-np.abs(x[i]) / (1.0 + 0.5 * np.sin(i * 0.35))) * np.cos(2.2 * x[i])
        
        # Polynomial chaos with exponential coupling - modified exponent
        f3 = 0.0
        for i in range(self.dim):
            f3 += 0.6 * (x[i]**4) * np.exp(-x[i]**2 / 10.0) * np.sin(1.7 * x[i])
        
        # Fractal-inspired radial interaction with varying scaling - altered decay rate
        f4 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)
            f4 += 0.7 * np.exp(-radial_dist / (6.0 + 0.3 * i)) * np.sin(3.2 * x[i])
        
        # Trigonometric coupling with dynamic frequency - modified frequency factor
        f5 = 0.0
        for i in range(self.dim - 1):
            freq = 2.2 + 0.8 * np.cos(i * 0.45)
            f5 += 0.5 * np.sin(freq * (x[i] + x[i+1]))
        
        # Cross-dimensional exponential interactions - modified coupling strength
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.45 * np.exp(-np.abs(x[i] - x[j]) / (2.0 + 0.1 * i)) * np.cos(1.3 * (x[i] + x[j]))
        
        # Adaptive harmonic oscillation with exponential decay - modified coefficients
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.65 * np.sin(2.7 * x[i]) * np.exp(-x[i]**2 / 8.0) * np.cos(1.9 * x[i])
        
        # Multi-peak exponential component with fractal coupling - modified peak positions
        f8 = 0.0
        for i in range(self.dim):
            peak_pos = 3.5 * np.cos(i * 0.65)
            f8 += 0.95 * np.exp(-((x[i] - peak_pos)**2) / 1.6) * np.sin(4.2 * x[i])
        
        # Radial power law with trigonometric modulation - modified exponent
        f9 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum(x**2)
            f9 += 0.55 * (x[i]**4) * np.exp(-radial_dist / 16.0) * np.cos(2.3 * x[i])
        
        # Fractal-like radial basis with sinusoidal coupling - modified decay
        f10 = 0.0
        for i in range(self.dim):
            f10 += 0.75 * np.exp(-np.sum((x - 1.6)**2) / (3.2 + 0.2 * i)) * np.sin(2.1 * x[i])
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.35 * np.log(self.dim + 1)
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)