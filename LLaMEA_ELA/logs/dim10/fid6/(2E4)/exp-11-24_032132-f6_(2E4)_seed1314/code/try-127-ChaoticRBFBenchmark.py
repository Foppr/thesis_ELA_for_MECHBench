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
                # Enhanced chaotic time evolution of center positions
                t = self.time_step * (i * 1.3 + j * 0.7)
                center[j] = 3.5 * np.sin(t) + 1.2 * np.cos(2 * t) + 0.8 * np.sin(3 * t) + 0.3 * np.cos(4 * t)
            centers.append(center)
        
        # Polynomial chaos expansion component with higher order terms
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # More complex chaotic coefficients with varying frequencies
            coeff = 1.2 + 0.4 * np.sin(i * 1.9) + 0.3 * np.cos(i * 2.3) + 0.1 * np.sin(i * 3.7)
            poly_term += coeff * (xi ** self.polynomial_order)
        
        # Radial basis functions with enhanced stochastic parameters
        rbf_sum = 0.0
        for i, center in enumerate(centers):
            # Enhanced stochastic width and height for each RBF
            width = 1.2 + 0.3 * np.sin(i * 0.9) + self.noise_level * np.random.randn()
            height = 1.5 + 0.5 * np.cos(i * 1.1) + self.noise_level * np.random.randn()
            
            # Distance to center with adaptive scaling
            dist = np.sum((x - center) ** 2)
            
            # RBF activation with enhanced chaotic modulation
            rbf_val = height * np.exp(-dist / (2 * width**2)) * (1.0 + 0.15 * np.sin(dist) + 0.08 * np.cos(dist))
            rbf_sum += rbf_val
        
        # Temporal evolution component with enhanced modulation
        temporal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced time-dependent modulation
            t_mod = np.sin(self.time_step * (i + 1) * 2.7) + 0.5 * np.cos(self.time_step * (i + 1) * 1.9)
            temporal_term += t_mod * np.cos(xi * 1.8 + t_mod) + 0.3 * np.sin(xi * 1.5)
        
        # Combine all components with adjusted dynamic weighting
        return 0.35 * poly_term + 0.45 * rbf_sum + 0.2 * temporal_term