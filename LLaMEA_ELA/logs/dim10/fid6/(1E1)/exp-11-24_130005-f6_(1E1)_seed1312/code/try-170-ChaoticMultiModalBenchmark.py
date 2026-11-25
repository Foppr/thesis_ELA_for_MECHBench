import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            sinusoidal += amp * np.sin(freq * x_scaled[i] * np.pi) * np.cos(freq * x_scaled[i] * np.pi * 0.5)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.4) * 0.7
            width = 0.5 + 0.2 * np.cos(i * 0.6)
            rbf += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Polynomial interaction terms with mixed degrees
        polynomial = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher order interactions with varying exponents
                poly_term = (x_scaled[i]**3) * (x_scaled[j]**2) + (x_scaled[i]**2) * (x_scaled[j]**3)
                polynomial += 0.5 * poly_term
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r_param = 3.8 + 0.2 * np.sin(i * 0.5)
            x_prev = x_scaled[i] if i == 0 else x_scaled[i-1]
            chaotic += r_param * x_prev * (1 - x_prev)
        
        # Cross-term interaction with non-linear coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear coupling between dimensions
                coupling = np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term += coupling
        
        # Combined function with adjusted weights for complexity balance
        return 1.2 * sinusoidal + 0.8 * rbf + 0.6 * polynomial + 0.4 * chaotic + 0.3 * cross_term