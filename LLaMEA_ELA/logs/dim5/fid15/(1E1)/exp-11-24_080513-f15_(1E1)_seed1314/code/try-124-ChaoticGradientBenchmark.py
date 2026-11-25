import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Time-delayed chaotic component with feedback
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # Iterate to reach chaotic regime
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 7)
        
        # Dynamic conditioning with time-varying weights
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.8 + np.sum(x_normalized[:i]) * 0.3)
            gradient += condition * (x_normalized[i] ** 3) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Saddle point with time-delayed coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-3), i):  # Delayed coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**2
        
        # Discontinuous region with multi-scale step modulation
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(5 * x_normalized[i])
        
        # Multi-scale harmonic interaction with dynamic weights
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0) * (1 + 0.5 * np.sin(i * 0.5))
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with exponential scaling
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**2
        
        # Global optima embedding with sinusoidal modulation
        global_opt = 0.0
        for i in range(self.dim):
            global_opt += np.sin(10 * x_normalized[i]) * np.cos(7 * x_normalized[i])
        
        # Combined fitness with enhanced scaling and cross-term interactions
        return (0.25 * chaotic + 0.2 * gradient + 0.18 * saddle + 
                0.18 * discontinuous + 0.12 * harmonic + 0.05 * nonlin + 0.02 * global_opt)