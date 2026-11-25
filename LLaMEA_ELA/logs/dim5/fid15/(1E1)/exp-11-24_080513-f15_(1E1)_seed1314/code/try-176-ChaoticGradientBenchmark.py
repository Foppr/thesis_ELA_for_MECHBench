import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with modified logistic map
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10)
        
        # Improved gradient-based component with dynamic conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.8) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 3) * np.exp(-0.25 * x_normalized[i]**2)
        
        # Enhanced saddle point region with coupled interactions
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Modified discontinuous region with enhanced step function
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i])
        
        # Enhanced harmonic interaction with multi-scale coupling
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0)
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with improved conditioning
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**2
        
        # Combined fitness with optimized weights and added bias term
        return (0.32 * chaotic + 0.28 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.08 * harmonic + 0.05 * nonlin + 0.02)