import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested exponential modulation with cross-dimensional coupling
        exp_term = np.sum(np.exp(-0.3 * np.sum(x_scaled**2)) * np.cos(0.4 * np.sum(x_scaled)))
        
        # Cross-dimensional trigonometric coupling with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_term += np.sin(3 * np.pi * (x_scaled[i] + x_scaled[j])) * np.cos(5 * np.pi * (x_scaled[i] - x_scaled[j]))
        
        # Adaptive polynomial distortion with dimension-dependent coefficients
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (i+1) * (x_scaled[i]**7 - 4 * x_scaled[i]**5 + 3 * x_scaled[i]**3)
        
        # Enhanced chaotic component with nested sine and exponential with dynamic parameters
        chaotic_term = np.sum(np.sin(np.exp(0.8 * x_scaled)) * np.cos(0.9 * x_scaled) * np.sin(2 * x_scaled))
        
        # Logarithmic barrier with dynamic penalty based on dimension
        barrier_term = np.sum(np.log(1.0 + 0.3 * np.abs(x_scaled)) * np.exp(-0.4 * x_scaled**2) * (1.0 + 0.1 * self.dim))
        
        # High-frequency oscillation with adaptive amplitude and phase
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += (i+1) * np.sin(20 * np.pi * x_scaled[i]) * np.cos(18 * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction with nonlinear coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += np.sin(2 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[j]) * (1.0 + 0.1 * abs(i-j))
        
        # Combine all terms with dynamic weights
        return 0.25 * exp_term + 0.2 * trig_term + 0.15 * poly_term + 0.18 * chaotic_term + 0.08 * barrier_term + 0.07 * high_freq_term + 0.07 * cross_term + 2.0