import numpy as np

class SinusoidalPolynomialAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_component = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            sin_component += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Polynomial interaction terms with mixed degrees and cross-terms
        poly_component = 0.0
        for i in range(self.dim):
            poly_component += x_scaled[i]**4 + 0.5 * x_scaled[i]**3 + 0.2 * x_scaled[i]**2
            for j in range(i+1, min(i+3, self.dim)):
                poly_component += 0.3 * x_scaled[i] * x_scaled[j] + 0.1 * x_scaled[i]**2 * x_scaled[j]**2
        
        # Gradient-based attraction fields with position-dependent strengths
        attractor_component = 0.0
        for i in range(self.dim):
            # Multiple attraction centers with varying strengths and positions
            center1 = np.sin(i * 0.8) * 0.8
            center2 = np.cos(i * 0.6) * 0.6
            strength1 = 1.5 + 0.3 * np.sin(i * 0.4)
            strength2 = 1.0 + 0.2 * np.cos(i * 0.7)
            
            dist1 = (x_scaled[i] - center1)**2
            dist2 = (x_scaled[i] - center2)**2
            
            attractor_component += strength1 * np.exp(-dist1 * 2.0) + strength2 * np.exp(-dist2 * 3.0)
        
        # Cross-dimensional coupling with varying interaction strengths
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i + 4:  # Limited range coupling
                    coupling_strength = 0.5 * (1.0 + np.sin((i+j) * 0.3))
                    coupling_component += coupling_strength * np.sin(x_scaled[i] * x_scaled[j]) * \
                                        np.cos(0.5 * (x_scaled[i] + x_scaled[j]))
        
        # Mixed harmonic and exponential terms for enhanced complexity
        mixed_component = 0.0
        for i in range(self.dim):
            mixed_component += np.sin(x_scaled[i])**2 * np.exp(-x_scaled[i]**2) + \
                             np.cos(x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Combine all components with carefully tuned weights
        return 1.2 * sin_component + 0.8 * poly_component + 1.0 * attractor_component + \
               0.6 * coupling_component + 0.4 * mixed_component