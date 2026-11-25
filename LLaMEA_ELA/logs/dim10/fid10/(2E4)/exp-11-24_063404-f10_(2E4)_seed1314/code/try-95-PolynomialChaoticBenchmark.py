import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters with enhanced randomness
        self.poly_orders = 3 + np.random.randint(0, 4, dim)
        self.rbf_centers = np.random.uniform(-1.5, 1.5, (dim, dim))
        self.rbf_widths = 0.3 + 2.0 * np.random.rand(dim)
        self.conditioning_factors = 0.5 + 3.0 * np.random.rand(dim)
        # Add chaotic modulation parameters
        self.chaotic_params = 1.0 + 2.0 * np.random.rand(dim)
        self.frequency_modulation = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with enhanced complexity
        poly_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            order = self.poly_orders[i]
            term = 0.0
            for j in range(1, order + 1):
                term += np.sin(j * xi) * (xi**j) * np.cos(j * xi**2)
            poly_component += term
        
        # Radial basis function component with enhanced interaction
        rbf_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(self.dim):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[j]
                # Add chaotic modulation to RBF
                modulator = np.sin(self.chaotic_params[j] * xi)
                rbf_component += modulator * np.exp(-width * (xi - center)**2)
        
        # Cross-dimensional coupling with enhanced conditioning
        coupling_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                cond_factor = self.conditioning_factors[i] * self.conditioning_factors[j]
                # Add frequency modulation to coupling
                freq_mod = self.frequency_modulation[i] * self.frequency_modulation[j]
                coupling_component += np.sin(freq_mod * xi * xj) * cond_factor
        
        # Enhanced adaptive conditioning with chaotic modulation
        adaptive_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic modulation using multiple sine/cosine terms
            freq1 = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
            freq2 = 1.0 + 0.4 * np.cos(i * np.pi / (self.dim + 3))
            adaptive_component += np.sin(freq1 * xi) * np.cos(freq2 * xi**2) * np.sin(xi**3)
        
        # Enhanced high-frequency oscillatory component
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Add multiple frequency components with chaotic modulation
            freq1 = 8.0 + 4.0 * np.sin(i * np.pi / (self.dim + 1))
            freq2 = 6.0 + 3.0 * np.cos(i * np.pi / (self.dim + 2))
            oscillatory_component += np.sin(freq1 * xi + np.sin(freq2 * xi)) * np.cos(freq1 * xi + np.cos(freq2 * xi))
        
        # Combine all components with optimized weights
        return 0.3 * poly_component + 0.25 * rbf_component + 0.2 * coupling_component + 0.15 * adaptive_component + 0.1 * oscillatory_component