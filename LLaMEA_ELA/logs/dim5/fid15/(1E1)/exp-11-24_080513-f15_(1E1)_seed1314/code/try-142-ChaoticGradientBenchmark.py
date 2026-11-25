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
        
        # Saddle point embedded region with enhanced hyperbolic tangent coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3  # Cubic difference
        
        # Discontinuous region using step function and sinusoidal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(6 * x_normalized[i]) * np.cos(4 * x_normalized[i])
        
        # Multi-scale harmonic interaction with exponential decay
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 3.0)  # Reduced decay rate
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(2 * (x_normalized[i] - x_normalized[j]))  # Changed frequencies
        
        # Additional nonlinearity for better conditioning
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**4) * np.sin(x_normalized[i])**2
        
        # Combined fitness with modified scaling
        return (0.3 * chaotic + 0.25 * gradient + 0.18 * saddle + 
                0.12 * discontinuous + 0.08 * harmonic + 0.07 * nonlin)