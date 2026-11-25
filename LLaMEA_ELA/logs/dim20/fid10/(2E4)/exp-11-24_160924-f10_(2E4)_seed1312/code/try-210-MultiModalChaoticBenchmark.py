import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.poly_exponents = np.random.uniform(2.0, 6.0, dim)
        self.gradient_strengths = np.random.uniform(0.5, 2.5, dim)
        self.asymmetry_params = np.random.uniform(0.1, 0.9, dim)
        self.interference_strengths = np.random.uniform(0.3, 1.2, dim)
        self.chaos_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.saddle_positions = np.random.uniform(-3.0, 3.0, dim)
        self.ridge_frequencies = np.random.uniform(1.0, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add polynomial chaos components with asymmetric gradient fields
        for i in range(self.dim):
            xi = x[i]
            poly_exp = self.poly_exponents[i]
            grad_strength = self.gradient_strengths[i]
            asymmetry = self.asymmetry_params[i]
            
            # Asymmetric polynomial with chaotic modulation
            poly_term = xi**poly_exp
            chaos_mod = self.chaos_amplitudes[i] * np.sin(5.0 * xi) * np.cos(3.0 * xi)
            asym_grad = grad_strength * (xi + asymmetry * xi**3)
            result += poly_term + asym_grad + chaos_mod
            
        # Add cross-dimensional interference with saddle points
        for i in range(self.dim):
            xi = x[i]
            saddle_pos = self.saddle_positions[i]
            
            # Saddle point interactions with harmonic interference
            for j in range(i+1, self.dim):
                xj = x[j]
                interference_strength = self.interference_strengths[i] * self.interference_strengths[j]
                ridge_freq = self.ridge_frequencies[i] * self.ridge_frequencies[j]
                
                # Cross-dimensional harmonic interference
                interference = interference_strength * np.sin(xi + xj) * np.cos(xi - xj)
                ridge_interaction = 0.5 * np.sin(ridge_freq * xi) * np.cos(ridge_freq * xj)
                result += interference + ridge_interaction
                
        # Add asymmetric gradient field components with polynomial decay
        for i in range(self.dim):
            xi = x[i]
            asym_param = self.asymmetry_params[i]
            poly_exp = self.poly_exponents[i]
            
            # Asymmetric gradient field with polynomial decay
            grad_field = asym_param * xi**3 + (1.0 - asym_param) * xi**5
            decay_factor = np.exp(-0.1 * xi**2)
            result += grad_field * decay_factor
            
        # Add global scaling and enhanced bias reduction
        global_scale = 1.0 + 0.3 * np.sin(0.3 * self.dim)
        result *= global_scale
        
        # Add final chaotic perturbation with exponential decay
        chaotic_perturb = 0.05 * np.sum(np.exp(-0.2 * x**2) * np.sin(8.0 * x) * np.cos(6.0 * x))
        result += chaotic_perturb
        
        # Add additional ridge structure for enhanced difficulty
        ridge_penalty = 0.04 * np.sum(np.sin(3.0 * x)**2 + np.cos(3.0 * x)**2)
        result += ridge_penalty
        
        return result