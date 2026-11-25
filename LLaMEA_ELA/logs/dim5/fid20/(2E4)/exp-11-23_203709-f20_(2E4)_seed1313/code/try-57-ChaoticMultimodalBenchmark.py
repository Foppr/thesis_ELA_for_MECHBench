import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential terms with modified rates and amplitudes
        exp_potential = 0
        for i in range(self.dim):
            exp_potential += 1.5 * np.exp(-0.4 * np.abs(x[i])) * np.sin(2.5 * x[i]) + 0.6 * np.exp(-0.6 * np.abs(x[i])) * np.cos(2.0 * x[i])
        
        # Sinusoidal modulation terms with altered frequencies
        sin_mod = 0
        for i in range(self.dim):
            sin_mod += 1.8 * np.sin(3.5 * x[i] + 0.5) * np.cos(2.5 * x[i] - 0.3) + 1.1 * np.sin(4.5 * x[i] + 1.1)
        
        # Quaternion-inspired cross-dimensional interactions with modified coupling
        quaternion_like = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Simulate quaternion-like interaction using trigonometric combinations
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                dz = x[i] * x[j]
                quaternion_like += 0.8 * np.sin(1.5 * dx) * np.cos(2.0 * dy) * np.exp(-0.15 * np.abs(dz))
        
        # Radial component with modified exponential peaks
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 3.0 * np.exp(-0.25 * r_squared) * np.sin(3.5 * np.sqrt(r_squared)) + 1.5 * np.exp(-0.15 * r_squared) * np.cos(4.5 * np.sqrt(r_squared))
        
        # Add interaction terms between all dimensions with modified coupling strengths
        total_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                total_interaction += 0.6 * np.sin(3.0 * dx) * np.cos(1.5 * dy) + 0.4 * np.exp(-0.4 * (dx**2 + dy**2))
        
        # Combine all components with adjusted weights
        return 2.0 * exp_potential + 1.4 * sin_mod + 0.5 * radial + 0.3 * quaternion_like + 0.15 * total_interaction + 35 * self.dim