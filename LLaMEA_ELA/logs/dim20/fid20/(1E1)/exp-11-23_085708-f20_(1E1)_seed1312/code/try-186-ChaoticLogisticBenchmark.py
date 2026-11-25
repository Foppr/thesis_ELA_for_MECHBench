import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic logistic map component with dimension-wise parameters
        chaotic_term = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            x_i = x_scaled[i]
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            chaotic_val = r * x_i * (1 - x_i)
            chaotic_term += chaotic_val ** 2
        
        # Fractional Brownian motion-like fractal terrain
        fbm_term = 0.0
        for i in range(self.dim):
            # Use sine waves with varying frequencies and amplitudes
            freq = 2 ** (i % 4 + 1)
            amp = 1.0 / (i + 1)
            fbm_term += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.5)
        
        # Saddle-point dominance with hyperbolic tangent interactions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent interaction creating saddle points
                diff = x_scaled[i] - x_scaled[j]
                saddle_term += np.tanh(diff) * np.tanh(x_scaled[i] + x_scaled[j])
        
        # Multi-scale periodic modulation with varying phase shifts
        periodic_term = 0.0
        for i in range(self.dim):
            # Multiple sine components with different periods and phases
            period1 = 2 * np.pi / (i + 1)
            period2 = 4 * np.pi / (i + 1)
            phase1 = i * np.pi / 4
            phase2 = i * np.pi / 6
            periodic_term += (np.sin(period1 * x_scaled[i] + phase1) + 
                             0.5 * np.cos(period2 * x_scaled[i] + phase2)) * (i + 1)
        
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Exponential decay based on dimension distance
                    decay = np.exp(-abs(i - j) * 0.1)
                    cross_term += decay * np.sin(x_scaled[i] * x_scaled[j]) * (i + j + 1)
        
        # Combine all terms with different weights and add constant offset
        total = (0.5 * chaotic_term + 
                0.3 * fbm_term + 
                0.2 * saddle_term + 
                0.1 * periodic_term + 
                0.4 * cross_term)
        
        # Add a global minimum at the origin with additional penalty
        penalty = 0.01 * np.sum(x_scaled**4)  # Quartic penalty
        
        return total + penalty + 2.0