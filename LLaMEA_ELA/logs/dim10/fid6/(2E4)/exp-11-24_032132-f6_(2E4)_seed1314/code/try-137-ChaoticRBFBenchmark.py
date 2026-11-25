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
                # Chaotic time evolution of center positions with modified frequencies
                t = self.time_step * (i * 1.3 + j * 0.7)
                center[j] = 3.5 * np.sin(t) + 1.2 * np.cos(2.5 * t) + 0.6 * np.sin(3.2 * t)
            centers.append(center)
        
        # Polynomial chaos expansion component with modified coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Higher-order polynomial terms with chaotic coefficients
            coeff = 1.2 + 0.4 * np.sin(i * 2.5) + 0.3 * np.cos(i * 1.9)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Radial basis functions with stochastic parameters and modified interactions
        rbf_sum = 0.0
        for i, center in enumerate(centers):
            # Stochastic width and height for each RBF with different noise characteristics
            width = 1.2 + 0.3 * np.sin(i * 0.9) + self.noise_level * np.random.randn()
            height = 0.8 + 0.5 * np.cos(i * 1.5) + self.noise_level * np.random.randn()
            
            # Distance to center with interaction term
            dist = np.sum((x - center) ** 2)
            interaction = 0.1 * np.sin(np.sum(x) * 0.5)
            
            # RBF activation with chaotic modulation and interaction
            rbf_val = height * np.exp(-dist / (2 * width**2)) * (1.0 + 0.15 * np.sin(dist + interaction))
            rbf_sum += rbf_val
        
        # Temporal evolution component with enhanced nonlinearity
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Time-dependent modulation with additional nonlinear term
            t_mod = np.sin(self.time_step * (i + 1) * 2.8) * np.cos(xi * 1.5)
            temporal_term += t_mod * np.sin(xi * 3.0 + t_mod)
        
        # Combine all components with modified weighting
        return 0.35 * poly_term + 0.45 * rbf_sum + 0.2 * temporal_term