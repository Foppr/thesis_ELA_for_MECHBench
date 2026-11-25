import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Piecewise logistic map transformation for chaotic behavior
        chaotic = 0.0
        r = 3.8
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(15):  # Iterate to reach chaotic regime
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 12) * np.cos(x_normalized[i] * x_prev * 8)
        
        # Gradient-based component with varying conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 3.0 * np.sin(i * 0.7)
            gradient += condition * (x_normalized[i] ** 3) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Enhanced saddle point embedded region with hyperbolic tangent
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Discontinuous region using step function and sinusoidal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(6 * x_normalized[i]) * np.cos(4 * x_normalized[i])
        
        # Multi-scale harmonic interaction with exponential decay (modified weights)
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 4.0)  # Increased decay rate
                harmonic += weight * np.sin(3 * (x_normalized[i] + x_normalized[j])) * np.cos(3 * (x_normalized[i] - x_normalized[j]))
        
        # Combined fitness with adaptive scaling
        return (0.3 * chaotic + 0.25 * gradient + 0.2 * saddle + 
                0.1 * discontinuous + 0.15 * harmonic)