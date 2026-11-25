import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with higher complexity and non-linearity
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher non-linearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add enhanced radial component with multiple frequency sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with complex frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i])) * np.sin(0.5 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength with phase shift and exponential decay
                coupling_strength = np.exp(-0.08 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.sin(0.5 * (i - j))
                result += coupling_strength * np.sin(x[i] * x[j] * 0.5) * np.cos(i + j)
                
        # Add global scaling with multiple frequency components and phase modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add noise component with enhanced irregularity
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Beale-like term for enhanced multimodality and conditioning
        beale_term = 0.0
        for i in range(self.dim - 1):
            beale_term += (1 - x[i])**2 + 100 * (x[i+1] - x[i]**2)**2
        result += 0.02 * beale_term
        
        # Add a periodic component with higher frequency and amplitude
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.03 * periodic_term
        
        # Add a novel component: fractal-like landscape with recursive coupling
        fractal_term = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                fractal_term += np.sin(x[i] * 3) * np.cos(x[i] * 2) * (1 + 0.1 * np.sin(x[i]))
            else:
                fractal_term += np.cos(x[i] * 4) * np.sin(x[i] * 3) * (1 + 0.1 * np.cos(x[i]))
        result += 0.015 * fractal_term
        
        return result