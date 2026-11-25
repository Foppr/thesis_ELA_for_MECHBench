import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential terms with varying rates and amplitudes
        exp_potential = 0
        for i in range(self.dim):
            exp_potential += 1.2 * np.exp(-0.3 * np.abs(x[i])) * np.sin(2.1 * x[i]) + 0.8 * np.exp(-0.5 * np.abs(x[i])) * np.cos(1.7 * x[i])
        
        # Sinusoidal modulation terms creating periodic oscillations
        sin_mod = 0
        for i in range(self.dim):
            sin_mod += 1.5 * np.sin(3.0 * x[i] + 0.5) * np.cos(2.0 * x[i] - 0.3) + 0.9 * np.sin(4.2 * x[i] + 1.1)
        
        # Quaternion-inspired cross-dimensional interactions with complex coupling
        quaternion_like = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Simulate quaternion-like interaction using trigonometric combinations
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                dz = x[i] * x[j]
                quaternion_like += 0.6 * np.sin(1.2 * dx) * np.cos(1.8 * dy) * np.exp(-0.1 * np.abs(dz))
        
        # Radial component with multiple exponential peaks
        radial = 0
        r_squared = np.sum(x ** 2)
        radial += 2.5 * np.exp(-0.2 * r_squared) * np.sin(3.0 * np.sqrt(r_squared)) + 1.3 * np.exp(-0.1 * r_squared) * np.cos(4.0 * np.sqrt(r_squared))
        
        # Add interaction terms between all dimensions with varying coupling strengths
        total_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dx = x[i] - x[j]
                dy = x[i] + x[j]
                total_interaction += 0.5 * np.sin(2.5 * dx) * np.cos(1.3 * dy) + 0.3 * np.exp(-0.3 * (dx**2 + dy**2))
        
        # Combine all components with appropriate weights
        return 1.8 * exp_potential + 1.2 * sin_mod + 0.4 * radial + 0.25 * quaternion_like + 0.1 * total_interaction + 30 * self.dim