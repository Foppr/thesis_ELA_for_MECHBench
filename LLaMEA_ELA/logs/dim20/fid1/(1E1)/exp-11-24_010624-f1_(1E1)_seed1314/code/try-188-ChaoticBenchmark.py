import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with more complex variation
        self.chaos_params = np.array([3.8 + 0.1 * np.sin(i * 0.7) + 0.05 * np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            # Add radial component with sinusoidal modulation
            radial_term = 0.3 * x[i]**2 * np.sin(0.5 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation
        for i in range(self.dim):
            poly_term = 0.05 * x[i]**6 * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with modified exponent
                coupling_strength = np.exp(-0.03 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j)
                
        # Add global scaling with multiple frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.15 * np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin))
        
        # Add noise component to increase irregularity
        noise = 0.01 * np.sum(np.sin(x * 10))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Rosenbrock-like term for enhanced multimodality
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        result += 0.015 * rosenbrock_term
        
        # Add a periodic component with altered frequencies to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4 * x[i]) * np.cos(6 * x[i])
        result += 0.025 * periodic_term
        
        # Add a new twist: introduce a modified Schwefel function component for increased multimodality and conditioning
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.02 * schwefel_term
        
        # Add a new twist: introduce a modified Ackley-like function component to increase multimodality and conditioning
        ackley_term = 0.0
        sum1 = np.sum(x**2)
        sum2 = np.sum(np.cos(2 * np.pi * x))
        ackley_term = -20 * np.exp(-0.2 * np.sqrt(sum1 / self.dim)) - np.exp(sum2 / self.dim) + 20 + np.e
        result += 0.01 * ackley_term
        
        # Add a new twist: introduce a modified Griewank-like function component to increase multimodality and conditioning
        griewank_term = 0.0
        sum3 = np.sum(x**2 / 4000)
        prod = np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1))))
        griewank_term = sum3 - prod + 1
        result += 0.005 * griewank_term
        
        return result