import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Piecewise logistic map transformation for chaotic behavior
        chaotic = 0.0
        r = 3.85
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(12):  # Iterate to reach chaotic regime
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 11) * np.cos(x_normalized[i] * x_prev * 6.5)
        
        # Gradient-based component with varying conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 2.5 * np.sin(i * 0.4)
            gradient += condition * (x_normalized[i] ** 3) * np.exp(-0.6 * x_normalized[i]**2)
        
        # Enhanced saddle point embedded region with hyperbolic tangent
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**2.5
        
        # Discontinuous region using step function and sinusoidal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(4.5 * x_normalized[i]) * np.cos(3.2 * x_normalized[i])
        
        # Multi-scale harmonic interaction with modified exponential decay
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 4.0)  # Increased decay rate
                harmonic += weight * np.sin(2.2 * (x_normalized[i] + x_normalized[j])) * np.cos(1.8 * (x_normalized[i] - x_normalized[j]))
        
        # Combined fitness with adaptive scaling
        return (0.27 * chaotic + 0.28 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.10 * harmonic)