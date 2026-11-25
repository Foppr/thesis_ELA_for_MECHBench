import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 4.2
        self.poly_degree = 7
        self.rbf_width = 1.5
        # Fractal and noise parameters
        self.fractal_dim = 0.8
        self.noise_level = 0.05
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component with enhanced nonlinearity and fractal scaling
        poly_sum = 0
        for i in range(self.dim):
            fractal_scale = (1 + self.fractal_dim * np.sin(i * np.pi / (self.dim + 4)))
            poly_sum += (x[i] ** (3 + i % 6)) * fractal_scale * (1 + 0.15 * np.sin(i * 1.5))
            
        # Radial basis function component with adaptive centers, weights, and fractal modulation
        rbf_sum = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 3)) * (1 + 0.1 * np.cos(i * np.pi / (self.dim + 4)))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.3 * (distance / self.rbf_width) ** 2) * (1 + 0.05 * np.sin(i * np.pi / (self.dim + 5)))
            rbf_sum += weight
            
        # Chaotic sine mapping component with dynamic parameter and noise injection
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with dynamic parameter based on dimension and fractal modulation
            chaotic_param = self.chaotic_factor * (1 + 0.2 * np.cos(i * np.pi / (self.dim + 4))) * (1 + 0.1 * np.sin(i * np.pi / (self.dim + 7)))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2) + 0.5 * np.sin(2 * chaotic_param * x[i])
            # Inject adaptive noise
            noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.05 * np.sin(i))
            chaotic_sum += (chaotic_val ** 2 + noise)
            
        # Enhanced cross-term interactions with multiple coupling types and fractal scaling
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                coupling2 = np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                # Fractal modulation for cross terms
                fractal_mod = 1 + 0.1 * np.sin((i+j) * np.pi / (self.dim + 8))
                cross_sum += ((coupling1 + 0.3 * coupling2) ** 2) * fractal_mod
                
        # Multi-scale sinusoidal modulation with frequency variation and fractal scaling
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(i * np.pi / (self.dim + 5)) * (1 + 0.1 * np.cos(i * np.pi / (self.dim + 9)))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(2 * scale_factor * x[i]) + 0.3 * np.sin(3 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Quaternion-based rotational component for increased complexity with fractal influence
        quat_sum = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                q1, q2, q3, q4 = x[i], x[i+1], x[i+2], x[i+3]
                # Quaternion-like interaction term with fractal modulation
                fractal_q = 1 + 0.1 * np.sin(i * np.pi / (self.dim + 10))
                quat_sum += ((q1 * q2 + q3 * q4) ** 2 + (q1 * q3 - q2 * q4) ** 2) * fractal_q
                
        # Global scaling and dimensionality effect with improved conditioning
        scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (poly_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum + 0.5 * quat_sum) + 0.1 * self.dim