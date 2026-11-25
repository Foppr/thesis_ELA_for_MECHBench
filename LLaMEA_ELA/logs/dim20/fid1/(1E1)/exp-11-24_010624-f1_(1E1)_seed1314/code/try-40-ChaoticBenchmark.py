import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with higher complexity and dynamic variation
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.9) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and multi-frequency sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add multi-scale radial component with multiple sinusoidal frequencies
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) + 0.2 * x[i]**3 * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with dynamic frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.2 * np.abs(x[i])) * np.sin(0.5 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with time-varying strength and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with phase shift
                coupling_strength = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.cos(0.1 * (i - j))
                result += coupling_strength * np.sin(x[i] * x[j] + 0.5 * np.sin(i + j)) * np.sin(0.3 * (i - j))
                
        # Add global scaling with multiple frequency components and adaptive modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add adaptive noise component with dynamic amplitude and frequency
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 0.5))
        result += noise
        
        # Add a new multi-modal component with Gaussian peaks and dynamic positioning
        modal_component = 0.0
        for k in range(3):
            peak_x = 2.0 * np.sin(k * np.pi / 3) + 0.5 * np.cos(k * np.pi / 2)
            peak_y = 2.0 * np.cos(k * np.pi / 3) + 0.5 * np.sin(k * np.pi / 2)
            modal_term = np.exp(-0.5 * ((x[0] - peak_x)**2 + (x[1] - peak_y)**2)) * np.sin(2 * k * np.pi / 3)
            modal_component += modal_term
            
        result += 0.5 * modal_component
        
        return result