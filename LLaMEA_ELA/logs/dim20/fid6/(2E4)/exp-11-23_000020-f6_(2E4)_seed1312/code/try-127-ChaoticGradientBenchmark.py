import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced hyperbolic tangent potentials with increased nonlinearity
        self.tanh_amplitudes = np.random.rand(dim) * 3.0 + 2.0
        self.tanh_frequencies = np.random.rand(dim) * 4.0 + 2.0
        # Modified sinusoidal modulation with higher frequency components
        self.sin_amplitudes = np.random.rand(dim) * 2.0 + 1.0
        self.sin_frequencies = np.random.rand(dim) * 3.0 + 2.0
        # Improved saddle-point shaping with elliptic curvature
        self.saddle_strengths = np.random.rand(dim) * 4.0 + 2.0
        self.saddle_angles = np.random.rand(dim) * np.pi
        # Enhanced adaptive scaling factors
        self.scaling_factors = np.random.rand(dim) * 3.0 + 2.0
        # Modified cross-dimensional coupling with stronger interactions
        self.coupling_matrix = np.random.rand(dim, dim) * 1.2 - 0.6
        # Enhanced chaotic modulation frequencies
        self.chaos_freqs = np.random.rand(dim) * 7.0 + 3.0
        # Additional quadratic terms for increased complexity
        self.quad_coeffs = np.random.rand(dim) * 2.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced hyperbolic tangent potential component
        tanh_potential = 0.0
        for i in range(self.dim):
            tanh_potential += self.tanh_amplitudes[i] * np.tanh(self.tanh_frequencies[i] * x_norm[i])
            
        # Modified sinusoidal modulation component
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i])
            
        # Improved saddle-point shaping component with elliptic curvature
        saddle_shaping = 0.0
        for i in range(self.dim):
            angle = self.saddle_angles[i]
            x_rot = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            saddle_shaping += self.saddle_strengths[i] * (x_rot**2 - y_rot**2)
            
        # Enhanced adaptive scaling component
        adaptive_scaling = 0.0
        for i in range(self.dim):
            adaptive_scaling += self.scaling_factors[i] * x_norm[i]**3
            
        # Modified cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.coupling_matrix[i, j] * np.sin(self.chaos_freqs[i] * x_norm[j])
        
        # Enhanced chaotic gradient component
        chaotic_gradient = 0.0
        for i in range(self.dim):
            chaotic_gradient += np.sin(x_norm[i] * self.chaos_freqs[i]) * np.cos(x_norm[i] * self.chaos_freqs[i])
            
        # Additional quadratic terms for increased landscape complexity
        quadratic_terms = 0.0
        for i in range(self.dim):
            quadratic_terms += self.quad_coeffs[i] * x_norm[i]**2
            
        # Combined function with enhanced chaotic interactions and increased complexity
        return (2.0 * tanh_potential + 1.5 * sin_modulation + 1.0 * saddle_shaping + 
                0.8 * adaptive_scaling + 0.6 * cross_coupling + 0.5 * chaotic_gradient + 
                0.4 * quadratic_terms + 1.5)