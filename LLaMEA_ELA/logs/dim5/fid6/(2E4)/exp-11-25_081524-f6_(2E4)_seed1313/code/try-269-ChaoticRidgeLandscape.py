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
            # Asymmetric ridge structure
            ridge_height = 1.0 + 0.5 * np.sin(0.3 * self.t + i * 0.4)
            ridge_width = 0.8 + 0.2 * np.cos(0.2 * self.t + i * 0.3)
            
            # Asymmetric quadratic ridge
            asym_term = (xi - 0.5)**2 * (1 + 0.3 * np.sin(0.7 * self.t + i * 0.5))
            result += ridge_height * np.exp(-asym_term / (2 * ridge_width**2))
            
        # Dynamic saddle points with time-varying positions
        saddle_energy = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Saddle point position varies chaotically
            saddle_pos = np.sin(0.5 * self.t + i * 0.3) * 2.0
            saddle_depth = 1.5 + 0.8 * np.cos(0.4 * self.t + i * 0.6)
            
            # Asymmetric saddle potential
            diff = xi - saddle_pos
            saddle_potential = saddle_depth * (diff**2 - 1.0)**2
            
            # Add nonlinearity through chaotic modulation
            mod = 1.0 + 0.3 * np.sin(0.8 * self.t + i * 0.7)
            saddle_energy += mod * saddle_potential
            
        result += saddle_energy
        
        # Adaptive noise injection with chaotic amplitude modulation
        noise_amp = 0.5 + 0.3 * np.sin(0.6 * self.t)
        noise = 0.0
        for i in range(self.dim):
            # Chaotic noise generator using logistic map
            r = self.r1 + 0.1 * np.sin(0.4 * self.t + i * 0.2)
            chaotic_val = (r * 0.5 * (1 - 0.5))  # Simplified chaotic generator
            noise += noise_amp * chaotic_val * np.cos(xi + 0.5 * self.t + i * 0.3)
            
        result += noise
        
        # Ridge interaction terms with dynamic coupling
        ridge_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                if j < self.dim:
                    # Dynamic coupling strength based on chaotic modulation
                    coupling_strength = 0.4 + 0.2 * np.sin(0.7 * self.t + (i+j) * 0.3)
                    
                    # Ridge interaction with phase shift
                    phase = 0.5 * np.sin(0.6 * self.t + i * 0.4 + j * 0.3)
                    interaction = coupling_strength * np.exp(-0.5 * (xi - x[j])**2) * \
                                 np.cos(2.0 * (xi + x[j]) + phase)
                    
                    ridge_coupling += interaction
                    
        result += ridge_coupling
        
        # Dynamic scaling factor based on chaotic time evolution
        scale_factor = 1.0 + 0.4 * np.sin(0.5 * self.t) * np.cos(0.3 * self.t)
        result *= scale_factor
        
        return result