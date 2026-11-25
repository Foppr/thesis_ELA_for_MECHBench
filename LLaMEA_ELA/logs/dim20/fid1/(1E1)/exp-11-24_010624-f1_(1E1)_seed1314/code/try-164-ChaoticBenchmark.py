import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with enhanced complexity
        self.chaos_params = np.array([3.8 + 0.1 * np.sin(i * 0.7) + 0.05 * np.cos(i * 0.3) + 0.02 * np.sin(i * 1.1) for i in range(dim)])
        # Rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to increase conditioning
        x_rotated = self.rotation @ x
        
        # Initialize result
        result = 0.0
        
        # Chaotic logistic map component with radial symmetry and sinusoidal modulation
        for i in range(self.dim):
            # Apply modified logistic map dynamics
            chaotic_val = self.chaos_params[i] * x_rotated[i] * (1 - x_rotated[i]**2)
            # Add radial component with sinusoidal modulation
            radial_term = 0.3 * x_rotated[i]**2 * np.sin(0.5 * x_rotated[i])
            result += chaotic_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation
        for i in range(self.dim):
            poly_term = 0.05 * x_rotated[i]**6 * np.cos(2 * x_rotated[i]) * np.exp(-0.1 * np.abs(x_rotated[i]))
            result += poly_term
            
        # Add cross-dimensional coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on both variables with modified exponent
                coupling_strength = np.exp(-0.03 * ((x_rotated[i] - x_rotated[j])**2 + (x_rotated[i] + x_rotated[j])**2))
                result += coupling_strength * np.sin(x_rotated[i] * x_rotated[j]) * np.cos(i - j)
                
        # Add global scaling with multiple frequency components
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.15 * np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin))
        
        # Add noise component to increase irregularity
        noise = 0.01 * np.sum(np.sin(x_rotated * 10))
        result += noise
        
        # Add a new component to improve conditioning and difficulty
        # Incorporate a modified Rosenbrock-like term for enhanced multimodality
        rosenbrock_term = 0.0
        for i in range(self.dim - 1):
            rosenbrock_term += 100 * (x_rotated[i+1] - x_rotated[i]**2)**2 + (1 - x_rotated[i])**2
        result += 0.015 * rosenbrock_term
        
        # Add a periodic component with altered frequencies to increase landscape complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4 * x_rotated[i]) * np.cos(6 * x_rotated[i])
        result += 0.025 * periodic_term
        
        # Add a new twist: introduce a modified Schwefel function component for increased multimodality and conditioning
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x_rotated[i] * np.sin(np.sqrt(np.abs(x_rotated[i])))
        result += 0.02 * schwefel_term
        
        # Add a new component: enhanced multimodal landscape using rotated Ackley function
        ackley_term = 0.0
        for i in range(self.dim):
            ackley_term += -20 * np.exp(-0.2 * np.sqrt(x_rotated[i]**2)) - np.exp(np.cos(2 * np.pi * x_rotated[i]) / self.dim) + 20 + np.e
        result += 0.03 * ackley_term
        
        # Add exponential conditioning factor to increase ill-conditioning
        cond_factor = np.exp(0.01 * np.sum(x**4))
        result *= cond_factor
        
        return result