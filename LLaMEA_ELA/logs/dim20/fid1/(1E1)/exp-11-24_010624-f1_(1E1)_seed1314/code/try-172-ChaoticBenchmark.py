import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced randomness and nonlinearity
        self.chaos_params = np.array([3.9 + 0.2 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.5) + 0.05 * np.tan(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced nonlinearity and radial symmetry
        for i in range(self.dim):
            # Apply modified chaotic dynamics with cubic and quartic terms
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) + 0.05 * x[i]**3 - 0.01 * x[i]**4
            # Add radial component with higher frequency modulation
            radial_term = 0.4 * x[i]**2 * np.sin(1.0 * x[i]) + 0.1 * x[i]**3 * np.cos(0.7 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**7 * np.cos(3 * x[i]) * np.exp(-0.15 * np.abs(x[i])) + 0.02 * x[i]**5 * np.sin(2 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with variable strength and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with complex exponent and phase
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**3 + (x[i] + x[j])**3)) * np.sin(0.5 * (i + j))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.tan(0.3 * x[i])
                
        # Add global scaling with multiple frequency components and dynamic phase
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.5 * dist_from_origin) * np.cos(1.2 * dist_from_origin) + 0.05 * np.cos(0.8 * dist_from_origin))
        
        # Add enhanced noise component with multiple frequency harmonics
        noise = 0.02 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty - enhanced Rosenbrock-like term
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 150 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        result += 0.02 * rosenbrock_term
        
        # Add a periodic component with altered frequencies and amplitude modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) * (1 + 0.2 * np.sin(0.5 * x[i]))
        result += 0.03 * periodic_term
        
        # Add Schwefel-like component with additional sinusoidal modulation for enhanced multimodality
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i]))) + 0.1 * x[i]**2 * np.cos(0.3 * x[i])
        result += 0.03 * schwefel_term
        
        # Add a new twist: introduce a modified Ackley-like function component
        ackley_term = 0.0
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        ackley_term = -20 * np.exp(-0.2 * np.sqrt(sum_sq / self.dim)) - np.exp(sum_cos / self.dim) + 20 + np.e
        result += 0.015 * ackley_term
        
        return result