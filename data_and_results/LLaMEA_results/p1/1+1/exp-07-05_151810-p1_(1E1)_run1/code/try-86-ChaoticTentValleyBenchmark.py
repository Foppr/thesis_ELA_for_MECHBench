import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with multi-scale frequencies
        sin_component = np.sum(0.4 * np.sin(2.5 * x) * np.cos(1.5 * x) * np.exp(-0.15 * x**2))
        
        # Improved radial basis function with chaotic center positioning and adaptive widths
        rbf = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.8 * i + x[i] * 0.6) - 1.2
            width = 0.4 + 0.3 * np.sin(0.5 * i)
            rbf += 1.2 * np.exp(-0.5 * (x[i] - center)**2 / (0.2 + width * np.cos(i)))
        
        # Enhanced chaotic tent map component with dynamic coupling
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.9 * x[i-1] + 0.4 * np.cos(x[i-1]) + 0.2 * np.sin(x[i-1]**2))
            tent += tent_val * (1.0 + 0.1 * np.sin(0.7 * i))
        
        # Modified radial distance from origin with enhanced sinusoidal modulation
        radial = np.sum(0.9 * np.sqrt(np.sum(x**2)) * (1.0 + 0.5 * np.sin(1.2 * np.sum(x))))
        
        # Enhanced multi-scale harmonic oscillations with varying amplitudes and phases
        harmonic = np.sum(0.7 * np.sin(3.5 * x) * np.cos(2.5 * x) * (1.0 + 0.4 * np.sin(0.6 * x) + 0.2 * np.cos(0.3 * x)))
        
        # Additional coupling term between dimensions
        coupling = 0.3 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # Combine all components
        result = sin_component + rbf + tent + radial + harmonic + coupling
        
        return result