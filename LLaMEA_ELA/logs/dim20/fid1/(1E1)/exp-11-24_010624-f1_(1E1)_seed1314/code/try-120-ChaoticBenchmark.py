import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with hyperbolic tangent modulation
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2) * np.tanh(0.5 * x[i])
            # Add radial component with sinusoidal modulation
            radial_term = 0.3 * x[i]**2 * np.sin(0.5 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and tanh scaling
        for i in range(self.dim):
            poly_term = 0.05 * x[i]**5 * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i])) * np.tanh(0.3 * x[i])
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength and hyperbolic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with tanh modulation
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.tanh(0.2 * (x[i] * x[j]))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.exp(-0.01 * np.abs(i - j))
                
        # Add global scaling with multiple frequency components and hyperbolic modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.15 * np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin) * np.tanh(0.1 * dist_from_origin))
        
        # Add noise component to increase irregularity with hyperbolic modulation
        noise = 0.01 * np.sum(np.sin(x * 10) * np.tanh(x))
        result += noise
        
        # Add a new component to improve conditioning and difficulty - enhanced Rosenbrock-like term
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        result += 0.01 * rosenbrock_term * np.tanh(0.5 * rosenbrock_term)
        
        # Add a periodic component to increase landscape complexity with hyperbolic modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(3 * x[i]) * np.cos(5 * x[i]) * np.tanh(0.2 * x[i])
        result += 0.02 * periodic_term
        
        # Add a novel banana-shaped global structure with hyperbolic tangent modulation
        banana_term = 0.0
        for i in range(self.dim):
            banana_term += (x[i] - 1)**2 + 100 * (x[(i+1) % self.dim] - x[i]**2)**2
        result += 0.005 * banana_term * np.tanh(0.3 * banana_term)
        
        # Add a complex cross-dimensional interaction with multiple coupling types
        complex_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complex_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.cos(0.5 * (i + j))
        result += 0.015 * complex_coupling
        
        return result