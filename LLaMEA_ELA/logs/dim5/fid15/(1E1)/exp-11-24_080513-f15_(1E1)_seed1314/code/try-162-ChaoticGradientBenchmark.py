import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with noise injection
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            x_prev = 0.5 + np.random.normal(0, 0.01)  # Add noise
            for _ in range(20):  # More iterations for chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10) * (1 + 0.1 * np.random.uniform(-1, 1))
        
        # Enhanced gradient with adaptive conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 5.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with polynomial coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                saddle += (np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * 
                          (x_normalized[i] - x_normalized[j])**3 + 
                          0.1 * np.sin(x_normalized[i]) * np.cos(x_normalized[j]))
        
        # Discontinuous region with modified step function
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i]) * (1 + 0.2 * np.sin(i))
        
        # Multi-scale harmonic interaction with dynamic weights
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0) * (1 + 0.3 * np.sin(i + j))
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(2 * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with coupling
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3 + 0.1 * np.cos(x_normalized[i])
        
        # Combined fitness with new scaling factors
        return (0.25 * chaotic + 0.3 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.08 * harmonic + 0.02 * nonlin)