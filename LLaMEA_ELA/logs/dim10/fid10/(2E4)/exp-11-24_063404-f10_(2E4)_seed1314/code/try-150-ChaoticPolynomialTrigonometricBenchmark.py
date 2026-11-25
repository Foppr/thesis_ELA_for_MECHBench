import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.7)
        self.phase_shifts = np.pi * np.random.rand(dim)
        self.polynomial_coeffs = 1.0 + 0.4 * np.sin(np.arange(dim) * np.pi / (dim + 5))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential component with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_term += self.polynomial_coeffs[i] * xi**(4 + i % 3)
        
        # Trigonometric coupling component with chaotic phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            trig_term += np.sin(self.omega[i] * xi + self.phase_shifts[i]) * \
                        np.cos(self.omega[i] * xi + self.phase_shifts[i])
        
        # Chaotic phase shift modulation with enhanced complexity
        chaotic_mod = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply logistic map for chaotic modulation with dynamic r
            r = 3.8 + 0.2 * np.sin(i * np.pi / (self.dim + 3))
            logistic_val = 1.0 / (1.0 + np.exp(-r * (xi - 0.5)))
            chaotic_mod += logistic_val * np.sin(self.omega[i] * xi + self.phase_shifts[i])
        
        # Cross-dimensional coupling with enhanced polynomial interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add enhanced polynomial interaction between dimensions
                cross_term += (x_scaled[i]**4 + x_scaled[j]**4) * \
                             np.sin(self.omega[i] * x_scaled[j] + self.omega[j] * x_scaled[i])
        
        # Add a chaotic noise component with improved complexity
        noise_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply different chaotic maps for each dimension with enhanced nonlinearity
            noise_component += np.sin(17 * xi) * np.cos(14 * xi) * \
                              np.exp(-0.35 * (xi - 0.2)**2)
        
        # Add a radial component to increase multimodality
        radial_term = 0.0
        sum_squares = np.sum(x_scaled**2)
        for i in range(self.dim):
            xi = x_scaled[i]
            radial_term += np.sin(12 * xi) * np.cos(9 * xi) * \
                          np.exp(-0.25 * sum_squares)
        
        # Combine all components with carefully tuned weights
        return 0.30 * poly_term + 0.20 * trig_term + 0.25 * chaotic_mod + \
               0.15 * cross_term - 0.10 * noise_component + 0.05 * radial_term