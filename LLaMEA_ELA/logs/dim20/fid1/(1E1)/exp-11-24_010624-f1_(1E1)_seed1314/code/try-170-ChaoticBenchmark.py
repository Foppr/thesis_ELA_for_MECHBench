import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with fractal-like variation
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.5) + 0.05 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with fractal radial symmetry and multi-frequency modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with fractal-like coupling
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            # Add fractal radial component with multiple frequency sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with multi-scale frequency modulation
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**7 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with fractal strength and multi-scale interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on both variables with modified exponent
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**2) * (1 + 0.2 * np.sin(x[i] * 0.5)))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.sin(0.3 * (i + j))
                
        # Add global scaling with multi-frequency components and fractal modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.sin(0.2 * dist_from_origin))
        
        # Add noise component with fractal structure to increase irregularity
        noise = 0.02 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Rosenbrock-like term with adaptive scaling for enhanced multimodality
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 150 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        result += 0.02 * rosenbrock_term
        
        # Add a periodic component with fractal frequencies to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
        result += 0.03 * periodic_term
        
        # Add a modified Schwefel function component with fractal-like structure
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i]))) * (1 + 0.1 * np.sin(0.5 * x[i]))
        result += 0.03 * schwefel_term
        
        # Add fractal saddle point component for increased conditioning difficulty
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.5 * (x[i]**4 - 2 * x[i]**2 + 1) * np.cos(3 * x[i])
        result += 0.015 * saddle_term
        
        # Add a multi-scale rotation component for increased complexity
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                rot_term += x[i] * x[j] * np.sin(0.5 * (x[i]**2 + x[j]**2))
        result += 0.025 * rot_term
        
        return result