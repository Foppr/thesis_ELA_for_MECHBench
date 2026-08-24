import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with frequency modulation
        sin_component = np.sum(0.4 * np.sin(2.5 * x + 0.5 * np.sin(0.3 * x)) * np.cos(1.5 * x + 0.4 * np.cos(0.2 * x)))
        
        # Improved radial basis function with dynamic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.8 * i + 0.6 * x[i]) - 1.0
            rbf += 2.0 * np.exp(-0.3 * (x[i] - center)**2 / (0.2 + 0.1 * np.sin(i * 0.5)))
        
        # Enhanced chaotic tent map with feedback coupling
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.7 * x[i-1] + 0.2 * np.cos(x[i-1]) + 0.3 * np.sin(x[i-2] if i > 1 else x[i]))
            tent += tent_val
        
        # Modified radial distance with multi-scale modulation
        radial = np.sum(0.6 * np.sqrt(np.sum(x**2)) * (1.0 + 0.3 * np.sin(2.0 * np.sum(x)) + 0.2 * np.cos(0.5 * np.sum(x))))
        
        # Advanced harmonic oscillations with amplitude and frequency variations
        harmonic = np.sum(0.5 * np.sin(3.5 * x + 0.2 * np.sin(0.4 * x)) * np.cos(2.0 * x + 0.3 * np.cos(0.3 * x)) * (1.0 + 0.2 * np.sin(0.6 * x)))
        
        # Combine all components
        result = sin_component + rbf + tent + radial + harmonic
        
        return result