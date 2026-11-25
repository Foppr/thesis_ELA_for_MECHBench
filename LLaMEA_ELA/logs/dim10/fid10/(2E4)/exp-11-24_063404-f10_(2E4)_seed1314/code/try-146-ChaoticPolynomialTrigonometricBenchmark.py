import numpy as np

class ChaoticPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for enhanced multimodality
        self.omega = 2.0 * np.pi * (1 + np.arange(dim) * 0.9)
        self.phase_shifts = np.pi * np.random.rand(dim)
        self.polynomial_coeffs = 2.0 + 0.8 * np.sin(np.arange(dim) * np.pi / (dim + 7))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential component with chaotic coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            poly_term += self.polynomial_coeffs[i] * xi**(5 + i % 4)
        
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
            r = 3.9 + 0.3 * np.sin(i * np.pi / (self.dim + 4))
            logistic_val = 1.0 / (1.0 + np.exp(-r * (xi - 0.5)))
            chaotic_mod += logistic_val * np.sin(self.omega[i] * xi + self.phase_shifts[i])
        
        # Cross-dimensional coupling with enhanced polynomial interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add enhanced polynomial interaction between dimensions
                cross_term += (x_scaled[i]**5 + x_scaled[j]**5) * \
                             np.sin(self.omega[i] * x_scaled[j] + self.omega[j] * x_scaled[i])
        
        # Add a chaotic noise component with improved complexity
        noise_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Apply different chaotic maps for each dimension with enhanced nonlinearity
            noise_component += np.sin(19 * xi) * np.cos(16 * xi) * \
                              np.exp(-0.5 * (xi - 0.4)**2)
        
        # Add a radial component to increase multimodality
        radial_term = 0.0
        sum_squares = np.sum(x_scaled**2)
        for i in range(self.dim):
            xi = x_scaled[i]
            radial_term += np.sin(14 * xi) * np.cos(11 * xi) * \
                          np.exp(-0.3 * sum_squares)
        
        # Add a novel oscillatory component with adaptive frequency
        oscillatory_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            freq = 12 + 6 * np.sin(i * np.pi / (self.dim + 2))
            oscillatory_term += np.sin(freq * xi) * np.cos(freq * xi) * \
                              np.exp(-0.15 * sum_squares)
        
        # Add a hybrid chaotic component with multiple map types
        hybrid_chaos = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Combined logistic and tent map
            logistic_val = 1.0 / (1.0 + np.exp(-4.0 * (xi - 0.5)))
            tent_val = 2.0 * xi if xi < 0.5 else 2.0 * (1.0 - xi)
            hybrid_chaos += (logistic_val + tent_val) * np.sin(10 * xi)
        
        # Add a hyperchaotic component with 4D Hénon map
        hyperchaos = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Hyperchaotic 4D Hénon-like map components
            h1 = 1.4 - 0.3 * xi**2 + 0.1 * np.sin(xi)
            h2 = 0.8 * xi + 0.2 * np.cos(xi)
            h3 = 1.2 - 0.4 * xi**2 + 0.15 * np.sin(2*xi)
            h4 = 0.9 * xi + 0.1 * np.cos(2*xi)
            hyperchaos += (h1 + h2 + h3 + h4) * np.sin(6 * xi)
        
        # Combine all components with carefully tuned weights
        return 0.25 * poly_term + 0.18 * trig_term + 0.15 * chaotic_mod + \
               0.14 * cross_term - 0.10 * noise_component + 0.05 * radial_term + \
               0.06 * oscillatory_term + 0.05 * hybrid_chaos + 0.07 * hyperchaos