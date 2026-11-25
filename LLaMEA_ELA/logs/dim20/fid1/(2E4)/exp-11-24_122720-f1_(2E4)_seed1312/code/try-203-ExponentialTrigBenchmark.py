import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential and trigonometric parameters with increased complexity
        self.exp_decay = 2.0
        self.trig_amp = 3.0
        self.sphere_radius = 4.0
        self.fractal_dim = 0.8
        self.noise_level = 0.12
        self.periodicity_mod = 1.5
        
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
                # Chaotic frequency modulation with periodicity
                freq_i = 2.0 + np.sin(i * np.pi / (self.dim + 1)) * 1.5 + np.cos(i * np.pi / (self.dim + 3)) * 0.8 + np.sin(i * self.periodicity_mod) * 0.3
                freq_j = 1.5 + np.cos(j * np.pi / (self.dim + 2)) * 1.2 + np.sin(j * np.pi / (self.dim + 4)) * 0.6 + np.cos(j * self.periodicity_mod) * 0.2
                
                # Cross-dimensional coupling with fractal interaction
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
                fractal_coupling = np.sin(np.log(np.abs(x[i] - x[j]) + 1) * self.fractal_dim)
                trig_sum += coupling ** 2 * fractal_coupling
                
        # Spherical distortion with higher-order harmonic terms
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            # Add fractal-like spherical distortion with periodic modulation
            sphere_distortion = np.sin(norm * self.fractal_dim) ** 2 + np.cos(norm * self.fractal_dim) ** 2 + 0.1 * np.sin(norm * self.periodicity_mod)
            sphere_sum = (norm - self.sphere_radius) ** 2 * sphere_distortion
            
        # Higher-order polynomial interactions with fractal scaling
        quartic_sum = 0
        quintic_sum = 0
        for i in range(self.dim):
            # Fractal-based scaling factors
            scale_factor = 1.0 + 0.3 * np.sin(np.log(i + 1) * self.fractal_dim)
            # Add periodicity modulation to scaling factors
            periodic_factor = 1.0 + 0.1 * np.cos(i * self.periodicity_mod)
            quartic_sum += 0.1 * scale_factor * periodic_factor * x[i] ** 4
            quintic_sum += 0.05 * scale_factor * periodic_factor * x[i] ** 5
            
        # Adaptive conditioning with fractal dimensionality and periodic modulation
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sin(np.log(self.dim)) + 0.1 * np.cos(np.log(self.dim)) + 0.05 * np.sin(self.dim * self.periodicity_mod)
        
        # Fractal noise injection for robustness
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.2 * np.cos(self.dim * self.fractal_dim) + 0.1 * np.sin(self.dim * self.fractal_dim) + 0.05 * np.cos(self.dim * self.periodicity_mod))
        
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + quartic_sum + quintic_sum) + noise + 0.3 * self.dim