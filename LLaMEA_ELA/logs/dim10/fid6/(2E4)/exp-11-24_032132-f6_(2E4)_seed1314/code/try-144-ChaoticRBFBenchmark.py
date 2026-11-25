import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_centers = 15
        self.time_step = 0.2
        self.noise_level = 0.02
        self.polynomial_order = 5
        
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
        
        # Generate time-varying centers for RBFs with enhanced chaos
        centers = []
        for i in range(self.num_centers):
            center = np.zeros(self.dim)
            for j in range(self.dim):
                # Enhanced chaotic time evolution with modified frequencies and coupling
                t = self.time_step * (i * 1.9 + j * 1.3 + np.sin(i * 0.6) * np.cos(j * 0.4))
                center[j] = 4.5 * np.sin(t) + 2.0 * np.cos(2.5 * t) + 0.9 * np.sin(4.1 * t) + 0.35 * np.cos(5.5 * t)
            centers.append(center)
        
        # Polynomial chaos expansion component with enhanced nonlinearity
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Higher-order polynomial terms with chaotic coefficients and coupling
            coeff = 1.7 + 0.6 * np.sin(i * 3.3) + 0.45 * np.cos(i * 2.9) + 0.25 * np.sin(i * 1.1)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Radial basis functions with stochastic parameters and enhanced interactions
        rbf_sum = 0.0
        for i, center in enumerate(centers):
            # Enhanced stochastic width and height with different noise characteristics
            width = 1.7 + 0.45 * np.sin(i * 1.3) + 0.35 * np.cos(i * 0.9) + self.noise_level * np.random.randn()
            height = 1.2 + 0.65 * np.cos(i * 1.9) + 0.45 * np.sin(i * 1.4) + self.noise_level * np.random.randn()
            
            # Distance to center with enhanced interaction term
            dist = np.sum((x - center) ** 2)
            interaction = 0.25 * np.sin(np.sum(x) * 0.8) * np.cos(np.mean(x) * 0.5)
            
            # RBF activation with enhanced chaotic modulation and interaction
            rbf_val = height * np.exp(-dist / (2 * width**2)) * (1.0 + 0.25 * np.sin(dist + interaction) + 0.2 * np.cos(dist * 0.6))
            rbf_sum += rbf_val
        
        # Temporal evolution component with enhanced nonlinearity and coupling
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Time-dependent modulation with additional nonlinear terms and coupling
            t_mod = np.sin(self.time_step * (i + 1) * 3.5) * np.cos(xi * 2.0) + 0.35 * np.sin(xi * 2.8)
            temporal_term += t_mod * np.sin(xi * 4.5 + t_mod) * np.cos(xi * 0.8)
        
        # Combine all components with modified weighting and additional coupling
        return 0.35 * poly_term + 0.45 * rbf_sum + 0.15 * temporal_term + 0.05 * np.sum(np.sin(x))