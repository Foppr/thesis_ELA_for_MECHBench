import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.poly_orders = 2 + np.arange(dim) % 4
        self.phase_shifts = np.pi * (0.5 + np.random.rand(dim) * 0.5)
        self.frequency_modulators = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential component
        polynomial_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            polynomial_term += (xi ** self.poly_orders[i]) * np.cos(self.phase_shifts[i])
        
        # Trigonometric coupling between dimensions
        trig_coupling = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                # Chaotic phase modulation
                phase_mod = np.sin(self.frequency_modulators[i] * xi + self.frequency_modulators[j] * xj)
                trig_coupling += np.sin(xi * xj) * phase_mod
        
        # Multi-scale harmonic component with chaotic amplitude
        harmonic_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic amplitude modulation
            amp_mod = 1.0 + 0.3 * np.sin(xi * np.pi * (i + 1) * 2)
            harmonic_sum += amp_mod * np.cos(3 * xi + self.phase_shifts[i])
        
        # Radial chaotic oscillation with fractal-like behavior
        r = np.sqrt(np.sum(x_scaled**2))
        radial_oscillation = np.sin(r * 5.0) * np.cos(r * 2.0) * np.exp(-r**2 * 0.1)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                # Exponential decay with chaotic rate
                decay_rate = 0.5 + 0.3 * np.sin(xi * xj)
                cross_coupling += np.exp(-decay_rate * (xi**2 + xj**2)) * np.sin(xi + xj)
        
        # Combine all components
        return 0.4 * polynomial_term + 0.3 * trig_coupling + 0.2 * harmonic_sum + 0.05 * radial_oscillation - 0.05 * cross_coupling