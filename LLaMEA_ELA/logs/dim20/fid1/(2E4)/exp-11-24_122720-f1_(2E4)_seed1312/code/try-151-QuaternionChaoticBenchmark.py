import numpy as np

class QuaternionChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quaternion parameters
        self.quaternion_scale = 2.0
        self.gaussian_width = 1.5
        self.chaotic_base = 3.8
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric potential component with varying frequencies
        trig_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            trig_sum += (np.sin(freq * x[i]) + np.cos(freq * x[i])) ** 2
            
        # Gaussian radial basis function component with quaternion-inspired centers
        rbf_sum = 0
        for i in range(self.dim):
            # Quaternion-inspired center placement
            center = self.quaternion_scale * np.sin(i * np.pi / (self.dim + 2))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.5 * (distance / self.gaussian_width) ** 2)
            rbf_sum += weight
            
        # Quaternion-based chaotic mapping component
        chaotic_sum = 0
        for i in range(self.dim):
            # Chaotic parameter based on quaternion structure
            chaotic_param = self.chaotic_base * (1 + 0.3 * np.cos(i * np.pi / (self.dim + 3)))
            # Quaternion-like chaotic mapping
            q_real = np.sin(chaotic_param * x[i])
            q_imag = np.cos(chaotic_param * x[i])
            q_j = np.sin(chaotic_param * x[i]**2)
            q_k = np.cos(chaotic_param * x[i]**2)
            chaotic_val = q_real**2 + q_imag**2 + q_j**2 + q_k**2
            chaotic_sum += chaotic_val
            
        # Adaptive coupling with multi-scale interactions
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale coupling with different interaction types
                coupling1 = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                coupling2 = np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(2 * x[i] + x[j])
                coupling3 = np.cos(x[i] * x[j]**2) + np.sin(x[i]**2 * x[j])
                coupling_sum += (coupling1 + 0.5 * coupling2 + 0.3 * coupling3) ** 2
                
        # Multi-scale frequency modulation with adaptive parameters
        mod_sum = 0
        for i in range(self.dim):
            # Adaptive scale factor based on dimension and position
            scale_factor = 1.0 + 0.8 * np.sin(i * np.pi / (self.dim + 5))
            # Multi-frequency modulation
            mod_val = np.sin(scale_factor * x[i]) + 0.5 * np.cos(2 * scale_factor * x[i]) + 0.3 * np.sin(3 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Global scaling factor with dimensionality effect
        scale = 1.0 + 0.6 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (trig_sum + rbf_sum + chaotic_sum + coupling_sum + mod_sum) + 0.2 * self.dim