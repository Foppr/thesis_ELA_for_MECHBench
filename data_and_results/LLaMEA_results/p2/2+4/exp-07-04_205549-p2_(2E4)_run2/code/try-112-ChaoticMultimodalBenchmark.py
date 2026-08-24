import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0  # Time variable for dynamic components
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine-wave component with time-varying frequency
        chaotic = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(self.t + i * 0.5)
            chaotic += np.sin(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
            
        # Dynamic harmonic interaction terms
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(self.t * 0.3 + i * 0.2 + j * 0.1)
                harmonic += np.sin(15 * (x_norm[i] + x_norm[j]) + phase) * np.cos(10 * (x_norm[i] - x_norm[j]) + phase)
                
        # Saddle point modifier with dynamic strength
        saddle = 0.0
        strength = 2.0 + np.sin(self.t * 0.7)
        for i in range(self.dim):
            saddle += strength * x_norm[i]**3 * np.cos(5 * x_norm[i])
            
        # Time-varying penalty with chaotic modulation
        penalty = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.5 * np.sin(self.t + i * 0.3)
            penalty += mod * (x_norm[i]**6 - 3 * x_norm[i]**4 + 3 * x_norm[i]**2 - 1)
            
        # Multi-scale oscillation with adaptive frequency
        multi_scale = 0.0
        for i in range(self.dim):
            freq = 20.0 * (1.0 + 0.3 * np.sin(self.t * 0.5 + i * 0.4))
            multi_scale += np.sin(freq * x_norm[i]) * np.cos(12 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
            
        # Cross-dimensional exponential interaction with time modulation
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.2 * np.cos(self.t * 0.4 + i * 0.3 + j * 0.2)
                exp_interaction += mod * np.exp(-2.0 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(25 * (x_norm[i] - x_norm[j]))
                
        # Add time component to make function non-stationary
        self.t += 0.01
        
        return quadratic + chaotic + harmonic + saddle + penalty + multi_scale + exp_interaction