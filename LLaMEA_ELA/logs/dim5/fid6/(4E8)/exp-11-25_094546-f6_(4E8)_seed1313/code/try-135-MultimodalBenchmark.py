import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = 3.9 + 0.1 * np.sin(i * 0.7)
            x_i = x_norm[i]
            chaotic += r * x_i * (1 - x_i)
        
        # Periodic orbit component with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            periodic += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric gradient flow component with saddle-point structure
        gradient = 0.0
        for i in range(self.dim):
            # Asymmetric quadratic terms
            asymmetry = 0.5 + 0.3 * np.sin(i * 0.4)
            quad_term = (x_norm[i]**2 + asymmetry * x_norm[i])**2
            gradient += quad_term
        
        # Embedded resonance component with cross-dimensional coupling
        resonance = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x_norm[i] + x_norm[j]))
                freq = 1.0 + 0.3 * np.cos(i * 0.2) * np.sin(j * 0.3)
                resonance += coupling * np.sin(freq * (x_norm[i] - x_norm[j]))
        
        # Dimensional scaling with fractal-like behavior
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.5) + 0.1 * np.cos(self.dim * 0.3)
        
        # Combine components with dynamic weighting based on dimensionality
        weight_chaotic = 0.3 + 0.1 * np.sin(self.dim * 0.2)
        weight_periodic = 0.4 + 0.15 * np.cos(self.dim * 0.15)
        weight_gradient = 0.2 + 0.05 * np.tanh(self.dim * 0.1)
        weight_resonance = 0.1
        
        return scale_factor * (weight_chaotic * chaotic + 
                              weight_periodic * periodic + 
                              weight_gradient * gradient + 
                              weight_resonance * resonance)