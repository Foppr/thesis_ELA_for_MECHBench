import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with frequency modulation
        sin_component = np.sum(0.4 * np.sin(2.7 * x + 0.5 * np.sin(0.35 * x)) * np.cos(1.6 * x + 0.4 * np.cos(0.25 * x)))
        
        # Improved radial basis function with dynamic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.85 * i + 0.6 * x[i]) - 1.0
            rbf += 2.2 * np.exp(-0.32 * (x[i] - center)**2 / (0.21 + 0.11 * np.sin(i * 0.52)))
        
        # Enhanced chaotic tent map with feedback coupling and adaptive scaling - mutated frequency
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.75 * x[i-1] + 0.22 * np.cos(x[i-1]) + 0.32 * np.sin(0.85 * x[i-2] if i > 1 else x[i]))  # Mutated frequency
            # Adaptive scaling factor
            scale_factor = 1.0 + 0.11 * np.sin(0.52 * i)
            tent += tent_val * scale_factor
        
        # Modified radial distance with multi-scale modulation and adaptive weighting
        radial = np.sum(0.62 * np.sqrt(np.sum(x**2)) * (1.0 + 0.32 * np.sin(2.1 * np.sum(x)) + 0.21 * np.cos(0.52 * np.sum(x))) * (1.0 + 0.11 * np.sin(0.31 * np.sum(x))))
        
        # Advanced harmonic oscillations with amplitude and frequency variations, and adaptive modulation
        harmonic = np.sum(0.52 * np.sin(3.6 * x + 0.21 * np.sin(0.41 * x)) * np.cos(2.1 * x + 0.31 * np.cos(0.31 * x)) * (1.0 + 0.21 * np.sin(0.61 * x)) * (1.0 + 0.11 * np.cos(0.41 * x)))
        
        # Combine all components with adaptive weights
        weight_sin = 1.0 + 0.21 * np.sin(0.11 * np.sum(x))
        weight_rbf = 1.0 + 0.11 * np.cos(0.21 * np.sum(x))
        weight_tent = 1.0 + 0.16 * np.sin(0.16 * np.sum(x))
        weight_radial = 1.0 + 0.11 * np.cos(0.26 * np.sum(x))
        weight_harmonic = 1.0 + 0.051 * np.sin(0.31 * np.sum(x))
        
        result = weight_sin * sin_component + weight_rbf * rbf + weight_tent * tent + weight_radial * radial + weight_harmonic * harmonic
        
        return result