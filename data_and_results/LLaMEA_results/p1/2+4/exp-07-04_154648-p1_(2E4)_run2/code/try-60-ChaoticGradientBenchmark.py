import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.frequency_coeffs = np.random.uniform(1.0, 8.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.curvature_modulators = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        # Chaotic sinusoidal base with dynamic frequencies
        chaotic_base = 0.0
        for i in range(self.dim):
            freq = self.frequency_coeffs[i] * (1.0 + 0.3 * np.sin(3.0 * x_norm[i]))
            chaotic_base += np.sin(freq * x_norm[i] + self.phase_shifts[i]) * \
                           np.cos(freq * x_norm[i] * 0.7 + self.phase_shifts[i] * 1.3) * \
                           self.coupling_coeffs[i]
        
        # Saddle point interactions with position-dependent strength
        saddle_interaction = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            strength = 1.0 / (1.0 + distance**2)
            saddle_interaction += strength * np.sin(2.0 * distance) * np.cos(1.5 * distance)
        
        # Varying curvature terms that create dynamic landscape
        curvature_term = 0.0
        for i in range(self.dim):
            curvature = self.curvature_modulators[i] * (1.0 + 0.5 * np.sin(4.0 * x_norm[i]))
            curvature_term += curvature * x_norm[i]**4
        
        # Non-smooth components with discontinuous gradients
        nonsmooth = 0.0
        for i in range(self.dim):
            nonsmooth += np.abs(x_norm[i]) * np.sin(10.0 * x_norm[i]) * \
                        (0.5 + 0.5 * np.tanh(5.0 * x_norm[i]))
        
        # Cross-dimensional coupling with chaotic interaction weights
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.sin(2.0 * (x_norm[i] + x_norm[i+1])) * \
                    np.cos(1.5 * (x_norm[i] - x_norm[i+1]))
            cross_coupling += weight * (x_norm[i]**3 + x_norm[i+1]**3)
        
        # Global minimum at origin with additional penalty for proximity to critical points
        penalty = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            penalty += 1.0 / (1.0 + distance**3)
        
        return chaotic_base + saddle_interaction + curvature_term + nonsmooth + cross_coupling + 0.3 * penalty