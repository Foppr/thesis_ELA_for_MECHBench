import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with higher complexity and non-linearity
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.5) + 0.05 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and multi-frequency sinusoidal modulation
        for i in range(self.dim):
            # Apply modified chaotic dynamics with higher-order non-linearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) * np.exp(-0.1 * x[i]**2)
            # Add multi-scale radial component with multiple sinusoidal frequencies
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with adaptive frequency modulation and dynamic scaling
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.2 * np.abs(x[i])) * (1 + 0.1 * np.sin(2 * x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with non-linear interaction strength and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear coupling strength based on combined variable interactions
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2 + 0.5 * (x[i]**2 - x[j]**2)))
                phase_shift = np.sin(i * 0.5) * np.cos(j * 0.3)
                result += coupling_strength * np.sin(x[i] * x[j] * phase_shift) * np.cos(i - j + 0.5 * x[i] * x[j])
                
        # Add global scaling with multi-frequency components and dynamic amplitude modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        global_scale = (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        result *= global_scale
        
        # Add adaptive noise component with dynamic frequency and amplitude
        noise = 0.02 * np.sum(np.sin(x * 15 + np.array([i * 0.3 for i in range(self.dim)])))
        result += noise
        
        # Add a final complex harmonic modulation to increase landscape irregularity
        harmonic_mod = np.sum(np.cos(2 * x) * np.sin(3 * x) * np.exp(-0.1 * np.abs(x)))
        result += 0.05 * harmonic_mod
        
        return result