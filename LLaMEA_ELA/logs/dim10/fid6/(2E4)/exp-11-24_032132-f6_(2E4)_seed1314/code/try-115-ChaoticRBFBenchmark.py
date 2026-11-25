import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_centers = 8
        self.time_step = 0.1
        self.noise_level = 0.05
        self.polynomial_order = 3
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Generate time-varying centers for RBFs
        centers = []
        for i in range(self.num_centers):
            center = np.zeros(self.dim)
            for j in range(self.dim):
                # Chaotic time evolution of center positions
                t = self.time_step * (i + j * 0.5)
                center[j] = 4.0 * np.sin(t) + 1.5 * np.cos(2 * t) + 0.5 * np.sin(3 * t)
            centers.append(center)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Higher-order polynomial terms with chaotic coefficients
            coeff = 1.0 + 0.3 * np.sin(i * 2.1) + 0.2 * np.cos(i * 1.7)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Radial basis functions with stochastic parameters
        rbf_sum = 0.0
        for i, center in enumerate(centers):
            # Stochastic width and height for each RBF
            width = 1.0 + 0.2 * np.sin(i * 0.8) + self.noise_level * np.random.randn()
            height = 1.0 + 0.4 * np.cos(i * 1.3) + self.noise_level * np.random.randn()
            
            # Distance to center
            dist = np.sum((x - center) ** 2)
            
            # RBF activation with chaotic modulation
            rbf_val = height * np.exp(-dist / (2 * width**2)) * (1.0 + 0.1 * np.sin(dist))
            rbf_sum += rbf_val
        
        # Temporal evolution component
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Time-dependent modulation
            t_mod = np.sin(self.time_step * (i + 1) * 3.14)
            temporal_term += t_mod * np.cos(xi * 2.0 + t_mod)
        
        # Combine all components with dynamic weighting
        return 0.4 * poly_term + 0.4 * rbf_sum + 0.2 * temporal_term