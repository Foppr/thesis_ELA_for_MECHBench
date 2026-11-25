import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Time-varying chaotic map with dynamic r parameter
        chaotic = 0.0
        for i in range(self.dim):
            r = 3.5 + 0.3 * np.sin(i * 0.5)
            x_prev = 0.5
            for _ in range(20):  # More iterations for chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10)
        
        # Enhanced gradient with adaptive conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.8) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Multi-modal saddle point with multiple attractor regions
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                saddle += (np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * 
                          (x_normalized[i] - x_normalized[j])**3 * 
                          np.sin(2 * (x_normalized[i] + x_normalized[j])))
        
        # Multi-scale discontinuous regions with varying step thresholds
        discontinuous = 0.0
        for i in range(self.dim):
            threshold = 0.1 * np.sin(i * 0.6)
            step_val = 1.0 if x_normalized[i] > threshold else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(5 * x_normalized[i])
        
        # Enhanced harmonic interactions with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                freq_mod = 1.0 + 0.5 * np.sin(i * 0.4)
                weight = np.exp(-dist * 3.0)
                harmonic += weight * np.sin(freq_mod * (x_normalized[i] + x_normalized[j])) * np.cos(freq_mod * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with periodic modulation
        nonlin = 0.0
        for i in range(self.dim):
            period_mod = 1.0 + 0.3 * np.sin(i * 0.7)
            nonlin += (x_normalized[i]**5) * np.sin(period_mod * x_normalized[i])**2
        
        # Cross-dimensional coupling with exponential weighting
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += np.exp(-np.abs(x_normalized[i] - x_normalized[j]) * 2.0) * (x_normalized[i] * x_normalized[j])
        
        # Combined fitness with new scaling factors
        return (0.35 * chaotic + 0.2 * gradient + 0.18 * saddle + 
                0.12 * discontinuous + 0.08 * harmonic + 0.04 * nonlin + 0.03 * coupling)