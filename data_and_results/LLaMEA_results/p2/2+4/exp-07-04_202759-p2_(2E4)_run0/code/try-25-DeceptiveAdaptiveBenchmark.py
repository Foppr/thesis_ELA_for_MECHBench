import numpy as np

class DeceptiveAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with adaptive scaling
        exp_decay = np.sum(np.exp(-0.5 * (x / (1.0 + np.abs(x)))**2))
        
        # Sine-wave modulation with varying frequencies and amplitudes
        sine_mod = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            sine_mod += amp * np.sin(freq * x[i]) * np.cos(0.7 * x[i])
        
        # Adaptive conditioning factor per dimension
        cond_factor = np.array([1.0 + 0.5 * np.sin(0.2 * i) for i in range(self.dim)])
        adaptive_cond = np.sum(cond_factor * x**2)
        
        # Cross-dimensional interaction with Gaussian kernel
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interaction += np.exp(-0.5 * dist**2) * np.sin(2.0 * (x[i] + x[j]))
        
        # Add a global deceptive term with multiple peaks
        deceptive = 0
        for i in range(self.dim):
            deceptive += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with dynamic weights
        return 0.25 * exp_decay + 0.35 * sine_mod + 0.2 * adaptive_cond + 0.15 * interaction + 0.05 * deceptive