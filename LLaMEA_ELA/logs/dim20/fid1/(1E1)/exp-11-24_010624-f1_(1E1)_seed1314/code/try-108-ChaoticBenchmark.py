import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add enhanced radial component with multiple frequency sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) + 0.2 * x[i]**3 * np.cos(0.4 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and phase shift
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on both variables and dimension difference
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.cos(0.5 * (i - j))
                result += coupling_strength * np.sin(x[i] * x[j] * 0.5) * np.sin(i + j)
                
        # Add global scaling with multiple frequency components and harmonic modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.6 * dist_from_origin) + 0.1 * np.sin(0.8 * dist_from_origin))
        
        # Add noise component to increase irregularity with enhanced frequency
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Rastrigin-like term for enhanced multimodality
        rastrigin_term = 0.0
        for i in range(self.dim):
            rastrigin_term += x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10
        result += 0.02 * rastrigin_term
        
        # Add a periodic component with more complex interaction
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4 * x[i]) * np.cos(6 * x[i]) + 0.5 * np.sin(2 * x[i])
        result += 0.03 * periodic_term
        
        # Add a saddle point enhancement component
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**4 - 6 * x[i]**2) * np.cos(x[i])
        result += 0.015 * saddle_term
        
        return result