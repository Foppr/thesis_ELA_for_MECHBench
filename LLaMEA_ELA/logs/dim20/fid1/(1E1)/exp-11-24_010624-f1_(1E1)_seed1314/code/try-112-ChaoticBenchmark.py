import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.7) + 0.1 * np.cos(i * 0.3) + 0.05 * np.tan(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with hyperbolic tangent
            chaotic_val = self.chaos_params[i] * x[i] * (1 - np.tanh(x[i]**2))
            # Add radial component with sinusoidal modulation
            radial_term = 0.3 * x[i]**2 * np.sin(0.5 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with fractional exponents and frequency modulation
        for i in range(self.dim):
            poly_term = 0.05 * x[i]**4.5 * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and hyperbolic functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with tanh
                coupling_strength = np.tanh(0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j)
                
        # Add global scaling with multiple frequency components and hyperbolic modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.tanh(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin))
        
        # Add adaptive noise component with varying amplitude
        noise = 0.02 * np.sum(np.sin(x * 15) * np.exp(-0.05 * np.abs(x)))
        result += noise
        
        # Add a new component to improve conditioning and difficulty - modified Rosenbrock with fractional powers
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 100 * (x[i+1] - x[i]**2.5)**2 + (1 - x[i]**1.5)**2
        result += 0.015 * rosenbrock_term
        
        # Add a periodic component with hyperbolic tangent modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.tanh(3 * x[i]) * np.cos(5 * x[i])
        result += 0.025 * periodic_term
        
        # Add a novel fractional polynomial component with exponential decay
        frac_poly_term = 0.0
        for i in range(self.dim):
            frac_poly_term += 0.03 * x[i]**3.7 * np.exp(-0.02 * x[i]**2)
        result += frac_poly_term
        
        # Add a component with multiple sinusoidal frequencies and adaptive weights
        multi_freq_term = 0.0
        for i in range(self.dim):
            multi_freq_term += 0.01 * np.sin(2 * x[i]) + 0.005 * np.sin(4 * x[i]) + 0.003 * np.sin(6 * x[i])
        result += multi_freq_term
        
        return result