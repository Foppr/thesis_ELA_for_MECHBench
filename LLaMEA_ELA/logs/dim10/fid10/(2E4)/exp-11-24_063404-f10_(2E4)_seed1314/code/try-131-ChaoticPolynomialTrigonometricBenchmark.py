import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.5)
        self.phase_shifts = np.pi * np.random.rand(dim)
        self.polynomial_coeffs = 1.0 + 0.8 * np.sin(np.arange(dim) * np.pi / (dim + 3))
        # Add radial basis function parameters
        self.rbf_centers = 2.0 * np.random.rand(dim) - 1.0
        self.rbf_widths = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential component with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_term += self.polynomial_coeffs[i] * xi**(4 + i % 4)
        
        # Trigonometric coupling component with chaotic phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            trig_term += np.sin(self.omega[i] * xi + self.phase_shifts[i]) * \
                        np.cos(self.omega[i] * xi + self.phase_shifts[i])
        
        # Chaotic phase shift modulation with logistic map
        chaotic_mod = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply logistic map for chaotic modulation
            r = 3.9 + 0.1 * np.sin(i * np.pi / (self.dim + 2))
            logistic_val = 1.0 / (1.0 + np.exp(-r * (xi - 0.5)))
            chaotic_mod += logistic_val * np.sin(self.omega[i] * xi)
        
        # Cross-dimensional coupling with polynomial interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add polynomial interaction between dimensions
                cross_term += (x_scaled[i]**2 + x_scaled[j]**2) * \
                             np.sin(self.omega[i] * x_scaled[j] + self.omega[j] * x_scaled[i])
        
        # Add radial basis function component for additional complexity
        rbf_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            rbf_term += np.exp(-0.5 * ((xi - self.rbf_centers[i]) / self.rbf_widths[i])**2)
        
        # Add a dynamic chaotic noise component
        noise_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply different chaotic maps for each dimension
            noise_component += np.sin(15 * xi) * np.cos(13 * xi) * \
                              np.exp(-0.3 * (xi - 0.2)**2)
        
        # Add a radial component with adaptive scaling
        radial_term = 0.0
        for i in range(self.dim):
            radial_term += x_scaled[i]**2
        
        # Combine all components with carefully tuned weights
        return 0.35 * poly_term + 0.25 * trig_term + 0.15 * chaotic_mod + \
               0.10 * cross_term - 0.10 * noise_component + 0.05 * rbf_term + \
               0.05 * radial_term