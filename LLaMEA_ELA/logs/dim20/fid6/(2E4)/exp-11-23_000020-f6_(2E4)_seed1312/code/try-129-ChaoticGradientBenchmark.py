import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced hyperbolic tangent potentials with multi-scale frequencies
        self.tanh_amplitudes = np.random.rand(dim) * 3.0 + 1.0
        self.tanh_frequencies = np.random.rand(dim) * 5.0 + 2.0
        # Multi-scale sinusoidal modulation with phase shifts
        self.sin_amplitudes = np.random.rand(dim) * 2.0 + 1.0
        self.sin_frequencies = np.random.rand(dim) * 4.0 + 1.0
        self.sin_phases = np.random.rand(dim) * np.pi
        # Enhanced saddle-point shaping with elliptic and hyperbolic components
        self.saddle_strengths = np.random.rand(dim) * 4.0 + 2.0
        self.saddle_angles = np.random.rand(dim) * np.pi * 2.0
        self.saddle_types = np.random.choice([0, 1], dim)  # 0 for elliptic, 1 for hyperbolic
        # Adaptive scaling with polynomial and exponential components
        self.scaling_factors = np.random.rand(dim) * 3.0 + 1.0
        self.exponential_factors = np.random.rand(dim) * 2.0 + 1.0
        # Enhanced cross-dimensional coupling with resonance interactions
        self.coupling_matrix = np.random.rand(dim, dim) * 1.2 - 0.6
        self.resonance_freqs = np.random.rand(dim) * 6.0 + 3.0
        # Additional chaotic modulation with logistic map behavior
        self.chaos_freqs = np.random.rand(dim) * 8.0 + 4.0
        self.logistic_r = np.random.rand(dim) * 3.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced hyperbolic tangent potential component
        tanh_potential = 0.0
        for i in range(self.dim):
            tanh_potential += self.tanh_amplitudes[i] * np.tanh(self.tanh_frequencies[i] * x_norm[i])
            
        # Multi-scale sinusoidal modulation component
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i] + self.sin_phases[i])
            
        # Enhanced saddle-point shaping component
        saddle_shaping = 0.0
        for i in range(self.dim):
            angle = self.saddle_angles[i]
            x_rot = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            
            if self.saddle_types[i] == 0:  # Elliptic saddle
                saddle_shaping += self.saddle_strengths[i] * (x_rot**2 + y_rot**2)
            else:  # Hyperbolic saddle
                saddle_shaping += self.saddle_strengths[i] * (x_rot**2 - y_rot**2)
            
        # Adaptive scaling with polynomial and exponential components
        adaptive_scaling = 0.0
        for i in range(self.dim):
            adaptive_scaling += self.scaling_factors[i] * x_norm[i]**3 + self.exponential_factors[i] * np.exp(-x_norm[i]**2)
            
        # Enhanced cross-dimensional coupling with resonance interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.coupling_matrix[i, j] * np.sin(self.resonance_freqs[i] * x_norm[j])
        
        # Chaotic gradient component with logistic map behavior
        chaotic_gradient = 0.0
        for i in range(self.dim):
            chaotic_gradient += np.sin(x_norm[i] * self.chaos_freqs[i]) * np.cos(x_norm[i] * self.chaos_freqs[i])
            # Logistic map component
            logistic_term = self.logistic_r[i] * x_norm[i] * (1 - x_norm[i])
            chaotic_gradient += 0.5 * logistic_term
            
        # Combined function with enhanced chaotic interactions
        return (2.0 * tanh_potential + 1.5 * sin_modulation + 1.0 * saddle_shaping + 
                0.8 * adaptive_scaling + 0.6 * cross_coupling + 0.5 * chaotic_gradient + 1.5)