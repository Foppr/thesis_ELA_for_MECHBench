import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.harmonic_freq = 2.0
        self.fractal_dim = 1.3
        self.quaternion_scale = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator potential
        quantum_potential = np.sum((x**2) * np.sin(self.harmonic_freq * x)**2)
        
        # Fractal Brownian motion component using fractional Brownian motion approximation
        fbm = 0.0
        for i in range(self.dim):
            pos = x[i] / 5.0
            fbm += np.sin(pos * 10.0) * np.cos(pos * 7.0) * (np.abs(pos) ** self.fractal_dim)
        
        # Quaternion-based rotation matrix for cross-dimensional coupling
        rot_matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                if i == j:
                    rot_matrix[i, j] = 1.0
                else:
                    angle = (x[i] + x[j]) * 0.1
                    rot_matrix[i, j] = np.sin(angle) * np.cos(angle)
        
        # Apply rotation to the input vector and compute dot product
        rotated_x = np.dot(rot_matrix, x)
        rotation_component = np.sum(rotated_x**2) * 0.5
        
        # Non-differentiable component using absolute value and step functions
        non_diff = 0.0
        for i in range(self.dim):
            non_diff += np.abs(x[i]) * np.sin(x[i] * 3.0) + np.floor(np.abs(x[i]))
        
        # Combine all components with adaptive weights based on dimensionality
        weight_quantum = 1.0 / (1.0 + np.exp(-self.dim / 5.0))
        weight_fbm = 0.8 * np.sin(self.dim * 0.2) + 0.7
        weight_rotation = 0.5 * np.cos(self.dim * 0.3) + 0.6
        weight_non_diff = 0.4 * np.tanh(self.dim / 10.0) + 0.3
        
        f_val = (weight_quantum * quantum_potential + 
                 weight_fbm * fbm + 
                 weight_rotation * rotation_component + 
                 weight_non_diff * non_diff)
        
        # Add a global structure with periodic modulation
        periodic_mod = np.sum(np.sin(x * 0.5) * np.cos(x * 0.3))
        f_val += 0.2 * periodic_mod
        
        return f_val