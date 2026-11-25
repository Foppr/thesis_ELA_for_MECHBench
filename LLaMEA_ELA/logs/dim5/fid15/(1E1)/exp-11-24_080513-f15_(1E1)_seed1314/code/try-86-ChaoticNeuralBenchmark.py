import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters for each dimension
        self.r_values = 3.9 + 0.1 * np.sin(np.arange(dim) * 0.5)
        self.delay = 2 + (np.arange(dim) % 3)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic map component with time-delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            x_prev = np.sin(i * 0.3) if i >= self.delay[i] else 0.5
            x_current = x_norm[i]
            
            # Time-delayed chaotic dynamics
            if i >= self.delay[i]:
                x_delayed = x_norm[i - self.delay[i]]
                chaotic += (r * x_current * (1 - x_current) + 
                           0.3 * np.sin(x_delayed) * np.cos(x_current)) ** 2
        
        # Multi-scale neural coupling with sigmoidal activation
        neural = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                weight = 1.0 / (1.0 + np.exp(-5 * (dist - 0.5)))
                activation_i = 1.0 / (1.0 + np.exp(-3 * x_norm[i]))
                activation_j = 1.0 / (1.0 + np.exp(-3 * x_norm[j]))
                neural += weight * activation_i * activation_j * np.sin(10 * dist)
        
        # Attractor basin with varying depth and width
        basin = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.4) * 0.5
            width = 0.3 + 0.2 * np.cos(i * 0.6)
            depth = 1.0 + 0.5 * np.sin(i * 0.8)
            basin += depth * np.exp(-0.5 * ((x_norm[i] - center) / width)**2) * np.cos(3 * x_norm[i])
        
        # Discontinuous jump component with fractal-like distribution
        jump = 0.0
        for i in range(self.dim):
            jump += np.floor(5 * x_norm[i]) * np.sin(2 * np.pi * x_norm[i]) + \
                   np.cos(np.pi * x_norm[i] ** 3) * np.tanh(x_norm[i])
        
        # Resonance coupling with frequency modulation
        resonance = 0.0
        for i in range(self.dim):
            freq_i = 2.0 + 0.5 * np.sin(i * 0.7)
            phase_i = 0.1 * np.cos(i * 0.9)
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                freq_j = 2.0 + 0.5 * np.sin(j * 0.7)
                phase_j = 0.1 * np.cos(j * 0.9)
                resonance += np.sin(freq_i * x_norm[i] + phase_i) * \
                           np.cos(freq_j * x_norm[j] + phase_j) * \
                           np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Combine components with adaptive weights
        return (0.3 * chaotic + 0.25 * neural + 0.2 * basin + 
                0.15 * jump + 0.1 * resonance)