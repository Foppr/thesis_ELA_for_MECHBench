import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term for global attraction
        quadratic = np.sum(x_normalized**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)  # Varying frequencies: 2, 4, 8, 16, 32
            amp = 0.5 + 0.5 * np.sin(i * np.pi / 3)  # Varying amplitudes
            chaotic += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Exponential decay terms creating deep, narrow valleys
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-2.0 * np.abs(x_normalized[i])) * np.cos(3 * np.pi * x_normalized[i])
        
        # Cross-dimensional interaction terms with varying weights
        cross_interaction = 0.0
        for i in range(self.dim-1):
            weight = 0.1 + 0.2 * np.sin(i * np.pi / 4)
            cross_interaction += weight * (x_normalized[i]**3 + x_normalized[i+1]**3) * \
                               np.exp(-0.3 * (x_normalized[i] - x_normalized[i+1])**2)
        
        # Fractional polynomial terms creating irregular curvature
        fractional_poly = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                fractional_poly += x_normalized[i]**(1.5) * np.sin(x_normalized[i])
            elif i % 4 == 1:
                fractional_poly += x_normalized[i]**(2.5) * np.cos(x_normalized[i])
            else:
                fractional_poly += x_normalized[i]**(3.5)
        
        # Global scaling and combination
        return 0.8 * quadratic + 0.3 * chaotic + 0.2 * exp_decay + 0.15 * cross_interaction + 0.25 * fractional_poly