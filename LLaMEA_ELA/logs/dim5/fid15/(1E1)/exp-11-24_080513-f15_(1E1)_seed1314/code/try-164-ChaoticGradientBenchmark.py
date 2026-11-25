import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with modified logistic map and variable coupling
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Enhanced gradient component with variable conditioning and cubic terms
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.9) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with higher-order coupling and hyperbolic functions
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Multi-modal discontinuous region with multiple step functions and sinusoidal modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * (np.sin(7 * x_normalized[i]) + np.cos(5 * x_normalized[i])) * np.exp(-0.3 * np.abs(x_normalized[i]))
        
        # Enhanced harmonic interaction with multi-scale exponential decay and cross-terms
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0)
                harmonic += weight * (np.sin(4 * (x_normalized[i] + x_normalized[j])) + np.cos(4 * (x_normalized[i] - x_normalized[j])))
        
        # Enhanced nonlinearity with polynomial and trigonometric combinations
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3 + 0.5 * x_normalized[i]**2
        
        # Combined fitness with adjusted scaling factors and added noise term
        noise = 0.01 * np.sum(np.sin(x_normalized * 10))
        return (0.28 * chaotic + 0.22 * gradient + 0.18 * saddle + 
                0.18 * discontinuous + 0.08 * harmonic + 0.06 * nonlin + noise)