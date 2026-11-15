import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal oscillation with multi-frequency coupling and dynamic phase modulation
        sin_component = np.sum(0.5 * np.sin(3.0 * x + 0.6 * np.sin(0.4 * x) + 0.3 * np.cos(0.2 * x)) * 
                             np.cos(2.0 * x + 0.5 * np.cos(0.3 * x) + 0.4 * np.sin(0.1 * x)))
        
        # Improved radial basis function with dynamic center positioning and multi-scale variance
        rbf = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.9 * i + 0.7 * x[i]) - 1.5
            variance = 0.3 + 0.2 * np.sin(0.6 * i)
            rbf += 2.5 * np.exp(-0.4 * (x[i] - center)**2 / (0.25 + 0.15 * np.sin(i * 0.6) + variance))
        
        # Enhanced chaotic tent map with higher-order feedback coupling and multi-frequency modulation
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                # Higher-order feedback with triple coupling
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                tent_val *= (np.sin(0.8 * x[i-1] + 0.3 * np.cos(x[i-1]) + 0.4 * np.sin(0.9 * x[i-2] if i > 1 else x[i])) *
                           np.cos(0.6 * x[i-1] + 0.2 * np.sin(x[i-1]) + 0.5 * np.cos(0.7 * x[i-3] if i > 2 else x[i-1])) *
                           np.sin(0.5 * x[i-2] + 0.4 * np.cos(x[i-2]) + 0.3 * np.sin(0.8 * x[i-3] if i > 2 else x[i-2])))
            # Adaptive scaling factor with multi-dimensional modulation
            scale_factor = 1.0 + 0.2 * np.sin(0.6 * i) * np.cos(0.4 * x[i])
            tent += tent_val * scale_factor
        
        # Modified radial distance with multi-scale modulation, phase coupling, and adaptive weighting
        radial = np.sum(0.7 * np.sqrt(np.sum(x**2)) * 
                       (1.0 + 0.4 * np.sin(2.5 * np.sum(x)) + 0.3 * np.cos(0.6 * np.sum(x))) * 
                       (1.0 + 0.15 * np.sin(0.4 * np.sum(x)) + 0.1 * np.cos(0.3 * np.sum(x))) * 
                       (1.0 + 0.2 * np.sin(0.7 * np.sum(x))))
        
        # Advanced harmonic oscillations with amplitude, frequency, and phase variations, and multi-dimensional modulation
        harmonic = np.sum(0.6 * np.sin(4.0 * x + 0.3 * np.sin(0.5 * x) + 0.2 * np.cos(0.3 * x)) * 
                         np.cos(2.5 * x + 0.4 * np.cos(0.4 * x) + 0.3 * np.sin(0.2 * x)) * 
                         (1.0 + 0.3 * np.sin(0.7 * x) + 0.2 * np.cos(0.5 * x)) * 
                         (1.0 + 0.2 * np.cos(0.6 * x) + 0.1 * np.sin(0.4 * x)))
        
        # Combine all components with multi-dimensional adaptive weights
        weight_sin = 1.0 + 0.3 * np.sin(0.15 * np.sum(x) + 0.1 * np.cos(0.2 * np.sum(x)))
        weight_rbf = 1.0 + 0.2 * np.cos(0.25 * np.sum(x) + 0.15 * np.sin(0.3 * np.sum(x)))
        weight_tent = 1.0 + 0.25 * np.sin(0.2 * np.sum(x) + 0.2 * np.cos(0.15 * np.sum(x)))
        weight_radial = 1.0 + 0.15 * np.cos(0.3 * np.sum(x) + 0.1 * np.sin(0.25 * np.sum(x)))
        weight_harmonic = 1.0 + 0.1 * np.sin(0.35 * np.sum(x) + 0.05 * np.cos(0.4 * np.sum(x)))
        
        result = weight_sin * sin_component + weight_rbf * rbf + weight_tent * tent + weight_radial * radial + weight_harmonic * harmonic
        
        return result