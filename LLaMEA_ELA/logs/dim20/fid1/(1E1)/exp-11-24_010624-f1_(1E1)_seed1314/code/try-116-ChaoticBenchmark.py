import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with increased complexity and randomness
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.9 + 1.2) + 0.1 * np.cos(i * 0.4 + 0.5) + 0.05 * np.sin(i * 0.6) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with additional nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) * np.exp(-0.1 * x[i]**2)
            # Add radial component with enhanced sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and additional complexity
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**6 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i])) * np.sin(0.5 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength and additional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with higher-order interactions
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2 + 0.5 * (x[i]**2 - x[j]**2)**2))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.exp(-0.02 * np.abs(x[i] - x[j]))
                
        # Add global scaling with multiple frequency components and additional modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add noise component to increase irregularity and variability
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty - enhanced Rosenbrock-like term
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 150 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        result += 0.02 * rosenbrock_term
        
        # Add a periodic component with higher frequency and additional structure
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.03 * periodic_term
        
        # Add a novel hyperchaotic component with multiple attractor interactions
        hyperchaos_term = 0.0
        for i in range(self.dim):
            hyperchaos_term += 0.05 * x[i]**3 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += hyperchaos_term
        
        # Add a fractional dimensionality component to increase complexity
        frac_dim = 0.0
        for i in range(self.dim):
            frac_dim += 0.01 * np.sin(0.8 * x[i]) * np.cos(0.9 * x[i]) * (i + 1)
        result += frac_dim
        
        return result