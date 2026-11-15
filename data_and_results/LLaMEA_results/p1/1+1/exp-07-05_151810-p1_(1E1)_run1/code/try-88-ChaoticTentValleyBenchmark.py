import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        sin_component = np.sum(0.3 * np.sin(3.5 * x) * np.cos(2.5 * x) * np.exp(-0.1 * x**2))
        
        # Radial basis function with chaotic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 3.5 * np.sin(0.7 * i + x[i] * 0.5) - 1.7
            rbf += 1.7 * np.exp(-0.5 * (x[i] - center)**2 / (0.35 + 0.25 * np.cos(i)))
        
        # Chaotic tent map component with spatial coupling
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.9 * x[i-1] + 0.35 * np.cos(x[i-1]))
            tent += tent_val
        
        # Radial distance from origin with sinusoidal modulation
        radial = np.sum(0.9 * np.sqrt(np.sum(x**2)) * (1.0 + 0.45 * np.sin(1.6 * np.sum(x))))
        
        # Multi-scale harmonic oscillations with varying amplitudes
        harmonic = np.sum(0.65 * np.sin(4.2 * x) * np.cos(3.2 * x) * (1.0 + 0.35 * np.sin(0.55 * x)))
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.2 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Combine all components
        result = sin_component + rbf + tent + radial + harmonic + cross_term
        
        return result