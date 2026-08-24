import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Ultra-high frequency sinusoidal oscillation with nested chaotic modulation
        sin_component = np.sum(1.2 * np.sin(10.0 * x + 0.8 * np.sin(3.0 * x + 0.5 * np.sin(2.0 * x))) * 
                             np.cos(7.0 * x + 0.6 * np.cos(4.0 * x + 0.4 * np.cos(3.0 * x))))
        
        # Enhanced radial basis function with fractal-like center positioning and multi-scale variance
        rbf = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(1.2 * i + 0.9 * x[i]) * np.cos(0.7 * i) - 1.5 * np.sin(0.3 * x[i])
            rbf += 3.0 * np.exp(-0.5 * (x[i] - center)**2 / (0.3 + 0.2 * np.sin(i * 0.8 + 0.4 * np.cos(i * 0.6))))
        
        # Mutated chaotic tent map with higher-order feedback coupling and frequency chaos
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                # Higher-order chaotic feedback with nested sinusoidal modulation
                tent_val *= np.sin(1.2 * x[i-1] + 0.8 * np.cos(x[i-1]) + 0.6 * np.sin(1.1 * x[i-2] if i > 1 else x[i]) + 
                                  0.4 * np.cos(0.9 * x[i-3] if i > 2 else x[i-1]))
            # Enhanced adaptive scaling with exponential factor
            scale_factor = 1.0 + 0.2 * np.sin(0.8 * i + 0.3 * np.cos(i * 0.5))
            tent += tent_val * scale_factor
        
        # Multi-scale radial distance with ultra-high frequency modulation and fractal weighting
        radial = np.sum(1.0 * np.sqrt(np.sum(x**2)) * (1.0 + 0.5 * np.sin(5.0 * np.sum(x)) + 0.4 * np.cos(3.0 * np.sum(x))) * 
                       (1.0 + 0.2 * np.sin(0.7 * np.sum(x)) + 0.1 * np.cos(0.9 * np.sum(x))) * 
                       (1.0 + 0.15 * np.sin(1.3 * np.sum(x)) + 0.1 * np.cos(1.1 * np.sum(x))))
        
        # Ultra-complex harmonic oscillations with amplitude, frequency, and phase modulation
        harmonic = np.sum(0.8 * np.sin(5.0 * x + 0.5 * np.sin(2.5 * x + 0.3 * np.sin(1.5 * x))) * 
                         np.cos(4.0 * x + 0.4 * np.cos(3.0 * x + 0.2 * np.cos(2.0 * x))) * 
                         (1.0 + 0.3 * np.sin(0.8 * x) + 0.2 * np.cos(0.6 * x)) * 
                         (1.0 + 0.25 * np.sin(0.5 * x) + 0.15 * np.cos(0.4 * x)))
        
        # Combine all components with highly adaptive weights and chaotic modulation
        weight_sin = 1.0 + 0.3 * np.sin(0.2 * np.sum(x) + 0.1 * np.cos(0.3 * np.sum(x)))
        weight_rbf = 1.0 + 0.2 * np.cos(0.3 * np.sum(x) + 0.15 * np.sin(0.2 * np.sum(x)))
        weight_tent = 1.0 + 0.25 * np.sin(0.25 * np.sum(x) + 0.2 * np.cos(0.15 * np.sum(x)))
        weight_radial = 1.0 + 0.15 * np.cos(0.4 * np.sum(x) + 0.1 * np.sin(0.25 * np.sum(x)))
        weight_harmonic = 1.0 + 0.1 * np.sin(0.35 * np.sum(x) + 0.05 * np.cos(0.3 * np.sum(x)))
        
        result = weight_sin * sin_component + weight_rbf * rbf + weight_tent * tent + weight_radial * radial + weight_harmonic * harmonic
        
        return result