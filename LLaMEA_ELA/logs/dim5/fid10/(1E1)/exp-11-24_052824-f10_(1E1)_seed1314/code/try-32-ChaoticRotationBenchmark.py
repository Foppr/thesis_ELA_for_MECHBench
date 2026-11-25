import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial potential
        r_squared = np.sum(x**2)
        radial = 0.1 * r_squared + 0.01 * r_squared**2
        
        # Sinusoidal oscillations in each dimension
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(10 * x[i]) * np.cos(5 * x[i])
        
        # Rotation-invariant chaotic component using matrix rotation
        chaotic = 0
        for i in range(self.dim):
            # Create a rotation matrix effect using cross-terms
            rot_sum = 0
            for j in range(self.dim):
                if i != j:
                    rot_sum += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
            chaotic += rot_sum**2
        
        # Polynomial interaction terms with varying exponents
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3 + x[j]**3) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Nested local minima using nested trigonometric functions
        nested = 0
        for i in range(self.dim):
            nested += np.sin(20 * x[i]) * np.cos(10 * x[i]) + np.sin(5 * x[i])**4
        
        # Combine all components with carefully tuned weights
        return radial + 0.5 * sin_component + 0.3 * chaotic + 0.4 * poly_interaction + 0.6 * nested + 20 * np.sum(np.abs(x)**3)