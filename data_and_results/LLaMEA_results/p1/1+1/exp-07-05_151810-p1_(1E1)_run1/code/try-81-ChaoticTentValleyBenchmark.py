import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = np.sum(0.3 * np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * x**2))
        
        # Radial basis function with chaotic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.7 * i + x[i] * 0.5) - 1.5
            rbf += 1.5 * np.exp(-0.5 * (x[i] - center)**2 / (0.3 + 0.2 * np.cos(i)))
        
        # Chaotic tent map component with spatial coupling
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.8 * x[i-1] + 0.3 * np.cos(x[i-1]))
            tent += tent_val
        
        # Radial distance from origin with sinusoidal modulation
        radial = np.sum(0.8 * np.sqrt(np.sum(x**2)) * (1.0 + 0.4 * np.sin(1.5 * np.sum(x))))
        
        # Multi-scale harmonic oscillations with varying amplitudes
        harmonic = np.sum(0.6 * np.sin(4.0 * x) * np.cos(3.0 * x) * (1.0 + 0.3 * np.sin(0.5 * x)))
        
        # Combine all components
        result = sin_component + rbf + tent + radial + harmonic
        
        return result