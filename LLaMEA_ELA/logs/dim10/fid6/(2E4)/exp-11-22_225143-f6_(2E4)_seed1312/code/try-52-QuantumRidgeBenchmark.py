import numpy as np

class QuantumRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Quantum oscillation parameters
        self.omega = np.random.uniform(1.0, 10.0, dim)
        self.phase = np.random.uniform(0, 2*np.pi, dim)
        self.amplitude = np.random.uniform(0.5, 2.0, dim)
        
        # Ridge structure parameters
        self.ridge_heights = np.random.uniform(0.1, 3.0, dim)
        self.ridge_widths = np.random.uniform(0.5, 2.0, dim)
        self.ridge_positions = np.random.uniform(-4.0, 4.0, dim)
        
        # Cross-dimensional coupling strengths
        self.coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_strengths, 0.0)
        
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Quantum oscillatory components
        for i in range(self.dim):
            quantum_term = self.amplitude[i] * np.sin(self.omega[i] * x_norm[i] + self.phase[i])
            f_val += quantum_term**2
        
        # Ridge structure components
        for i in range(self.dim):
            ridge_term = self.ridge_heights[i] * np.exp(-0.5 * ((x_norm[i] - self.ridge_positions[i]) / self.ridge_widths[i])**2)
            f_val += ridge_term
        
        # Cross-dimensional coupling with adaptive conditioning
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.sin(x_norm[i] - x_norm[j])
            f_val += 0.5 * coupling_sum**2
        
        # Adaptive conditioning and multi-scale oscillations
        for i in range(self.dim):
            # Add varying conditioning
            condition_factor = self.conditioning_factors[i]
            f_val += condition_factor * (x_norm[i]**4 + 0.1 * x_norm[i]**2)
            
            # Multi-scale oscillation
            scale_sum = 0.0
            for scale in [0.5, 1.0, 2.0]:
                scale_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
            f_val += 0.3 * scale_sum**2
        
        # Add a global periodic modulation
        global_mod = np.sin(0.5 * np.sum(x_norm))
        f_val += 0.2 * global_mod**2
        
        # Add noise-like perturbations for increased complexity
        noise_perturbation = 0.05 * np.sum(np.sin(17 * x_norm) + np.cos(11 * x_norm))
        f_val += noise_perturbation
        
        return f_val