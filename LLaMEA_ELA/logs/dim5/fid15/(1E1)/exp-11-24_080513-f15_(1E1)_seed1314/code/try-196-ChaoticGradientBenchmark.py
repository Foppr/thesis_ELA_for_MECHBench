import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Henon map-based chaotic transformation with quantum interference
        chaotic = 0.0
        a, b = 1.4, 0.3
        x_prev, y_prev = 0.1, 0.1
        for i in range(self.dim):
            for _ in range(20):  # Iterate to reach chaotic regime
                x_new = 1 - a * x_prev**2 + y_prev
                y_new = b * x_prev
                x_prev, y_prev = x_new, y_new
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * y_prev * 10)
        
        # Quantum-inspired harmonic interactions with phase modulation
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.5) * np.cos(i * 0.3)
            quantum += (x_normalized[i]**2) * np.sin(x_normalized[i] * phase * 20) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Nested saddle points with polynomial coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Polynomial coupling with varying exponents
                exponent = 2 + np.sin(i * 0.8) * 2
                saddle += (x_normalized[i]**exponent) * (x_normalized[j]**(exponent/2)) * (x_normalized[i] - x_normalized[j])**3
        
        # Adaptive conditioning with dynamic scaling factors
        adaptive = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 2.0 * np.sin(i * 0.6) * np.cos(i * 0.4)
            adaptive += scale_factor * x_normalized[i]**5 * np.exp(-0.2 * np.abs(x_normalized[i]))
        
        # Discontinuous regions with fractal-like step functions
        discontinuous = 0.0
        for i in range(self.dim):
            # Fractal step function with multiple scales
            step_val = np.sign(x_normalized[i])
            freq_mod = 1 + 0.5 * np.sin(i * 0.7)
            discontinuous += step_val * np.sin(freq_mod * x_normalized[i] * 8) * np.cos(freq_mod * x_normalized[i] * 6)
        
        # Multi-scale interference patterns with exponential decay
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0)
                interference += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(2 * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with exponential and logarithmic components
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += np.exp(x_normalized[i]**2) * np.log(np.abs(x_normalized[i]) + 1) * np.sin(x_normalized[i] * 3)
        
        # Combined fitness with dynamic weighting and global scaling
        return (0.25 * chaotic + 0.2 * quantum + 0.15 * saddle + 
                0.15 * adaptive + 0.15 * discontinuous + 0.08 * interference + 0.02 * nonlin)