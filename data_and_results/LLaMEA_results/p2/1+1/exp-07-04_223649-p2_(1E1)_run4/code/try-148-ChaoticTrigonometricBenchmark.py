import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.9  # Logistic map parameter
        self.noise_level = 0.1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic logistic map component
        chaotic = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Logistic map with current dimension value as parameter
                chaotic += np.sin(self.r * x[i] * (1 - x[i])) * np.cos(self.r * x[i+1] * (1 - x[i+1]))
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_coupling += np.sin(2.0 * (x[i] + x[j])) * np.cos(3.0 * (x[i] - x[j]))
        
        # Adaptive noise component
        adaptive_noise = 0.0
        for i in range(self.dim):
            noise_factor = 1.0 / (1.0 + np.exp(-x[i]))
            adaptive_noise += noise_factor * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Multi-scale periodic peaks
        peaks = 0.0
        for i in range(self.dim):
            peaks += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle point interactions
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                saddle += (x[i]**2 - x[i+1]**2) * np.sin(x[i] + x[i+1])
        
        # Exponential decay with trigonometric modulation
        exp_trig = 0.0
        for i in range(self.dim):
            exp_trig += np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Combined result
        result = result + 0.5 * chaotic + 0.3 * trig_coupling + 0.2 * adaptive_noise + 0.4 * peaks + 0.3 * saddle + 0.25 * exp_trig
        
        return result