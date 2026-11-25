import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic-like maps with dynamic parameters
        chaotic = 0
        for i in range(self.dim):
            # Dynamic parameter based on position and dimension
            r = 3.8 + 0.2 * np.sin(i * np.pi / self.dim)
            x_i = x_norm[i]
            chaotic += (r * x_i * (1 - x_i)) / (1.0 + i * 0.1)
        
        # Polynomial potential component with nested interactions
        polynomial = 0
        for i in range(self.dim):
            # Nested polynomial terms with varying degrees
            poly_term = x_norm[i]**(2 + i % 3) + 0.5 * x_norm[i]**(3 + i % 4)
            polynomial += poly_term / (1.0 + i * 0.05)
        
        # Multi-scale correlation structure with dynamic phase shifts
        correlation = 0
        phases = [np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
        for i in range(self.dim):
            phase_idx = i % len(phases)
            phase_shift = phases[phase_idx]
            # Correlated terms with varying interaction strength
            corr_term = np.sin(x_norm[i] + phase_shift) * np.cos(2 * x_norm[i] + phase_shift)
            correlation += corr_term / (1.0 + 0.1 * i)
        
        # Dynamic ridge structure with varying curvature
        ridge = 0
        for i in range(self.dim):
            # Create ridges with varying steepness and width
            ridge_width = 0.5 + 0.3 * np.cos(i * np.pi / self.dim)
            steepness = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 1))
            ridge += steepness * np.exp(-0.5 * ((x_norm[i] / ridge_width)**2)) * np.cos(3 * x_norm[i])
        
        # Asymmetric curvature with exponential weighting
        curvature = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                curvature += (x_norm[i]**4) * np.exp(-0.5 * x_norm[i]**2)
            else:
                curvature += (x_norm[i]**6) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combined result with adaptive weights
        result = 1.2 * chaotic + 1.8 * polynomial + 1.5 * correlation + 0.8 * ridge + 0.6 * curvature
        
        return result