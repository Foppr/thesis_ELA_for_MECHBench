import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.15 * np.sin(i * 0.9) + 0.08 * np.cos(i * 0.4) + 0.03 * np.sin(i * 1.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with enhanced radial symmetry and multi-frequency modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add complex radial component with multiple sinusoidal modulations
            radial_term = 0.4 * x[i]**2 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with multi-frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**7 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with adaptive strength and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with complex exponent and phase shift
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**3 + (x[i] + x[j])**3 + 0.5 * (x[i]**2 + x[j]**2)))
                result += coupling_strength * np.sin(x[i] * x[j] + 0.5 * (i - j)) * np.cos(0.7 * (i - j))
                
        # Add global scaling with multiple frequency components and amplitude modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add enhanced noise component for increased irregularity
        noise = 0.02 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty - enhanced Rosenbrock-like term
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 150 * (x[i+1] - x[i]**3)**2 + (1 - x[i])**3
        result += 0.02 * rosenbrock_term
        
        # Add a periodic component with more complex frequencies and phase relationships
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.sin(3 * x[i]**2)
        result += 0.03 * periodic_term
        
        # Add a modified Schwefel function component with altered parameters for increased multimodality
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(2 * np.abs(x[i])))
        result += 0.03 * schwefel_term
        
        # Add a new twist: introduce a modified Ackley-like component to further increase landscape complexity
        ackley_term = 0.0
        sum1 = np.sum(x**2)
        sum2 = np.sum(np.cos(2 * np.pi * x))
        ackley_term = -20 * np.exp(-0.2 * np.sqrt(sum1 / self.dim)) - np.exp(sum2 / self.dim) + 20 + np.e
        result += 0.025 * ackley_term
        
        # Add a final component: a modified Griewank-like term for additional multimodality
        griewank_term = 0.0
        griewank_term = np.sum(x**2 / 4000) - np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1)))) + 1
        result += 0.015 * griewank_term
        
        return result