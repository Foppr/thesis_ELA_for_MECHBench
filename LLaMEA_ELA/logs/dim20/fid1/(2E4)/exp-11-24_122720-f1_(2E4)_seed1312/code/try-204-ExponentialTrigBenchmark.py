import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential and trigonometric parameters with increased complexity
        self.exp_decay = 1.8
        self.trig_amp = 3.0
        self.sphere_radius = 4.0
        self.fractal_dim = 0.8
        self.noise_level = 0.12
        self.quaternion_scale = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with fractal-like scaling
        exp_sum = 0
        for i in range(self.dim):
            # Fractal-like interaction term
            fractal_factor = np.sin(np.log(i + 1) * self.fractal_dim) ** 2
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * (1 + 0.5 * fractal_factor)
            
        # Chaotic trigonometric couplings with higher-order interactions
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic frequency modulation
                freq_i = 2.0 + np.sin(i * np.pi / (self.dim + 1)) * 1.5 + np.cos(i * np.pi / (self.dim + 3)) * 0.8
                freq_j = 1.5 + np.cos(j * np.pi / (self.dim + 2)) * 1.2 + np.sin(j * np.pi / (self.dim + 4)) * 0.6
                
                # Cross-dimensional coupling with fractal interaction
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
                fractal_coupling = np.sin(np.log(np.abs(x[i] - x[j]) + 1) * self.fractal_dim)
                trig_sum += coupling ** 2 * fractal_coupling
                
        # Spherical distortion with higher-order harmonic terms
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            # Add fractal-like spherical distortion
            sphere_distortion = np.sin(norm * self.fractal_dim) ** 2 + np.cos(norm * self.fractal_dim) ** 2
            sphere_sum = (norm - self.sphere_radius) ** 2 * sphere_distortion
            
        # Higher-order polynomial interactions with fractal scaling
        quartic_sum = 0
        quintic_sum = 0
        for i in range(self.dim):
            # Fractal-based scaling factors
            scale_factor = 1.0 + 0.3 * np.sin(np.log(i + 1) * self.fractal_dim)
            quartic_sum += 0.1 * scale_factor * x[i] ** 4
            quintic_sum += 0.05 * scale_factor * x[i] ** 5
            
        # Quaternion-based symmetry breaking for increased complexity
        quaternion_term = 0
        if self.dim >= 4:
            # Create quaternion-like interactions for every 4 dimensions
            for k in range(0, self.dim - 3, 4):
                q_real = x[k] + x[k+1] + x[k+2] + x[k+3]
                q_imag1 = x[k] * x[k+1] - x[k+2] * x[k+3]
                q_imag2 = x[k] * x[k+2] + x[k+1] * x[k+3]
                q_imag3 = x[k] * x[k+3] - x[k+1] * x[k+2]
                
                # Combine quaternion terms with fractal scaling
                quat_contrib = (q_real**2 + q_imag1**2 + q_imag2**2 + q_imag3**2) * np.sin(np.log(k + 1) * self.fractal_dim)
                quaternion_term += quat_contrib
                
        # Adaptive conditioning with fractal dimensionality and quaternion influence
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sin(np.log(self.dim)) + 0.1 * np.cos(np.log(self.dim))
        cond_factor += self.quaternion_scale * (quaternion_term / (self.dim + 1))
        
        # Fractal noise injection for robustness
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.2 * np.cos(self.dim * self.fractal_dim) + 0.1 * np.sin(self.dim * self.fractal_dim))
        
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + quartic_sum + quintic_sum + quaternion_term) + noise + 0.3 * self.dim