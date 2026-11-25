import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.8
        self.beta = 2.5
        self.gamma = 1.2
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.alpha * np.sin(i * 0.4))
            
        # Enhanced sine-wave interaction terms with variable frequencies
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_factor = 1.2 + 0.3 * np.sin(i * 0.3) * np.cos(j * 0.2)
                sine_interaction += np.sin(freq_factor * x[i] * x[j]) * np.cos(self.beta * (x[i] + x[j]))
                
        # Polynomial chaos component with dynamic weights and adaptive exponents
        chaos_term = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.5 * np.sin(i * 0.6)
            chaos_term += (x[i]**(4*exp_factor) + self.gamma * x[i]**(6*exp_factor)) * np.exp(-0.2 * x[i]**2)
            
        # Enhanced cross-dimensional coupling with dynamic strength and phase
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.3 + 0.2 * np.sin(i * 0.5) * np.cos(j * 0.4)
                coupling += (x[i] * x[j]) * np.sin(2.0 * np.pi * (x[i] - x[j])) * strength
                           
        # Non-convex penalty with adaptive polynomial terms and directional modulation
        penalty = 0.0
        for i in range(self.dim):
            mod_factor = 1.0 + 0.4 * np.sin(i * 0.25)
            penalty += (x[i]**(8*mod_factor) + x[i]**(5*mod_factor) + x[i]**(3*mod_factor)) * (1 + self.beta * np.sin(i * 0.3))
            
        # Add a new adaptive multi-modal component
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * (1 + 0.2 * np.sin(i * 0.5))
            
        return result + 0.4 * sine_interaction + 0.3 * chaos_term + 0.25 * coupling + 0.4 * penalty + 0.15 * multimodal