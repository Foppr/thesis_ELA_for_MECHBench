import numpy as np

class ChaoticRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        # Initialize chaotic parameters
        self.r1 = 3.8
        self.r2 = 3.9
        self.noise_level = 0.01
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal function with asymmetric ridges
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal-like ridge structure with self-similar patterns
            ridge_height = 1.0 + 0.5 * np.sin(0.3 * self.t + i * 0.4)
            ridge_width = 0.8 + 0.2 * np.cos(0.2 * self.t + i * 0.3)
            
            # Asymmetric quadratic ridge with fractal modulation
            fractal_mod = 1.0 + 0.3 * np.sin(2.0 * self.t + i * 0.5) * np.cos(3.0 * self.t + i * 0.2)
            asym_term = (xi - 0.5)**2 * fractal_mod
            result += ridge_height * np.exp(-asym_term / (2 * ridge_width**2))
            
        # Dynamic saddle points with time-varying positions and chaotic evolution
        saddle_energy = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Saddle point position varies chaotically through coupled logistic maps
            saddle_pos = np.sin(0.5 * self.t + i * 0.3) * 2.0 + 0.3 * np.sin(1.7 * self.t + i * 0.8)
            saddle_depth = 1.5 + 0.8 * np.cos(0.4 * self.t + i * 0.6) + 0.4 * np.sin(2.1 * self.t + i * 0.9)
            
            # Asymmetric saddle potential with fractal-like nonlinearity
            diff = xi - saddle_pos
            fractal_saddle = (diff**2 - 1.0)**2 * (1.0 + 0.2 * np.sin(3.0 * self.t + i * 0.7))
            saddle_energy += saddle_depth * fractal_saddle
            
        result += saddle_energy
        
        # Adaptive noise injection with chaotic amplitude modulation and fractal structure
        noise_amp = 0.5 + 0.3 * np.sin(0.6 * self.t)
        noise = 0.0
        for i in range(self.dim):
            # Chaotic noise generator using coupled logistic maps
            r1 = self.r1 + 0.1 * np.sin(0.4 * self.t + i * 0.2)
            r2 = self.r2 + 0.1 * np.cos(0.3 * self.t + i * 0.5)
            chaotic_val = (r1 * 0.5 * (1 - 0.5)) * (1.0 + 0.1 * np.sin(2.0 * self.t + i * 0.8))
            noise += noise_amp * chaotic_val * np.cos(xi + 0.5 * self.t + i * 0.3)
            
        result += noise
        
        # Ridge interaction terms with dynamic coupling and fractal complexity
        ridge_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling range
                if j < self.dim:
                    # Dynamic coupling strength based on fractal chaotic modulation
                    coupling_strength = 0.4 + 0.2 * np.sin(0.7 * self.t + (i+j) * 0.3) * \
                                       np.cos(1.3 * self.t + (i-j) * 0.4)
                    
                    # Ridge interaction with phase shift and fractal structure
                    phase = 0.5 * np.sin(0.6 * self.t + i * 0.4 + j * 0.3) + \
                            0.2 * np.cos(1.8 * self.t + i * 0.5 + j * 0.6)
                    interaction = coupling_strength * np.exp(-0.5 * (xi - x[j])**2) * \
                                 np.cos(2.0 * (xi + x[j]) + phase) * \
                                 (1.0 + 0.1 * np.sin(3.0 * self.t + i * 0.7 + j * 0.8))
                    
                    ridge_coupling += interaction
                    
        result += ridge_coupling
        
        # Dynamic scaling factor based on chaotic time evolution with fractal characteristics
        scale_factor = 1.0 + 0.4 * np.sin(0.5 * self.t) * np.cos(0.3 * self.t) * \
                      (1.0 + 0.2 * np.sin(2.0 * self.t))
        result *= scale_factor
        
        # Add high-frequency chaotic modulation to increase landscape complexity
        high_freq_mod = 0.3 * np.sin(5.0 * self.t) * np.cos(4.0 * self.t)
        result += high_freq_mod * np.sum(np.abs(x)**3)
        
        return result