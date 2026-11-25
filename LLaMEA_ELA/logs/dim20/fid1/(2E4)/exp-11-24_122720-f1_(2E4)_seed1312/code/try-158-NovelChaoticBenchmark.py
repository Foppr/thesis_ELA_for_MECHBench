import numpy as np

class NovelChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 3.8
        self.poly_degree = 3
        self.rbf_width = 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric potential component with enhanced nonlinearity
        trig_sum = 0
        for i in range(self.dim):
            trig_sum += (np.sin(x[i]) + np.cos(x[i])) * (1 + 0.2 * np.sin(i * 2.0))
            
        # Radial basis function component with adaptive centers and weights
        rbf_sum = 0
        for i in range(self.dim):
            center = 3.0 * np.cos(i * np.pi / (self.dim + 1))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.25 * (distance / self.rbf_width) ** 2)
            rbf_sum += weight
            
        # Chaotic sine mapping component with dynamic parameter
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with dynamic parameter based on dimension
            chaotic_param = self.chaotic_factor * (1 + 0.15 * np.sin(i * np.pi / (self.dim + 2)))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2) + 0.4 * np.sin(2 * chaotic_param * x[i])
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced cross-term interactions with multiple coupling types
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                coupling2 = np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                cross_sum += (coupling1 + 0.25 * coupling2) ** 2
                
        # Multi-scale sinusoidal modulation with frequency variation
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(2 * scale_factor * x[i]) + 0.25 * np.sin(3 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Quaternion-based rotational component for increased complexity
        quat_sum = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                q1, q2, q3, q4 = x[i], x[i+1], x[i+2], x[i+3]
                # Quaternion-like interaction term
                quat_sum += (q1 * q2 + q3 * q4) ** 2 + (q1 * q3 - q2 * q4) ** 2
                
        # Global scaling and dimensionality effect with improved conditioning
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (trig_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum + 0.4 * quat_sum) + 0.08 * self.dim