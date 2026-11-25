import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_centers = 12
        self.time_step = 0.15
        self.noise_level = 0.03
        self.polynomial_order = 4
        
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
                t = self.time_step * (i * 1.7 + j * 1.1 + np.sin(i * 0.5) * np.cos(j * 0.3))
                center[j] = 4.0 * np.sin(t) + 1.8 * np.cos(2.3 * t) + 0.8 * np.sin(3.7 * t) + 0.3 * np.cos(5.1 * t)
            centers.append(center)
        
        # Polynomial chaos expansion component with enhanced nonlinearity
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Modified chaotic coefficients and coupling
            coeff = 2.0 + 0.3 * np.sin(i * 2.9) + 0.6 * np.cos(i * 3.1) + 0.1 * np.sin(i * 0.7)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Radial basis functions with stochastic parameters and enhanced interactions
        rbf_sum = 0.0
        for i, center in enumerate(centers):
            # Modified stochastic width and height
            width = 1.2 + 0.5 * np.sin(i * 1.4) + 0.2 * np.cos(i * 0.9) + self.noise_level * np.random.randn()
            height = 1.3 + 0.7 * np.cos(i * 2.1) + 0.3 * np.sin(i * 1.5) + self.noise_level * np.random.randn()
            
            # Distance to center with modified interaction term
            dist = np.sum((x - center) ** 2)
            interaction = 0.3 * np.sin(np.sum(x) * 0.9) * np.cos(np.mean(x) * 0.6)
            
            # RBF activation with modified chaotic modulation and interaction
            rbf_val = height * np.exp(-dist / (2 * width**2)) * (1.0 + 0.3 * np.sin(dist + interaction) + 0.2 * np.cos(dist * 0.7))
            rbf_sum += rbf_val
        
        # Temporal evolution component with modified nonlinearity and coupling
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Modified time-dependent modulation
            t_mod = np.sin(self.time_step * (i + 1) * 2.8) * np.cos(xi * 1.5) + 0.4 * np.sin(xi * 3.0)
            temporal_term += t_mod * np.sin(xi * 3.5 + t_mod) * np.cos(xi * 0.9)
        
        # Combine all components with modified weighting
        return 0.25 * poly_term + 0.55 * rbf_sum + 0.15 * temporal_term + 0.05 * np.sum(np.sin(x))