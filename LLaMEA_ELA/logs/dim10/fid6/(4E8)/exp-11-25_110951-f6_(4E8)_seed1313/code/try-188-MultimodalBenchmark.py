import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic with rotation and conditioning
        base_quad = np.sum(x_norm**2)
        
        # Asymmetric saddle points with varying curvature
        saddle = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            saddle += (x_norm[i]**2 - x_norm[j]**2)**2 + 0.3 * x_norm[i] * x_norm[j]
        
        # Multi-scale Gaussian interactions with varying widths and heights
        gaussian_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x_norm[i] - x_norm[j])**2
                gaussian_interaction += np.exp(-dist / (0.1 + 0.2 * np.sin(5 * (i + j)))) * \
                                       np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Non-linear frequency modulations with chaotic phase shifts
        freq_mod = 0.0
        for i in range(self.dim):
            freq_mod += np.sin(10 * x_norm[i] + np.sin(7 * x_norm[i]) * np.cos(4 * x_norm[i])) * \
                        np.cos(8 * x_norm[i] + np.cos(6 * x_norm[i]) * np.sin(3 * x_norm[i]))
        
        # Rotation-invariant chaotic structure with exponential decay
        rotation_invariant = 0.0
        for i in range(self.dim):
            rotation_invariant += np.exp(-2 * np.abs(x_norm[i])) * \
                                 np.sin(15 * x_norm[i] + 0.5 * np.sin(12 * x_norm[i]))
        
        # Sharp transition regions with hyperbolic tangent modulations
        sharp_transitions = 0.0
        for i in range(self.dim):
            sharp_transitions += np.tanh(5 * x_norm[i]) * np.sin(18 * x_norm[i])
        
        # Cross-dimensional coupling with asymmetric interaction strengths
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 4) % self.dim
            cross_coupling += np.sin(6 * x_norm[i]) * np.cos(9 * x_norm[j]) * \
                              np.exp(-0.5 * (x_norm[k] - 0.3)**2)
        
        # Final combined function with adaptive weights and chaotic complexity
        return 0.4 * base_quad + 0.25 * saddle + 0.15 * gaussian_interaction + \
               0.1 * freq_mod + 0.08 * rotation_invariant + 0.07 * sharp_transitions + \
               0.05 * cross_coupling