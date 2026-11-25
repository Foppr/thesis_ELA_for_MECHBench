import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with time-delayed variation
        self.chaos_params = np.array([3.8 + 0.1 * np.sin(i * 0.7) + 0.05 * np.cos(i * 0.3) + 0.02 * np.sin(i * 0.1) for i in range(dim)])
        # Time-delayed chaotic map parameters
        self.delay_params = np.array([0.5 + 0.2 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Time-delayed logistic map component with quaternion-inspired coupling
        for i in range(self.dim):
            # Apply time-delayed logistic map dynamics
            delayed_val = self.chaos_params[i] * x[i] * (1 - x[i]**2)
            # Add time-delayed effect
            if i > 0:
                delayed_val += self.delay_params[i] * x[i-1] * (1 - x[i-1]**2)
            # Add quaternion-inspired radial component
            radial_term = 0.3 * x[i]**2 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            result += delayed_val + radial_term
            
        # Add higher-order polynomial terms with frequency modulation and adaptive scaling
        for i in range(self.dim):
            poly_term = 0.05 * x[i]**5 * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i])) * (1 + 0.1 * np.sin(i))
            result += poly_term
            
        # Add cross-dimensional coupling with quaternion-inspired strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-inspired coupling strength based on both variables and their indices
                coupling_strength = np.exp(-0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**2)) * np.cos(i - j)
                result += coupling_strength * np.sin(x[i] * x[j]) * np.cos(i * j)
                
        # Add global scaling with multiple frequency components and adaptive noise
        dist_from_origin = np.sqrt(np.sum(x**2))
        result *= (1 + 0.15 * np.sin(0.3 * dist_from_origin) * np.cos(0.7 * dist_from_origin))
        
        # Add quaternion-inspired noise component to increase irregularity
        noise = 0.01 * np.sum(np.sin(x * 10) * np.cos(x * 0.5))
        result += noise
        
        # Add adaptive noise based on dimensionality
        adaptive_noise = 0.005 * np.sum(np.sin(x * (2 + self.dim * 0.1)))
        result += adaptive_noise
        
        return result