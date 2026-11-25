import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with modified logistic map
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10)
        
        # Modified gradient component with dynamic conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 3) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with additional coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Modified discontinuous region with enhanced step function
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i])
        
        # Improved harmonic interaction with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0)
                freq_mod = 1.0 + 0.5 * np.sin(i * 0.4)
                harmonic += weight * np.sin(freq_mod * (x_normalized[i] + x_normalized[j])) * np.cos(freq_mod * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with modified power
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**2
        
        # Combined fitness with adjusted weights to reduce systematic errors
        return (0.25 * chaotic + 0.30 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.08 * harmonic + 0.02 * nonlin)