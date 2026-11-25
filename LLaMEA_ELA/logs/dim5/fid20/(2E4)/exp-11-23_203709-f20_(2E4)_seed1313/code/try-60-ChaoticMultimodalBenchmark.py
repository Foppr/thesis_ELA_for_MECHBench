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
            exp_potential += 1.7 * np.exp(-0.35 * np.abs(x[i])) * np.sin(2.8 * x[i]) + 0.5 * np.exp(-0.55 * np.abs(x[i])) * np.cos(2.2 * x[i])
        
        # Sinusoidal modulation terms with altered frequencies
        sin_mod = 0
        for i in range(self.dim):
            sin_mod += 2.0 * np.sin(3.8 * x[i] + 0.6) * np.cos(2.8 * x[i] - 0.4) + 1.3 * np.sin(4.8 * x[i] + 1.2)
        
        # Quaternion-inspired cross-dimensional interactions with modified coupling
        quaternion_like = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Simulate quaternion-like interaction using trigonometric combinations
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                dz = x[i] * x[j]
                quaternion_like += 0.9 * np.sin(1.7 * dx) * np.cos(2.2 * dy) * np.exp(-0.2 * np.abs(dz))
        
        # Radial component with modified exponential peaks
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 3.5 * np.exp(-0.3 * r_squared) * np.sin(3.8 * np.sqrt(r_squared)) + 1.7 * np.exp(-0.2 * r_squared) * np.cos(4.8 * np.sqrt(r_squared))
        
        # Add interaction terms between all dimensions with modified coupling strengths
        total_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                total_interaction += 0.7 * np.sin(3.2 * dx) * np.cos(1.7 * dy) + 0.5 * np.exp(-0.45 * (dx**2 + dy**2))
        
        # Combine all components with adjusted weights
        return 2.2 * exp_potential + 1.6 * sin_mod + 0.6 * radial + 0.35 * quaternion_like + 0.2 * total_interaction + 37 * self.dim