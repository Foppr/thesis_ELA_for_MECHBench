import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperbolic tangent potentials with random amplitudes and frequencies
        self.tanh_amplitudes = np.random.rand(dim) * 2.0 + 1.0
        self.tanh_frequencies = np.random.rand(dim) * 3.0 + 1.0
        # Sinusoidal modulation parameters
        self.sin_amplitudes = np.random.rand(dim) * 1.5 + 0.5
        self.sin_frequencies = np.random.rand(dim) * 2.0 + 1.0
        # Saddle-point shaping parameters
        self.saddle_strengths = np.random.rand(dim) * 3.0 + 1.0
        self.saddle_angles = np.random.rand(dim) * np.pi
        # Adaptive scaling factors for chaotic behavior
        self.scaling_factors = np.random.rand(dim) * 2.0 + 1.0
        # Cross-dimensional coupling with chaotic interaction terms
        self.coupling_matrix = np.random.rand(dim, dim) * 0.8 - 0.4
        # Chaotic modulation frequencies
        self.chaos_freqs = np.random.rand(dim) * 5.0 + 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Hyperbolic tangent potential component
        tanh_potential = 0.0
        for i in range(self.dim):
            tanh_potential += self.tanh_amplitudes[i] * np.tanh(self.tanh_frequencies[i] * x_norm[i])
            
        # Sinusoidal modulation component
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i])
            
        # Saddle-point shaping component
        saddle_shaping = 0.0
        for i in range(self.dim):
            angle = self.saddle_angles[i]
            x_rot = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            saddle_shaping += self.saddle_strengths[i] * (x_rot**2 - y_rot**2)
            
        # Adaptive scaling component
        adaptive_scaling = 0.0
        for i in range(self.dim):
            adaptive_scaling += self.scaling_factors[i] * x_norm[i]**3
            
        # Cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.coupling_matrix[i, j] * np.sin(self.chaos_freqs[i] * x_norm[j])
        
        # Chaotic gradient component
        chaotic_gradient = 0.0
        for i in range(self.dim):
            chaotic_gradient += np.sin(x_norm[i] * self.chaos_freqs[i]) * np.cos(x_norm[i] * self.chaos_freqs[i])
            
        # Combined function with chaotic interactions
        return (1.5 * tanh_potential + 1.2 * sin_modulation + 0.8 * saddle_shaping + 
                0.6 * adaptive_scaling + 0.4 * cross_coupling + 0.3 * chaotic_gradient + 1.0)