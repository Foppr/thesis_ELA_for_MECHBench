import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.3)
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        self.poly_exponents = 2 + np.arange(dim) % 4
        # Add chaotic logistic map parameter
        self.r = 3.8 + 0.2 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential component with chaotic exponents
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_term += (xi ** self.poly_exponents[i]) * np.sin(self.r[i] * xi)
        
        # Trigonometric coupling component
        trig_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            trig_sum += np.sin(self.omega[i] * xi + self.phase_shifts[i]) * np.cos(self.omega[i] * xi + self.phase_shifts[i])
        
        # Chaotic phase coupling between dimensions
        phase_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x_scaled[j], x_scaled[i])
                phase_coupling += np.sin(self.r[i] * angle + self.r[j] * xi) * np.cos(self.r[i] * angle + self.r[j] * xi)
        
        # Polynomial with chaotic modulation
        modulated_poly = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            logistic_mod = 1.0 / (1.0 + np.exp(-self.r[i] * (xi - 0.25)))
            modulated_poly += (xi ** 3) * logistic_mod
        
        # Add a chaotic noise component for additional complexity
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += np.sin(5 * x_scaled[i]) * np.cos(4 * x_scaled[i])
        
        # Combine all components with modified weights
        return 0.28 * poly_term + 0.32 * trig_sum + 0.18 * phase_coupling - 0.22 * modulated_poly - 0.08 * noise_component