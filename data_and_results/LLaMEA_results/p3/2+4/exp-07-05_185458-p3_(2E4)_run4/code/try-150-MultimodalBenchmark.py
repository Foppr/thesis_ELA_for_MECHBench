import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with chaotic center placements and modified weights
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3.0) * 0.9
            weight = 1.0 + 0.5 * np.sin(i * np.pi / 2.0)
            rb += weight * np.exp(-15 * (x_norm[i] - center)**2) * np.cos(20 * (x_norm[i] - center))
        
        # Enhanced chaotic cosine modulation with varying frequencies, amplitudes, and phase shifts
        chaos = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4 + 1) * np.pi
            amp = 0.7 + 0.3 * np.sin(i * np.pi / 4.0)
            phase = 0.5 * np.cos(i * np.pi / 5.0)
            chaos += amp * np.cos(freq * x_norm[i] + phase + np.sin(freq * x_norm[i]))
        
        # Enhanced asymmetric polynomial interactions with cross-dimensional coupling and modified exponents
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**4 + 0.4 * x_norm[i]**6 + 0.15 * x_norm[i]**8) * np.cos(x_norm[(i+1) % self.dim]) * np.sin(x_norm[(i+2) % self.dim])
        
        # Enhanced cross-dimensional coupling with sine-based interaction and additional interaction terms
        cross = 0.0
        for i in range(self.dim - 1):
            cross += np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**3 + x_norm[i+1]**3) + 0.5 * np.cos(x_norm[i] + x_norm[i+1])
        
        # Enhanced chaotic interference with exponential weighting and additional sine modulation
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-x_norm[i]**2) * np.sin(25 * x_norm[i] + np.cos(15 * x_norm[i])) + 0.3 * np.cos(30 * x_norm[i])
        
        # Additional high-frequency oscillation component with modified parameters
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(60 * x_norm[i]) * np.cos(50 * x_norm[i])
        
        # Novel cross-dimensional sine coupling terms for improved conditioning
        sine_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_coupling += 0.2 * np.sin(x_norm[i] * x_norm[j]) * np.cos(2 * (x_norm[i] + x_norm[j]))
        
        # Additional complex interaction terms with modified exponents and coupling
        complex_interaction = 0.0
        for i in range(self.dim):
            complex_interaction += (x_norm[i]**5 + 0.3 * x_norm[i]**7 + 0.1 * x_norm[i]**9) * np.sin(x_norm[(i+1) % self.dim]) * np.cos(x_norm[(i+2) % self.dim]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Additional multi-modal component with higher frequency sine terms
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += 0.5 * np.sin(40 * x_norm[i]) * np.cos(35 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Final combined function with carefully weighted components
        return 0.9 * rb + 0.7 * chaos + 0.5 * poly + 0.4 * cross + 0.3 * interference + 0.2 * high_freq + 0.1 * np.sum(x_norm**2) + 0.05 * sine_coupling + 0.15 * complex_interaction + 0.08 * multi_modal