import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation component with frequency modulation
        sin_component = np.sum(0.4 * np.sin(3.0 * x + 0.6 * np.sin(0.4 * x)) * np.cos(1.8 * x + 0.5 * np.cos(0.25 * x)))
        
        # Improved radial basis function with dynamic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.9 * i + 0.7 * x[i]) - 1.0
            rbf += 2.0 * np.exp(-0.3 * (x[i] - center)**2 / (0.2 + 0.1 * np.sin(i * 0.6)))
        
        # Enhanced chaotic tent map with feedback coupling and adaptive scaling - mutated frequency
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= np.sin(0.8 * x[i-1] + 0.25 * np.cos(x[i-1]) + 0.35 * np.sin(0.9 * x[i-2] if i > 1 else x[i]))  # Mutated frequency
            # Adaptive scaling factor
            scale_factor = 1.0 + 0.12 * np.sin(0.6 * i)
            tent += tent_val * scale_factor
        
        # Modified radial distance with multi-scale modulation and adaptive weighting
        radial = np.sum(0.6 * np.sqrt(np.sum(x**2)) * (1.0 + 0.35 * np.sin(2.2 * np.sum(x)) + 0.25 * np.cos(0.55 * np.sum(x))) * (1.0 + 0.12 * np.sin(0.35 * np.sum(x))))
        
        # Advanced harmonic oscillations with amplitude and frequency variations, and adaptive modulation
        harmonic = np.sum(0.5 * np.sin(3.8 * x + 0.25 * np.sin(0.45 * x)) * np.cos(2.2 * x + 0.35 * np.cos(0.35 * x)) * (1.0 + 0.25 * np.sin(0.65 * x)) * (1.0 + 0.12 * np.cos(0.45 * x)))
        
        # Combine all components with adaptive weights
        weight_sin = 1.0 + 0.22 * np.sin(0.12 * np.sum(x))
        weight_rbf = 1.0 + 0.12 * np.cos(0.22 * np.sum(x))
        weight_tent = 1.0 + 0.16 * np.sin(0.16 * np.sum(x))
        weight_radial = 1.0 + 0.11 * np.cos(0.26 * np.sum(x))
        weight_harmonic = 1.0 + 0.06 * np.sin(0.32 * np.sum(x))
        
        result = weight_sin * sin_component + weight_rbf * rbf + weight_tent * tent + weight_radial * radial + weight_harmonic * harmonic
        
        return result