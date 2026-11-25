import numpy as np

class NovelChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with slight modification
        self.chaotic_factor = 3.9
        self.poly_degree = 3
        self.rbf_width = 1.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric potential component with altered nonlinearity
        trig_sum = 0
        for i in range(self.dim):
            trig_sum += (np.sin(1.5 * x[i]) + np.cos(1.2 * x[i])) * (1 + 0.3 * np.sin(i * 1.8))
            
        # Radial basis function component with modified centers and weights
        rbf_sum = 0
        for i in range(self.dim):
            center = 2.5 * np.cos(i * np.pi / (self.dim + 1.5))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.3 * (distance / self.rbf_width) ** 2)
            rbf_sum += weight
            
        # Chaotic sine mapping component with altered parameter dynamics
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with modified dynamic parameter
            chaotic_param = self.chaotic_factor * (1 + 0.2 * np.sin(i * np.pi / (self.dim + 1.8)))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**1.5) + 0.3 * np.sin(1.5 * chaotic_param * x[i])
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced cross-term interactions with modified coupling types
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(1.2 * x[i] * x[j]) + np.cos(0.8 * (x[i] + x[j]))
                coupling2 = np.exp(-0.35 * (x[i] - x[j])**2) * np.sin(1.3 * (x[i] + x[j]))
                cross_sum += (coupling1 + 0.3 * coupling2) ** 2
                
        # Multi-scale sinusoidal modulation with altered frequency variation
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.4 * np.sin(i * np.pi / (self.dim + 2.5))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(1.8 * scale_factor * x[i]) + 0.3 * np.sin(2.5 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Quaternion-based rotational component with modified interaction terms
        quat_sum = 0
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 4):
                q1, q2, q3, q4 = x[i], x[i+1], x[i+2], x[i+3]
                # Modified quaternion-like interaction term
                quat_sum += (q1 * q2 + q3 * q4) ** 2 + (q1 * q3 - q2 * q4) ** 2 * 0.7
                
        # Global scaling and dimensionality effect with modified conditioning
        scale = 1.2 + 0.25 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (trig_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum + 0.35 * quat_sum) + 0.09 * self.dim