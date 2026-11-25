import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with increased complexity and variability
        self.chaos_params = np.array([3.8 + 0.2 * np.sin(i * 0.9) + 0.1 * np.cos(i * 0.4) + 0.05 * np.sin(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics with higher nonlinearity
            chaotic_val = self.chaos_params[i] * x[i] * (1 - x[i]**3)
            # Add radial component with enhanced sinusoidal modulation
            radial_term = 0.4 * x[i]**2 * np.sin(0.7 * x[i]) + 0.1 * x[i]**4 * np.cos(0.3 * x[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and exponential decay
        for i in range(self.dim):
            poly_term = 0.08 * x[i]**7 * np.cos(2.5 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength and additional trigonometric modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with modified exponent and phase shift
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**3))
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i - j) * np.sin(0.5 * (x[i] + x[j]))
                
        # Add global scaling with multiple frequency components and phase modulation
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.2 * np.sin(0.4 * dist_from_origin) * np.cos(0.8 * dist_from_origin) * np.exp(-0.05 * dist_from_origin))
        
        # Add noise component to increase irregularity with enhanced frequency
        noise = 0.02 * np.sum(np.sin(x * 15) + 0.5 * np.cos(x * 8))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Rosenbrock-like term for enhanced multimodality with variable coefficients
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 150 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2 * np.sin(0.5 * x[i])
        result += 0.02 * rosenbrock_term
        
        # Add a periodic component with altered frequencies, phase shifts, and amplitude modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += (np.sin(5 * x[i]) + 0.3 * np.cos(7 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.03 * periodic_term
        
        # Add a novel fractal-like component to increase landscape complexity and conditioning
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += 0.5 * np.sin(10 * x[i]) * np.cos(12 * x[i]) * (1 + 0.2 * np.sin(3 * x[i]))
        result += 0.015 * fractal_term
        
        return result