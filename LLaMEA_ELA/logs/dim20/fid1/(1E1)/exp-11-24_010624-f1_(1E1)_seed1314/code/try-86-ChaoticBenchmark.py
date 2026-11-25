import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with multi-scale variation
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.7) + 0.1 * np.cos(i * 0.3) + 0.05 * np.sin(i * 0.1) for i in range(dim)])
        # Precompute frequency modulation coefficients
        self.freq_mod = np.array([1.0 + 0.3 * np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Multi-iteration chaotic logistic map component
        for i in range(self.dim):
            chaotic_val = 0.0
            xi = x[i]
            for _ in range(3):  # Three iterations of chaos
                chaotic_val = self.chaos_params[i] * xi * (1 - xi**2)
                xi = chaotic_val
            result += chaotic_val
            
        # Radial symmetry with multi-scale sinusoidal modulation
        for i in range(self.dim):
            radial_term = 0.5 * x[i]**2 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            result += radial_term
            
        # Add higher-order polynomial terms with dynamic frequency modulation
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i])) * self.freq_mod[i]
            result += poly_term
            
        # Cross-dimensional coupling with time-varying weights and multiple interaction types
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables and their interaction type
                dist_ij = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                coupling_strength = np.exp(-0.03 * dist_ij) * np.sin(0.5 * (x[i]**2 + x[j]**2))
                interaction = np.sin(x[i] * x[j]) * np.cos(i - j) + 0.5 * np.cos(x[i] + x[j])
                result += coupling_strength * interaction
                
        # Add global scaling with multiple frequency components and phase modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        phase_mod = np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin) + 0.5 * np.sin(1.1 * dist_from_origin)
        result *= (1 + 0.2 * phase_mod)
        
        # Add novel noise injection with chaotic amplitude modulation
        noise_amplitude = 0.02 * np.sum(np.sin(x * 10)) + 0.01 * np.cos(np.sum(x))
        noise = noise_amplitude * np.random.uniform(-1, 1) * np.exp(-0.05 * dist_from_origin)
        result += noise
        
        # Add a final chaotic perturbation component
        final_perturbation = 0.05 * np.sum(np.sin(x * np.pi) * np.cos(x * np.pi))
        result += final_perturbation
        
        return result