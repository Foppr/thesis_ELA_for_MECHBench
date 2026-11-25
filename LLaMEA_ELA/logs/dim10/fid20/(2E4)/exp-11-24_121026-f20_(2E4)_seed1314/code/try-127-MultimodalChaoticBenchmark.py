import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial base with conditioning
        f1 = np.sum(x_norm**4)
        
        # Trigonometric modulations with dynamic frequencies and adaptive amplitudes
        f2 = np.sum(np.sin(15 * x_norm) * np.cos(10 * x_norm) * (1 + 0.3 * np.sin(7 * x_norm)))
        
        # Radial basis function components with chaotic scaling
        rb_centers = np.linspace(-1, 1, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            center = rb_centers[i]
            f3 += np.exp(-5 * (x_norm - center)**2) * np.sin(8 * (x_norm - center))
        
        # Adaptive chaotic interaction terms with dynamic coupling weights
        weights = 1 + 0.5 * np.sin(12 * x_norm)
        f4 = np.sum(weights * x_norm**3 * np.cos(9 * x_norm))
        
        # Multi-scale sinusoidal chaos with varying amplitudes and frequencies
        f5 = np.sum(np.sin(25 * x_norm) * np.cos(18 * x_norm) * np.sin(14 * x_norm) * (1 + 0.2 * np.cos(16 * x_norm)))
        
        # Fractional power with logarithmic barrier and chaotic modulation
        f6 = np.sum(np.abs(x_norm)**1.5 * np.log(1 + np.abs(x_norm)) * (1 + 0.25 * np.sin(13 * x_norm)))
        
        # Cross-dimensional interaction with dynamic coupling and nonlinear transformation
        f7 = 0.0
        for i in range(self.dim - 1):
            f7 += (x_norm[i] * x_norm[i+1]) * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2)
        
        # Enhanced hyperbolic and exponential interaction with chaotic feedback
        f8 = np.sum(np.tanh(6 * x_norm) * np.exp(-0.3 * x_norm**2) * (1 + 0.3 * np.sin(11 * x_norm)))
        
        # Mixed polynomial and trigonometric terms with dynamic scaling
        f9 = np.sum((x_norm**5 - 0.7 * x_norm**3 + 0.2 * x_norm)**2 * np.cos(8 * x_norm))
        
        # Adaptive chaotic modulation with boundary influence and frequency coupling
        f10 = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.4 * x_norm**2) * (1 + 0.15 * np.sin(18 * x_norm)))
        
        return f1 + 0.3 * f2 + 0.25 * f3 + 0.2 * f4 + 0.15 * f5 + 0.18 * f6 + 0.12 * f7 + 0.15 * f8 + 0.1 * f9 + 0.08 * f10