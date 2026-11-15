import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation with multi-frequency coupling
        sin_component = np.sum(0.5 * np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.15 * x**2) * (1.0 + 0.2 * np.sin(2.0 * x)))
        
        # Enhanced radial basis function with dynamic centers and multi-scale variance
        rbf = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.8 * i + x[i] * 0.6) - 1.2
            variance = 0.4 + 0.3 * np.cos(i * 0.5 + x[i] * 0.3)
            rbf += 2.0 * np.exp(-0.5 * (x[i] - center)**2 / variance)
        
        # Chaotic tent map with multi-dimensional coupling and gradient modulation
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.9 * x[i-1] + 0.4 * np.cos(x[i-1]) + 0.3 * np.sin(x[i-2] if i >= 2 else x[i]))
            tent += tent_val * (1.0 + 0.1 * np.sin(1.2 * x[i]))
        
        # Enhanced radial distance with multi-scale harmonic modulation and gradient field
        radial = np.sum(1.0 * np.sqrt(np.sum(x**2)) * (1.0 + 0.5 * np.sin(2.0 * np.sum(x)) + 0.3 * np.cos(1.5 * np.sum(x))))
        
        # Multi-scale harmonic oscillations with amplitude and frequency modulation
        harmonic = np.sum(0.8 * np.sin(5.0 * x) * np.cos(4.0 * x) * (1.0 + 0.4 * np.sin(0.7 * x) + 0.3 * np.cos(0.6 * x)))
        
        # Gradient attraction field with multiple local minima
        attraction = 0.0
        for i in range(self.dim):
            attraction += 0.5 * (x[i] - 1.0)**2 * (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Combine all components
        result = sin_component + rbf + tent + radial + harmonic + attraction
        
        return result