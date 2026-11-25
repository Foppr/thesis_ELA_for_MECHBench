import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyperbolic tangent oscillations with dynamic frequencies and amplitudes
        tanh_component = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * (1.0 + 0.3 * np.sin(i * 0.5))
            amp = 1.0 / (1.0 + 0.1 * i)
            tanh_component += amp * np.tanh(freq * x_scaled[i])
        
        # Dynamic Gaussian peaks with position and width modulation
        gaussian_peaks = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.8) * 0.7 + 0.3 * np.cos(i * 0.3)
            width = 0.2 + 0.1 * np.sin(i * 0.6)
            gaussian_peaks += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Multi-scale cross-terms with varying interaction strengths and phase shifts
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = (i + 1) * (j + 1)
                phase = np.sin(0.4 * (i + j)) * np.cos(0.3 * (i - j))
                interaction = np.sin(scale * x_scaled[i] * x_scaled[j] + phase)
                cross_terms += interaction * (0.5 + 0.5 * np.sin(i * j * 0.2))
        
        # Chaotic cubic interactions with varying exponents and coupling
        chaotic_cubic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exponent_i = 1.5 + 0.5 * np.sin(i * 0.7)
                exponent_j = 2.0 + 0.3 * np.cos(j * 0.4)
                coupling = 0.8 + 0.2 * np.sin(i + j)
                chaotic_cubic += (x_scaled[i]**exponent_i) * (x_scaled[j]**exponent_j) * coupling
        
        # Logarithmic conditioning with distance-based scaling
        dist = np.sqrt(np.sum(x_scaled**2))
        conditioning = 1.2 * np.log(1.0 + dist**3)
        
        # Asymmetric sine modulation with frequency coupling
        asymmetric_sine = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(i * 0.8)
            asymmetry = 0.5 + 0.5 * np.cos(i * 0.3)
            asymmetric_sine += asymmetry * np.sin(freq_mod * x_scaled[i]) * np.cos(freq_mod * x_scaled[i])
        
        # Combine all components with carefully tuned weights
        return 1.5 * tanh_component + 2.0 * gaussian_peaks + 1.8 * cross_terms + 0.9 * chaotic_cubic + conditioning + 1.3 * asymmetric_sine